import pandas as pd
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import json
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
            converter = TextConverter(rsrcmgr, fake_file_handle, laparams = laparams)
            page_interpreter = PDFPageInterpreter(rsrcmgr, converter)
            page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()

            # close open handles
            converter.close()
            fake_file_handle.close()

            return text

def fromSkillsPDF(bigram):
    with open("/home/becode/Documents/GitHub/NLP-project-Radix/assets/cleaned_related_skills.json") as db:
        data = db.readlines()
        data = data[0].replace("}","},")
        data = '['+data[:-1]+']'
        data = json.loads(data)

    dict_ = {}
    for dat in data:
        skill = dat['name']
        related_skills = []
        for i in range(1, 11):
            related_skills.append(dat['related_'+str(i)])
        dict_[skill] = related_skills

    # x = pd.DataFrame.from_dict(dict_)

    pat = '|'.join(" ".join(item) for item in bigram)

    skills = []
    for i in pat:
        skills.append(dict_.findall(pat))
    
    return skills