"""Created by Jonathan Rach for the SwampHacks 2016 Hackathon Project"""
"""This file contains code that uses the PyPDF2 library to convert the pdf to text for analysis with the DatumBox API"""
"""Inspiration for this code from https://automatetheboringstuff.com/chapter13/"""
import PyPDF2

#Method to return the text from each page of a pdf
def getText(PATH):
    i=0
    totalText = ""
    pdfFileObj = open (PATH, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print "This pdf has %i pages" % pdfReader.numPages
    while (i<pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        totalText += pageObj.extractText()
        i+=1
    return totalText

