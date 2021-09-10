from typing import List
import nltk
import fitz
import re
import string
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('maxent_ne_chunker')
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download('wordnet')

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

def lines_without_noise(lines_tokenized : List) -> List:
    lines_without_noise = []

    # let us remove stop words first
    stop_words = stopwords.words('english')

    #print(remove_noise(lines_pos_tagged, stop_words))
    for i, each in enumerate(lines_tokenized):   
        x = remove_noise(each, stop_words)
        # print(x)
        if len(x) > 0 : lines_without_noise.append(x)

    return lines_without_noise