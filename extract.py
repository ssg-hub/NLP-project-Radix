from numpy import concatenate
import pandas as pd
import fitz
import nltk
import PyPDF2
import spacy
from spacy.lang.en import English
from spacy import displacy
import re

'''# using PyPDF2
pdf1File = open('NLP-project-Radix/sample-the-seeker-resume.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
print(pdf1Reader.numPages)
pageObj = pdf1Reader.getPage(0)
print(pageObj.extractText())'''

# using PyMuPDF and fitz

'''doc = fitz.open(pdf)
for page in doc:
    text = page.getText("text")
    # html_text = page.getText("html")
    # print(text)
    # print(html_text)'''


def pdf_to_text(pdf_name : str) ->  str:
    """
    Function to get all the pages of given pdf in text format.
    """
    doc = fitz.open(pdf_name)
    full_text = ''
    for page in doc:
        text = page.getText("text")
        full_text = full_text + ' ' + text
    return doc, full_text

pdf = '/home/becode/Documents/Projects/9.RadixNLP/curriculum_vitae_data-master/pdf/41.pdf'

#create the nlp object
nlp = spacy.load('en_core_web_sm')


#print(doc)
print('check 2')

def text_to_df( text : str) -> pd.DataFrame :
    """
    Function to generate a dataframe with words and types from given text
    """

    # Creating a doc by processing the given text with an nlp object
    doc = nlp(text)

    # create a 2 column empty dataframe
    df = pd.DataFrame(columns = ['token_text', 'token_label' ])

    # Populating the dataframe with the word and its type
    for ent in doc.ents:
        #print(ent.text, ent.label_)
        df.loc[df.shape[0]] = [ent.text, ent.label_]

    return df

pages, text = pdf_to_text(pdf)
data = text_to_df(text)

#print(data.head())

# grouping by token_label
label_groups = data.groupby('token_label')
print(label_groups.head())

# Let's print the first entries in all the groups formed.
label_groups_first = label_groups.first()
#print(label_groups_first)

# list of all unique token labels
labels_list = list(label_groups_first.index.values)

'''for item in labels_list:
    # Finding the values contained in the token group
    print(item, len(label_groups.get_group(item)))'''
####################################################################
ds = data.loc[data['token_label'] == 'Language'].groupby('token_label')
print(ds.head())

doc = nlp(text)
'''for token in doc:
    print(token, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)'''

#trying other method
print('check 3')
lines = [each.strip() for each in text.split("\n") if len(each) > 0]
#print(lines[3:15])
lines = [nltk.word_tokenize(each) for each in lines]
lines = [nltk.pos_tag(each) for each in lines]
#print(lines[3:20])

phone_regex = re.compile(r'[\+\()]*[1-9][0-9 .\-\(\)]{8,}[0-9]')

def extract_phone_number(cv_text):
    phone = re.findall(phone_regex, cv_text)
    
    numbers = []
    if phone:
      for number in phone:
        
        digits = 0
        for ch in number:
            if ch.isdigit():
                digits=digits+1
            else :
                digits = digits
        
        if  digits < 16:
            numbers.append(number)
        
      for number in numbers:
        return number

    return None



email_regex = re.compile(r'[\w._-]+@[\w-]+\.[\w.-]+')

def extract_email_address(cv_text):
    emails = re.findall(email_regex, cv_text)
    
    for email in emails:
      return email

print('check 4')

print(extract_phone_number(text))
print(extract_email_address(text))

#displacy.serve(doc, style="ent")

# trying to build bounding box i.e. annot
page1 = pages[0]
words = page1.get_text("words")

#print(words)

first_annots=[]

rec=page1.rect

print(rec)
print('check 5')

#function to extract info contained in the box, sort the words and return in form of a string : 

def make_text(words):

    line_dict = {} 

    words.sort(key=lambda w: w[0])

    for w in words:  

        y1 = round(w[3], 1)  

        word = w[4] 

        line = line_dict.get(y1, [])  

        line.append(word)  

        line_dict[y1] = line  

    lines = list(line_dict.items())

    lines.sort()  

    return "n".join([" ".join(line[1]) for line in lines])

#Information of words in first object is stored in mywords

mywords = [w for w in words if fitz.Rect(w[:4]) in rec]

ann= make_text(mywords)

first_annots.append(ann)

########################################
with open('textfile.txt', 'a+') as f:
  f.write(text)