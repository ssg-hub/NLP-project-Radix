from fitz.utils import Shape
from numpy import concatenate
from tabulate import tabulate
import pandas as pd
import fitz
import nltk
import PyPDF2
import spacy
from spacy.lang.en import English
from spacy import displacy
from phone_email_extraction import extract_phone_number, extract_dob
from phone_email_extraction import extract_email_address, extract_email_address_2
from eduction_extraction import extract_education
from nltk.corpus import stopwords

import string
from functions import preprocess, named_entities, pdf_to_text, mark_word
from functions import extract_lines_tokenized, remove_noise, lines_without_noise
import re
pd.set_option('display.max_columns',10)


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

#pdf name 
pdf = '/home/becode/Documents/Projects/9.RadixNLP/curriculum_vitae_data-master/pdf/1526.pdf'

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
#print(label_groups.head())

# Let's print the first entries in all the groups formed.
label_groups_first = label_groups.first()
#print(label_groups_first)

# list of all unique token labels
labels_list = list(label_groups_first.index.values)

# to check how many times an entity group is found in the text
#unuseful results yielded
#for item in labels_list:
    # Finding the values contained in the token group
    #print(item, len(label_groups.get_group(item)))

# load text using nlp
doc = nlp(text)

# visual rep of entity groups found using spacy
#displacy.serve(doc, style = 'ent')
####################################################################
#trying to see if languages are marked corrctly
ds = data.loc[data['token_label'] == 'DATE'].groupby('token_label')
#not getting all languages, DOB etc
#they are not, by observation, bad results yielded


'''for token in doc:
    print(token, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)'''

print('check 3')

# let us remove stop words first
stop_words = stopwords.words('english')

# not needed currently
text_tokenized = nltk.word_tokenize(text)
text_cleaned = []
for token in text_tokenized:
    if token.lower() not in stop_words: # '''token not in string.punctuation and''' 
        text_cleaned.append(token)

# joining back after removing stop words
text_cleaned_joined = ' '.join(text_cleaned)

# trying other method using nltk instead of spacy for pos tags
# we are here using the original text generated by the pdf

lines_tokenized, lines_pos_tagged = extract_lines_tokenized(text)

lines_without_noise = lines_without_noise(lines_tokenized)


 #print(len(lines_without_noise), len(lines_pos_tagged))

for i,x in enumerate(lines_without_noise):

    if 'languages' in x or 'languages' in x:
        lang = (remove_noise(lines_without_noise[i+1], stop_words))
        # in some cases it would written in same line, then:
        # (remove_noise(lines_tokenized[i], stop_words))
        print ('Languages:', "\n", lang, '\n')

    if 'dob' in x or 'birth' in x:
        print("Date of Birth:")
        dob = (remove_noise(lines_without_noise[i], stop_words))
        dob = extract_dob(dob)
        if len(dob) != 0: 
            print(dob)    
        else:
            dob = (remove_noise(lines_without_noise[i+1], stop_words))
            dob = extract_dob(dob)
            print(dob)
            
    if 'experience' in x or 'past' in x:
        print("Experience:")
        #print(remove_noise(x, stop_words))
        print(remove_noise(lines_without_noise[i+1], stop_words), '\n')
        

    if 'address' in x:
        print("Address:")
        #print(remove_noise(x, stop_words))
        print(' '.join(remove_noise(lines_without_noise[i+1], stop_words)))
        print(' '.join(remove_noise(lines_without_noise[i+2], stop_words)))
        print(' '.join(remove_noise(lines_without_noise[i+3], stop_words)), "\n")

    hobby_list = ['hobby','hobbies','interests', 'extra-curricular',
                    'extracurriculum','extracurricular', 'extra- ',
                    'extra', 'sports','curricular','activities']
    hl = list(set(hobby_list).intersection(x))
    #if set(x) in hobby_list
    if len(hl) != 0:
        print(hl[0],":")            
        #print(hl, i, i+1)
        #print(remove_noise(x, stop_words))
        print(remove_noise(lines_without_noise[i+1], stop_words))

    edu_list = ['education','qualification','qualifications','certification',
                'certifications']
    el = list(set(edu_list).intersection(x))
    if len(el) != 0:
        print(el[0],":")
        j = 1
        while j < 7:
            print(remove_noise(lines_without_noise[i+j], stop_words) )
            j += 1
        

print('check 4')
for each in lines_without_noise:
    print(each)
print('check 5')

###################################################################
# trying to build bounding box i.e. annot
# pages is the resulting text when we open pdf using fitz/PyMuPDF
page1 = pages[0]
words = page1.get_text("words") # words on only page1

# getting the bounding boxes for page1
#first_annots=[] #empty list to store results

#rec=words#.first_annot.rect
#print(rec)
# create DataFrame using data
df_words = pd.DataFrame(words, columns =['A','B','C','D', 'Word', 'BlockNo','LineNo','WordNo'])
df_words_groupby_block = df_words.groupby('BlockNo')
  
for x in df_words_groupby_block.groups:
    print('Block '+ str(x))
    print(df_words_groupby_block.get_group(x))
print('check 6')

# draw polyline
# create a Shape to draw on
# get list of text locations
t = 'Education:'
doc, text = pdf_to_text(pdf)
# we use "quads", not rectangles because text may be tilted!
rl = page1.search_for(t, quads = True)
# mark all found quads with one annotation
page1.add_highlight_annot(rl)
# save to a new PDF
doc.save("quiggly.pdf")

mark_word(page1, t)
doc.save("a-squiggly.pdf")
#shape = page1.new_shape()
#shape.draw_quad(108.099998 , 324.977936 , 114.685936 , 339.524811)


'''
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
page1 = pages[0]
blocks = page1.get_text("blocks") # blcoks on only page1 
#or lines = page1.get_text.extractBLOCKS()

# create DataFrame using data
df_blocks = pd.DataFrame(blocks, columns =['A','B','C','D', 'Word', 'BlockNo','BlockType'])
df_blocks_groupby_block = df_blocks.groupby('BlockNo')
  
for x in df_blocks_groupby_block.groups:
    print('Block '+ str(x))
    print(df_blocks_groupby_block.get_group(x))
print('check 7')
shape = page1.new_shape()
for b in blocks[:10]:
    r = fitz.Rect(b[:4])
    shape.draw_rect(r)
    doc.save("a-squiggly.pdf")
###########################
'''shape = page1.new_shape()
#shape.draw_quad((108.099998 , 324.977936)(114.685936 , 339.524811))
#quad = fitz.Quad( 209.100006,  439.669434  ,584.948486 , 743.95105)
#
areas = page1.searchFor("@", hit_max = 3)
shape.draw_rect(areas)
doc.save("a-squiggly.pdf")
print(areas)
print('check 8')'''
###########################
page1 = pages[0]
j_son = page1.get_text("dict")
for annot in page1.annots():
    print(annot)

######################
