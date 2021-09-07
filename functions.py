import nltk
import fitz
nltk.download('maxent_ne_chunker')

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