#from extract import pdf_to_text
from functions import preprocess, pdf_to_text

#pdf name 
pdf = '/home/becode/Documents/Projects/9.RadixNLP/curriculum_vitae_data-master/pdf/526.pdf'

pages, text = pdf_to_text(pdf)

a = preprocess(text)
#print(a)
#b = named_entities(a)

nnp_list = []
for token, tag in a:
    if tag == "NNP":
        nnp_list.append(token)

#print(nnp_list)

tags_for_name = nnp_list[:10] #will def have name , will use later
print(tags_for_name)