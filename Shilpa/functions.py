import nltk
import fitz

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