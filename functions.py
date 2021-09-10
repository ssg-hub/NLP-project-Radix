'''
Created on Sep 8, 2021

@author: Shilpa Singhal
'''

import nltk
import fitz
import re
import string
import itertools
from typing import List
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
#nltk.download('maxent_ne_chunker')
from phone_email_extraction import extract_dob

# function 1
# convert all pages of pdf to text
def pdf_to_text(pdf_name : str) ->  str:
    """
    Function to get all the pages of given pdf in text format.
    Returns 2 parameters.
    """
    doc = fitz.open(pdf_name)
    full_text = ''
    for page in doc:
        text = page.getText("text")#.encode("utf8") 
        full_text = full_text + ' ' + text
    return doc, full_text

# function 2
def preprocess(text : str ):
    """
    Function to tokenize and add part of speech tags
    """
    preprocessed_text = nltk.word_tokenize(text)
    preprocessed_text = nltk.pos_tag(preprocessed_text)

    return preprocessed_text

# function 3
def named_entities(tagged):
    try:
        for i in tagged[:20]:
            #words = nltk.word_tokenize(i)
            #tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=False)
            namedEnt.draw()
    except Exception as e:
        print(str(e))

# function 4
def mark_word(page, text):
    """
    Underline each word that contains 'text'.
    """
    
    wlist = page.getText("words")  # make the word list
    for w in wlist:  # scan through all words on page
        if text in w[4]:  # w[4] is the word's string
            
            r = fitz.Rect(w[:4])  # make rect from word bbox
            highlight = page.addHighlightAnnot(r)
            highlight.setColors({"stroke":(0, 0, 1), "fill":(0.75, 0.8, 0.95)})
            highlight.update()  # underline
    return 

# function 5
def extract_lines_tokenized(text : str) -> List:
    """
    Function to tokenize the text into lines containing tokens.
    Returns 2 parameters.
    """
    #breaking text into sentences
    lines = [each.strip() for each in text.split("\n") if len(each) > 0] 

    #tokenizing each sentence
    lines_tokenized = [nltk.word_tokenize(each) for each in lines  ]

    #adding part of speech for each token
    lines_pos_tagged = [nltk.pos_tag(each) for each in lines_tokenized]
 
    return lines_tokenized, lines_pos_tagged
    
# function 6
def remove_noise(each_line, stop_words = ()):
    """
    Function to remove stop words and punctuation
    Works on token of one line.
    """
    cleaned_line = []
     
    for token, tag in nltk.pos_tag(each_line):


        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith("VB"):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)
        # removing '\uf0b7' characters like bullet points
        token = re.sub(r'[^\x00-\x7F]+(\s)*', '', token)
        if len(token) > 0 and token not in string.punctuation \
             and token.lower() not in stop_words: 
            cleaned_line.append(token.lower())
            
    return cleaned_line


# function 7
def extract_lines_without_noise(lines_tokenized : List) -> List:
    """
    Function to clean the remove noise from each line( a list of tokens)
    from the corpus, which is  list of lines.
    Works on corpus ie list of lines and remove_noise() works on a single line.
    """
    lines_without_noise = []

    # let us remove stop words first
    stop_words = stopwords.words('english')

    for i,each in enumerate(lines_tokenized):   
        x = remove_noise(each, stop_words)
        if len(x) > 0 : lines_without_noise.append(x)

    return lines_without_noise

# function 8
def extract_few(lines_without_noise: List):
    """
    Function to get the languages
                        date of birth
                        experience
                        address
                        hobbies
                        education
    Returns 6 parameters.
    
    Here we go through the corpus of noiseless lines (tokenized, \
    lemmatized, lower case, stop words, utf characters and punctuation removed)
    
    And then whenever the keyword like 'Languages' or 'Education' is found,
    We consider that as a new section. 
    
    We get the information from the following lines in this section and
    add it to a list
    """

    stop_words = stopwords.words('english')

    lang = []
    dob = []
    experience = []
    address = []
    hobbies = []
    education = []

    # length of corpus will be needed for comparison
    l = len(lines_without_noise)

    for i,x in enumerate(lines_without_noise):

        if 'language' in x or 'languages' in x or 'mlanguages' in x:
            # in some cases it would written in same line, then:
            if 'english' in x or 'french' in x or 'dutch' in x or 'nederlands' in x:            
                lang.append(remove_noise(lines_without_noise[i], stop_words))
            # when languages are written in the next line:
            elif i != l-1:
                lang.append(remove_noise(lines_without_noise[i+1], stop_words))
               
        
        if 'dob' in x or 'birth' in x:
            #print("Date of Birth:")
            somedate = (remove_noise(lines_without_noise[i], stop_words))
            somedate = extract_dob(somedate)
            if len(somedate) != 0: 
                dob.append(somedate)   
            elif i != l-1:
                somedate = (remove_noise(lines_without_noise[i+1], stop_words))
                somedate = extract_dob(somedate)
                dob.append(somedate) 
       
                
        if ('experience' in x or 'past' in x) and (l > i+1):
            experience.append(remove_noise(lines_without_noise[i+1], stop_words))
        

        if 'address' in x or 'permanentaddress' in x\
            or 'localaddress' in x \
            or 'homeaddress' in x\
            or 'postaladdress' in x:
            three = ''
            two = ''
            one = ''
            if l > i+1:
                one = (' '.join(remove_noise(lines_without_noise[i+1], stop_words)))
                if l > i+2:
                    two = (' '.join(remove_noise(lines_without_noise[i+2], stop_words)))
                    if l > i+3:
                        three = (' '.join(remove_noise(lines_without_noise[i+3], stop_words)), "\n")
            address.extend((one, two, three))
        

        hobby_list = ['hobby','hobbies','interests', 'extra-curricular',
                        'extracurriculum','extracurricular', 'extra- ',
                        'extra', 'sports','curricular','activities']
        hl = list(set(hobby_list).intersection(x))
        if (len(hl) != 0) and (l > i+1):
            hobbies.append(remove_noise(lines_without_noise[i+1]))
       

        edu_list = ['education','qualification','qualifications','certification',
                    'certifications']
        el = list(set(edu_list).intersection(x))
        if len(el) != 0:
            j = 1
            while (j < 5) and (l > i+j):
                place_holder = (remove_noise(lines_without_noise[i+j], stop_words) )
                education.append(place_holder)
                j += 1
        
    #unpacking list of lists
    lang = list(itertools.chain(*lang))
    lang = ' '.join(lang)
    hobbies = list(itertools.chain(*hobbies))
    dob = list(itertools.chain(*dob))

    return  lang, dob, experience, address, education, hobbies