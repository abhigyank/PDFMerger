#combinePDFs

import PyPDF2, os


def mergeDefault():

	files = []
	for filename in os.listdir('pdf'):
		if filename.endswith('pdf'):

			files.append(filename)
	os.chdir('pdf')
	writer = PyPDF2.PdfFileWriter()
	files.sort(key = str.lower)
	#os.getcwd()



	for filename in files:

		fileObj = open (filename,'rb') 
		reader = PyPDF2.PdfFileReader(fileObj)
		for pageNum in range(0,reader.numPages):
			pageObj = reader.getPage(pageNum)
			writer.addPage(pageObj)
		

	resultPdf = open('FinalPDF.pdf','wb')
	writer.write(resultPdf)
	fileObj.close()
	resultPdf.close()

def decide():
	global var
	num = var.get()
	if num == 1:
		mergeDefault()
from Tkinter import *
top = Tk()
top.title('Merge PDFs')

string = StringVar()
label = Label(top, textvariable=string )
string.set("All PDFs in the set directory will be merged according to alphabetical order of file name.\n To Merge check the box below and start merge.")
label.pack()

var = IntVar()
C = Checkbutton(top, text = "Merge all PDFs directly", variable = var)
C.pack()

b = Button(top,text='Start Merging',command=decide)
b.pack()

a= Button(top, text="Close", command=quit)
a.pack()

top.mainloop()


