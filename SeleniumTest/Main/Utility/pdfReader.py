import os
import PyPDF2


class PDFReader:
    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+"/TestResources/downloads/"

    def verifyText(self,sFileName,sValue):
        #print(self.path+sFileName+'.pdf')
        pdfFileObj = open(self.path+sFileName+'.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
        # number of pages in pdf
        # print(pdfReader.numPages)
        # a page object
        pageObj = pdfReader.getPage(0)
        # extracting text from page.
        # this will print the text you can also save that into String
        asd = pageObj.extractText()


#PDFReader().verifyText("IN125314",'GHPCGMMJX')