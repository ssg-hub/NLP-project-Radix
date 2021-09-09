'''pip install nltk
pip install spacy==2.3.5
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
pip install pyresparser'''
import os
import pandas as pd
import PyPDF2
import en_core_web_sm
nlp = en_core_web_sm.load()
import nltk


from pyresparser import ResumeParser

def extract_skills(pdf):
    """
    Function to get the skills of the person
    """
    skills = []
    everything = ResumeParser(pdf).get_extracted_data()
    skills = everything['skills']
    return skills
    

def extract_designation(pdf):
    """
    Function to get the skills of the person
    """
    designation = []
    everything = ResumeParser(pdf).get_extracted_data()
    designation = everything['designation']
    if designation is not None: return designation[0]
    else :  return designation

'''
def extract_education(tokens_with_pos):
    """
    Function to get the education of person out of given text
    """
    education_words = [
    #'school',
    #'university',
    'certificate',
    #'study',
    'diploma',
    #'hsc',
    #'ssc',
    #'college',
    #'higher',
    #'institute',
    #'studies',
    #'education',
   # 'high',
   # 'master',
    #'bachelor',
    #'academy',
    #'polytechnic',
    #'degree',
    'masters',
    'bachelors',
    'p.h.d',
    'b.e',
    'b.e.',
    'm.e.'
    'engineering'
    ]

    edu_institutes = []
    for each, tag in tokens_with_pos:
        if each.lower() in education_words:
            edu_institutes.append(each)

  

    return edu_institutes
'''    