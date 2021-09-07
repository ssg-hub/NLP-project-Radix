from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io


def extract_text_from_pdf(pdf_path):
    '''
    Helper function to extract the plain text from .pdf files

    :param pdf_path: path to PDF file to be extracted
    :return: iterator of string of extracted text
    '''
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            rsrcmgr = PDFResourceManager()
            laparams = LAParams(detect_vertical = True, line_margin = 1.3, boxes_flow = -1)
            fake_file_handle = io.StringIO()
            converter = TextConverter(rsrcmgr, fake_file_handle, codec='utf-8', laparams = laparams)
            page_interpreter = PDFPageInterpreter(rsrcmgr, converter)
            page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()
            print(text)
 
            # close open handles
            converter.close()
            fake_file_handle.close() 

alltext = extract_text_from_pdf("/Users/paww/Documents/GitHub/NLP-project-Radix/assets/pdf/456.pdf")
print(type(alltext))