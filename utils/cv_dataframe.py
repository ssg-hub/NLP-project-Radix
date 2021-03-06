'''
Created on Sep 8, 2021
@author: Shilpa Singhal
@additions: Pauwel De Wilde
'''
from functions import pdf_to_text
import pandas as pd
from nltk.corpus import stopwords
from functions import pdf_to_text, extract_lines_tokenized
from functions import extract_lines_without_noise, extract_few
from phone_email_extraction import extract_email_address, extract_phone_number
from skills_extraction import extract_skills, extract_designation
from name_API import get_name

pd.set_option('display.max_columns',15)

#creating an empty dataframe
df = pd.DataFrame(columns=['Pdf','Name','Phone','Email',\
                    'Date_Of_Birth','Hobbies','Languages','Skills',\
                    'Education','Experience','Previous_Job_Title'])


# each cv is a row of the dataframe
# populating columns for each of the cv
for i in range(1, 251):

    # calling the pdfs
    pdf = 'assets/pdf/'+str(i)+'.pdf'

    # populating names
    df.at[i-1, 'Name'] = get_name(pdf)

    # converting pdf to document and text using PyMuPDF
    pages, text = pdf_to_text(pdf)

    # tokenize and pos tag the lines
    lines_tokenized, lines_pos_tagged = extract_lines_tokenized(text)

    # remove stopwords, bullets, punctuations and lowercase the tokenized lines
    lines_noiseless = extract_lines_without_noise(lines_tokenized)
    
    # getting these fields with a function from cleaned lines
    # language, date of birth, experience, address, education, hobbies
    lang, dob, experience, address, education, hobbies =  extract_few(lines_noiseless)           
    
    # Now filling the details in data the empty daataframe we created
    # populating names of pdf
    df.at[i-1, 'Pdf']  = pdf 

    # populating phone
    df.at[i-1, 'Phone']  = str(extract_phone_number(text)) 

    # populating email
    df.at[i-1, 'Email']  = str(extract_email_address(text)) 

    # populating languages
    df.at[i-1, 'Languages']  = str(lang)

    # populating date of birth
    df.at[i-1, 'Date_Of_Birth']  = str(dob)

    # populating hobbies
    df.at[i-1, 'Hobbies']  = str(hobbies)

    # populating address
    df.at[i-1, 'Address']  = str(address)    

    # populating education
    df.at[i-1, 'Education']  = str(education)

    # populating experience
    df.at[i-1, 'Experience']  = str(experience) 

    # populating skills
    df.at[i-1, 'Skills']  = extract_skills(pdf)

    # populating designation
    df.at[i-1, 'Previous_Job_Title']  = extract_designation(pdf)

# save everything into pickle dataframes
df.to_pickle("assets/df_file_250pdfs.pkl")
df_pers = df[["Pdf", "Name", "Phone", "Email", "Date_Of_Birth","Hobbies", "Languages"]]
df_prof = df[["Pdf", "Name", "Skills", "Education", "Experience", "Previous_Job_Title"]]

df_pers.to_pickle("assets/df_personal.pkl")
df_prof.to_pickle("assets/df_professional.pkl")