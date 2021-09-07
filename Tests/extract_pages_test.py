from pdfminer.high_level import extract_pages

for page_layout in extract_pages("/Users/paww/Documents/GitHub/NLP-project-Radix/assets/pdf/39.pdf"):
    for element in page_layout:
        print(element)