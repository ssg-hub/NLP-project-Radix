from numpy import concatenate
import pandas as pd
import fitz
import nltk
import PyPDF2
import spacy
from spacy.lang.en import English
from spacy import displacy
import re
from regex_extraction import extract_phone_number
from regex_extraction import extract_email_address
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
import string

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

# convert all pages of pdf to text
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

#pdf name 
pdf = '/home/becode/Documents/Projects/9.RadixNLP/curriculum_vitae_data-master/pdf/3264.pdf'

#create the nlp object
nlp = spacy.load('en_core_web_lg')

print('check 1')

# convert text to dataframe with token and labels
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

print('check 2')

# grouping by token_label
label_groups = data.groupby('token_label')
print(label_groups.head())

# Let's print the first entries in all the groups formed.
label_groups_first = label_groups.first()
#print(label_groups_first)

# list of all unique token labels
labels_list = list(label_groups_first.index.values)

# to check how many times an entity group is found in the text
for item in labels_list:
    # Finding the values contained in the token group
    print(item, len(label_groups.get_group(item)))

# load text using nlp
doc = nlp(text)

# visual rep of entity groups found using spacy
#displacy.serve(doc, style = 'ent')
####################################################################
#trying to see if languages are marked corrctly
ds = data.loc[data['token_label'] == 'LANGUAGE'].groupby('token_label')
print(ds.head())
#they are not, by observation


'''for token in doc:
    print(token, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)'''

print('check 3')

# let us remove stop words first
stop_words = stopwords.words('english')

#let us remove all punctuation from text 
text_tokenized = nltk.word_tokenize(text)
text_cleaned = []
for token in text_tokenized:
    if token.lower() not in stop_words: # '''token not in string.punctuation and''' 
        text_cleaned.append(token)

print(text_cleaned)
text_cleaned_joined = ' '.join(text_cleaned)

#trying other method using nltk instead of spacy for pos tags
lines = [each.strip() for each in text_cleaned_joined.split("\n") if len(each) > 0]
lines_tokenized = [nltk.word_tokenize(each) for each in lines]
lines_pos_tagged = [nltk.pos_tag(each) for each in lines_tokenized]


def remove_noise(tokens, stop_words = ()):

    cleaned_lines = []
     
    for token, tag in nltk.pos_tag(tokens):


        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith("VB"):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation \
             and token.lower() not in stop_words:
            cleaned_lines.append(token)
            
    return cleaned_lines

#print(remove_noise(line, stop_words))



print('check 4')
# print extracted phone number and email addresses
print(extract_phone_number(text))
print(extract_email_address(text))


# trying to build bounding box i.e. annot
# pages is the resulting text when we open pdf using fitz/PyMuPDF
page1 = pages[0]
words = page1.get_text("words") # words on only page1

'''# getting the bounding boxes for page1
first_annots=[] #empty list to store results

rec=page1.first_annot.rect
print(rec)
print('check 5')

#Information of words in first object is stored in mywords
mywords = [w for w in words if fitz.Rect(w[:4]) in rec]

#not my code
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

ann= make_text(mywords)
first_annots.append(ann)
# not my code - end'''
########################################
