from numpy import concatenate
import pandas as pd
import fitz
import PyPDF2
import spacy
from spacy.lang.en import English

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

pdf = '/home/becode/Documents/Projects/9.RadixNLP/curriculum_vitae_data-master/pdf/3260.pdf'


#create the nlp object
nlp = spacy.load('en_core_web_sm')


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

print(data.head())

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