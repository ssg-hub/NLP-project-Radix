import PyPDF2

pdfobject = open('/Users/paww/Documents/GitHub/NLP-project-Radix/assets/pdf/27.pdf','rb')

pdfreader = PyPDF2.PdfFileReader(pdfobject)
pdfreader.read()
print(pdfreader)

dictionary = pdfreader.getFormTextFields()

print(dictionary)