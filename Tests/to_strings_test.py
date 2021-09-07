from io import StringIO
import re

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

# def get_string():
output_string = StringIO()
with open('/Users/paww/Documents/GitHub/NLP-project-Radix/assets/pdf/214.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

text = output_string.getvalue()
print(text)

# match = re.findall(r"(\+?\d{2} .\d+ | )", text)
# print(match)

schooling = re.findall("education")
if schooling in text:
    education = text.split(schooling)
    print(education)