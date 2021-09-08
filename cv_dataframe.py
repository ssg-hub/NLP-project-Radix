from functions import pdf_to_text
import os, sys
import pandas as pd
from functions import pdf_to_text
from extract import extract_languages
pd.set_option('display.max_columns',10)

#creating an empty dataframe
df = pd.DataFrame(columns=['Pdf','Name','Phone','Email',\
                    'Date_Of_Birth','Hobbies','Languages','Skills',\
                    'Education','Experience','Previous_Job_Title'])
print(df.head())

for i in range(1,11):

    #calling the pdfs
    pdf = 'assets/'+str(i)+'.pdf'

    # populating names of pdf
    df.at[i, 'Pdf']  = pdf 

    # extracting text from pdf
    doc, text = pdf_to_text(text)

    # populating languages
    languages = extract_languages(text)
    df.at[i, 'Skills']  = skills 




    

