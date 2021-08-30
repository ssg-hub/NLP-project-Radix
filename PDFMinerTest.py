from pdfminer.high_level import extract_text
 
text = extract_text("apple_10k.pdf")
 
print(text)