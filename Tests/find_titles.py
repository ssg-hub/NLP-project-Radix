from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
import pdfminer


def createPDFDoc(fpath):
    fp = open(fpath, 'rb')
    parser = PDFParser(fp)
    document = PDFDocument(parser)
    return document


def createDeviceInterpreter():
    rsrcmgr = PDFResourceManager()
    laparams = LAParams(detect_vertical = True, line_margin = 1.3, boxes_flow = -1)
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    return device, interpreter


def parse_obj(objs):
    for obj in objs:
        if isinstance(obj, pdfminer.layout.LTTextBox):
            print(obj)
        # if it's a container, recurse
        elif isinstance(obj, pdfminer.layout.LTFigure):
            parse_obj(obj._objs)
        else:
            pass


document = createPDFDoc("/home/becode/Documents/GitHub/NLP-project-Radix/assets/pdfs/1964.pdf")
device,interpreter = createDeviceInterpreter()
pages = PDFPage.create_pages(document)
for page in pages:
    interpreter.process_page(page)

layout = device.get_result()

result = parse_obj(layout._objs)
print(result)