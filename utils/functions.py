from typing import List
import nltk
import fitz
import re
import string
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from phone_email_extraction import extract_dob
import itertools

# convert all pages of pdf to text
def pdf_to_text(pdf_name : str) ->  str:
    """
    Function to get all the pages of given pdf in text format.
    """
    doc = fitz.open(pdf_name)
    full_text = ''
    for page in doc:
        text = page.getText("text")#.encode("utf8") 
        full_text = full_text + ' ' + text
    return doc, full_text

def preprocess(text : str ):
    """
    Function to tokenize and add part of speech tags
    """
    preprocessed_text = nltk.word_tokenize(text)
    preprocessed_text = nltk.pos_tag(preprocessed_text)

    return preprocessed_text

def named_entities(tagged):
    try:
        for i in tagged[:20]:
            #words = nltk.word_tokenize(i)
            #tagged = nltk.pos_tag(words)
            namedEnt = nltk.ne_chunk(tagged, binary=False)
            namedEnt.draw()
    except Exception as e:
        print(str(e))

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

def extract_lines_tokenized(text : str) -> List:
    """
    Function to tokenize the text into lines containing tokens.
    """
    #breaking text into sentences
    lines = [each.strip() for each in text.split("\n") if len(each) > 0] 

    #tokenizing each sentence
    lines_tokenized = [nltk.word_tokenize(each) for each in lines  ]

    #adding part of speech for each token
    lines_pos_tagged = [nltk.pos_tag(each) for each in lines_tokenized]
 
    return lines_tokenized, lines_pos_tagged

def remove_noise(each_line, stop_words = ()):
    """
    Function to remove stop words and punctuation
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

def extract_lines_without_noise(lines_tokenized : List) -> List:
    lines_without_noise = []

    # let us remove stop words first
    stop_words = stopwords.words('english')

    #print(remove_noise(lines_pos_tagged, stop_words))
    for i,each in enumerate(lines_tokenized):   
        x = remove_noise(each, stop_words)
        #print(x)
        if len(x) > 0 : lines_without_noise.append(x)

    return lines_without_noise


def extract_few(lines_without_noise):

    stop_words = stopwords.words('english')

    lang = []
    dob = []
    experience = []
    address = []
    hobbies = []
    education = []

    for i,x in enumerate(lines_without_noise):

        
        if 'language' in x or 'languages' in x or 'mlanguages' in x:
            # in some cases it would written in same line, then:
            if 'english' in x or 'french' in x:            
                lang.append(remove_noise(lines_without_noise[i], stop_words))
            # when languages are written in the next line:
            else:
                lang.append(remove_noise(lines_without_noise[i+1], stop_words))
        # else: 
        #     lang = 'n/a'
        
        
        if 'dob' in x or 'birth' in x:
            #print("Date of Birth:")
            somedate = (remove_noise(lines_without_noise[i], stop_words))
            somedate = extract_dob(somedate)
            if len(somedate) != 0: 
                #print(dob) 
                dob.append(somedate)   
            else:
                somedate = (remove_noise(lines_without_noise[i+1], stop_words))
                somedate = extract_dob(somedate)
                dob.append(somedate) 
                #print(dob)
        
                
        if 'experience' in x or 'past' in x:
            #print("Experience:")
            #print(remove_noise(x, stop_words))
            experience.append(remove_noise(lines_without_noise[i+1], stop_words))
            #print(experience, '\n')
        
        #token = re.sub(r'[^\x00-\x7F]+(\s)*', '', token) 
        #token = re.sub(r'[.*a*d*r*e*s*., '', token)
        if 'address' in x or 'permanentaddress' in x\
            or 'localaddress' in x \
            or 'homeaddress' in x\
            or 'postaladdress' in x:
            #print("Address:")
            #print(remove_noise(x, stop_words))
            one = (' '.join(remove_noise(lines_without_noise[i+1], stop_words)))
            '''if len(lines_without_noise) >= i+2:
                two = (' '.join(remove_noise(lines_without_noise[i+2], stop_words)))
            else : two = ''
            if len(lines_without_noise) >= i+3:
                    three = (' '.join(remove_noise(lines_without_noise[i+3], stop_words)), "\n")
            else : three = '''''
            address.append((one))
            #print(one, "\n", two, "\n", three)
        

        hobby_list = ['hobby','hobbies','interests', 'extra-curricular',
                        'extracurriculum','extracurricular', 'extra- ',
                        'extra', 'sports','curricular','activities']
        hl = list(set(hobby_list).intersection(x))
        #if set(x) in hobby_list
        if len(hl) != 0:
            #print(hl[0],":")            
            #print(hl, i, i+1)
            #print(remove_noise(x, stop_words))
            hobbies.append(remove_noise(lines_without_noise[i+1]))
            #print(hobbies)
        
            

        edu_list = ['education','qualification','qualifications','certification',
                    'certifications']
        
        el = list(set(edu_list).intersection(x))
        if len(el) != 0:
            #print(el[0],":")
            j = 1
            while j < 7:
                place_holder = (remove_noise(lines_without_noise[i+j], stop_words) )
                education.append(place_holder)
                j += 1
        
    
    lang = list(itertools.chain(*lang))
    lang = ' '.join(lang)
    hobbies = list(itertools.chain(*hobbies))
    dob = list(itertools.chain(*dob))
    return  lang, dob, experience, address, education, hobbies