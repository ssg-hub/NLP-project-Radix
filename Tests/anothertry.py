from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

import io
import os

fp = open("/Users/paww/Documents/GitHub/NLP-project-Radix/assets/pdf/456.pdf", 'rb')
rsrcmgr = PDFResourceManager()
retstr = io.StringIO()
print(type(retstr))
codec = 'utf-8'
laparams = LAParams()
device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)

page_no = 0
for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
    if pageNumber == page_no:
        interpreter.process_page(page)

        data = retstr.getvalue()

        with open(os.path.join("/Users/paww/Documents/GitHub/NLP-project-Radix/assets", f'pdf page {page_no}.txt'), 'wb') as file:
            file.read(data.encode('utf-8'))
        data = ''
        retstr.truncate(0)
        retstr.seek(0)

    page_no += 1