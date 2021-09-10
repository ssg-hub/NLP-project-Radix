'''
Created on Sep 8, 2021

@author: Shilpa Singhal
'''
from fuzzywuzzy import process, fuzz
from pandas.core.frame import DataFrame
from typing import List
# https://www.geeksforgeeks.org/fuzzywuzzy-python-library/

def similarity_on_languages(df: DataFrame, match_for  = 'english') -> List:

    language_col = df['Languages'].tolist()
    lang_i_list = []
    for i, x in enumerate(language_col):
        wratio_lang = fuzz.WRatio(match_for, x)
        if wratio_lang >= 70 : lang_i_list.append(i+1)
        return lang_i_list


def similarity_on_skills(df: DataFrame, match_for  = 'c') -> List:
    skills_col = df['Skills'].tolist()
    skills_i_list = []
    for i, x in enumerate(skills_col):
        wratio_skills = fuzz.WRatio(match_for, x)
        print(wratio_skills, i, x)
        if wratio_skills >= 70 : skills_i_list.append(str(i+1)+'.pdf')
    return skills_i_list
        

def similarity_on_desig(df: DataFrame, match_for  = 'manager') -> List:
    desig_col = df['Previous_Job_Title'].tolist()
    desig_i_list = []
    for i, x in enumerate(desig_col):
        wratio_desig = fuzz.WRatio(match_for, x)
        if wratio_desig >= 70 : desig_i_list.append(i+1)
    return desig_i_list

def similarity_on_edu(df: DataFrame, match_for  = 'degree') -> List:
    edu_col = df['Education'].tolist()
    edu_i_list = []
    for i, x in enumerate(edu_col):
        wratio_edu = fuzz.WRatio(match_for, x)
        if wratio_edu >= 70 : edu_i_list.append(i+1)
    return edu_i_list


data = 'assets/df_file.pkl'
#print(similarity_on_skills(data))