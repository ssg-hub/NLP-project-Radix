import nltk
nltk.download('maxent_ne_chunker')

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