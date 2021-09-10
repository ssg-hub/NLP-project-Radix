'''
Created on Sep 8, 2021

@author: Shilpa Singhal
'''
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

from pyresparser import ResumeParser #pyreparser is a library

def extract_skills(pdf):
    """
    Function to get the skills of the person
    """
    skills = [] #to populate the results
    # gets everything from a person's cv 
    everything = ResumeParser(pdf).get_extracted_data()
    # we are using skills only here
    skills = everything['skills']
    skills = ' '.join(skills)
    return skills
    

def extract_designation(pdf):
    """
    Function to get the designation/previous job title of the person
    """
    designation = [] #to populate the results
    # gets everything from a person's cv
    everything = ResumeParser(pdf).get_extracted_data()
    # we are using only designation here
    designation = everything['designation']
    if designation is not None: return designation[0]
    else :  return designation
