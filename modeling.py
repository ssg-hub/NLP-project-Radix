'''
Created on Sep 9, 2021

@author: Shilpa Singhal
'''
from fuzzywuzzy import fuzz
from pandas.core.frame import DataFrame
from typing import List
import pandas as pd
import pickle
# https://www.geeksforgeeks.org/fuzzywuzzy-python-library/

def similarity_on_languages(df: DataFrame,\
                     match_for : str, threshold : int) -> List:
    """
    Function to return a list of CVs that match with the required language.
    This match is decided using the W-Ration of python fuzzywuzzy library,
    which uses Levenshtein Distance to calculate the differences
    between sequences.

    df : is the dataframe from which matching CVs will be found out.
    match for : is the keywords on which the match is sought
                here, the keywords from one cv can be pasted and hence we can 
                find other cvs that match the selected one.
    threshold : is the minimum w-ratio to have for the
                cv to be considered a good match and hence
                included in the final list.
    """
    # putting all vales from list column of given data frame to a 
    # list for quicker and faster processing
    language_col = df['Languages'].tolist()
    #creating an empty list to populate the results in the end.
    lang_i_list = []
    # knowing the choice of view from the user
    user_input = input("Do you want to see the detailed results, Yes/No?" )
    print('')
    print('W-Ratio | ', "Index in dataframe | ", "Languages of that person")

    # going over language for each resume one by one from list above
    for i, x in enumerate(language_col):
        # finding w ratio for each cv 
        wratio_lang = fuzz.WRatio(match_for, x)
        # adding to list only if meeting threshold specified
        if wratio_lang >= threshold:
            lang_i_list.append(str(i+1)+'.pdf')
            # printing this result only if the user has said 'yes' above
            if user_input.lower() == 'yes':  
                print(wratio_lang," | ", i," | ", x)
    print("\n","These CVs match the required languages")
    return lang_i_list #returning a list of names of CVs that are a good match


def similarity_on_skills(df: DataFrame, match_for : str,\
                         threshold : int) -> List:
    """
    Function to return a list of CVs that match with the required skills.
    """
    #all other comments similar to similarity_on_languages() function above.
    skills_col = df['Skills'].tolist()
    skills_i_list = []
    user_input = input("Do you want to see the detailed results, Yes/No?" )
    print('')
    print('W-Ratio | ', "Index in dataframe | ", "Skills of that person")
    for i, x in enumerate(skills_col):
        wratio_skills = fuzz.WRatio(match_for, x)
        if wratio_skills >= threshold:
            skills_i_list.append(str(i+1)+'.pdf')
            if user_input.lower() == 'yes':  
                print(wratio_skills," | ", i," | ", x)
    print("\n","These CVs match the required skills")
    return skills_i_list        

def similarity_on_desig(df: DataFrame, match_for : str,\
                         threshold : int) -> List:
    """
    Function to return a list of CVs that match with the required Previous Job Title.
    """
    #all other comments similar to similarity_on_languages() function above.
    desig_col = df['Previous_Job_Title'].tolist()
    desig_i_list = []
    user_input = input("Do you want to see the detailed results, Yes/No?" )
    print('')
    print('W-Ratio | ', "Index in dataframe | ", "Previous Job Title of that person")
    for i, x in enumerate(desig_col):
        wratio_desig = fuzz.WRatio(match_for, x)
        if wratio_desig >= threshold:
            desig_i_list.append(str(i+1)+'.pdf')
            if user_input.lower() == 'yes':  
                print(wratio_desig," | ", i," | ", x)
    print("\n","These CVs match the required previous job title")
    return desig_i_list

def similarity_on_edu(df: DataFrame, match_for : str,\
                         threshold : int) -> List:
    """
    Function to return a list of CVs that match with the required education.
    """
    #all other comments similar to similarity_on_languages() function above.
    edu_col = df['Education'].tolist()
    edu_i_list = []
    user_input = input("Do you want to see the detailed results, Yes/No?" )
    print('')
    print('W-Ratio | ', "Index in dataframe | ", "Education of that person")
    for i, x in enumerate(edu_col):
        wratio_edu = fuzz.WRatio(match_for, x)
        if wratio_edu >= threshold:
            edu_i_list.append(str(i+1)+'.pdf')
            if user_input.lower() == 'yes':  
                print(wratio_edu," | ", i," | ", x)
    print("\n","These CVs match the required education")
    return edu_i_list


name = 'assets/df_file.pkl'
output_df = pd.read_pickle(name)
print(similarity_on_skills(output_df, 'Excel', 30))