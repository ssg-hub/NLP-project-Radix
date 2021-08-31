from pdfminer.high_level import extract_text
 
text = extract_text("pdf/27.pdf")
 
print(text)