import string
from functions import preprocess, pdf_to_text

def tokensNameExtr(pdf):

    # pages is full document from pdf and text is text fromm all pages of pdf
    pages, text = pdf_to_text(pdf)

    #preprocess to tokenize and add pos
    a = preprocess(text)

    #keeping only the tokens that are personal singular nouns
    nnp_list = []
    for token, tag in a:
        if tag == "NNP" and token not in string.punctuation:
            nnp_list.append(token)

    #choosing only first tokens to extract name
    #as in >95% times it should be there.
    tags_for_name = nnp_list[:8] 
    return tags_for_name
