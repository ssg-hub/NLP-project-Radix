from pdfminer.high_level import extract_pages
from pdfminer.layout import LAParams, LTTextBox, LTTextContainer

laparams = LAParams(detect_vertical = True, line_margin = 1.3, word_margin = 20, boxes_flow = 0)
for page_layout in extract_pages("/Users/paww/Documents/GitHub/NLP-project-Radix/assets/pdf/2214.pdf", laparams = laparams):
    for element in page_layout:
        print("New textbox: ", LTTextBox)
        if isinstance(element, LTTextContainer):
            print("New Element: ", element.get_text())