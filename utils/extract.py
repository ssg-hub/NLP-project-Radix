import pandas as pd
import fitz
import spacy
import en_core_web_sm

def pdf_to_text(pdf_name : str) ->  str:
    """
    Function to get all the pages of given pdf in text format.
    """
    doc = fitz.open(pdf_name)
    full_text = ''
    for page in doc:
        text = page.getText("text")
        full_text = full_text + ' ' + text
    return full_text

pdf = '/Users/paww/Documents/GitHub/NLP-project-Radix/assets/pdf/156.pdf'

#create the nlp object
nlp = en_core_web_sm.load()

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

text = pdf_to_text(pdf)
data = text_to_df(text)

print(data.head(20))

# grouping by token_label
label_groups = data.groupby('token_label')

# Let's print the first entries in all the groups formed.
label_groups_first = label_groups.first()
print(label_groups_first)

# list of all unique token labels
labels_list = list(label_groups_first.index.values)

for item in labels_list:
    # Finding the values contained in the token group
    print(item, len(label_groups.get_group(item)))