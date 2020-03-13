# combinePdfs.py - Combines all the PDFs in the current working directory into
# a single PDF.

import PyPDF2, os

# getting all the PDF filenames
pdfFiles = []
for filename in os.listdir('.\pdfs'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
    pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()
print(pdfFiles)

# looping through all the PDF files
for file in pdfFiles:
    filename = '.\pdfs\\' + file
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    if pdfReader.isEncrypted:
        for password in ['rosebud', 'swordfish']:
            if pdfReader.decrypt(password) == 1:
                break

    # looping through all pages (except the first one)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    # saving the resulting PDF to a file
    pdfOutput = open('allminutes.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()
    
