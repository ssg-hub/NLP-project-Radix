'''
Created on Sep 4, 2021

@author: Shilpa Singhal
'''
import re

# function 1
def extract_phone_number(cv_text):
    """
    Function to use the regex to extract phone number from text
    """
    # using regex to extract phone
    phone_regex = re.compile(r'[\+\(]*[1-9][0-9.\-\(\)]{8,}[0-9\)]')

    # matching all using regex
    phones = re.findall(phone_regex, cv_text)
    
    # adding to list of phone numbers only if number of digits 
    # is less than 16 as per international standards
    phone_numbers = [] #empty list to store all phone_numbers
    if phones:
        for number in phones:
        
            digits = 0
            for ch in number:
                if ch.isdigit():
                    digits=digits+1
                else :
                    digits = digits
            
            if  7 < digits < 16:
                phone_numbers.append(number)
        
        # if more than one email found return as a list
        if len(phone_numbers) > 1: return phone_numbers[:2]
        else : return phone_numbers[0]

    # return none if no numbers found as per regex rule
    return None


# function 2
def extract_email_address(cv_text : str):
    """
    Function to extract emails using regex
    """
    #using regex to extract email address
    email_regex = re.compile(r'[\w._-]+@[\w-]+\.[\w.-]+')

    # matching all using regex
    emails = re.findall(email_regex, cv_text)
    
    # check if matches are found
    if emails :
        # if more than one email found return as a list
        if len(emails) > 1: return emails[0]
        else : return emails[0]

    # return none if no numbers found as per regex rule
    return None

# function 3 - not using in final script
def extract_email_address_2(doc):
    """
    Function to retrive emails using inbuilt function from spacy
    """
    email_list = []

    for token in doc:
        if token.like_email == True: 
            email_list.append(token)
    x = list(set(email_list))
    return x
    
# function 4
def extract_dob(a_list):
    """
    Function to extract date of birth from given text using regex
    """
    # pattern for  mm/dd/yy, mm/dd/yyyy, dd/mm/yy, and dd/mm/yyyy, allowing leading zeros to be omitted
    # and not acconting for Feb 30th or 31st
    #pattern = r'^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d'
    #pattern = r'(\d{1,4}([.\-/])\d{1,2}([.\-/])\d{1,4})'
    #pattern = r'^[1-2][0-9]|[0][1-9]|[3][01][- /.]([0]?[1-9]|[1][012])[- /.]((19|20)\d\d)$'
    pattern = r'^[0-3]?[0-9][- /.][0-3]?[0-9][- /.](?:[0-9]{2})?[0-9]{2}$'
    for item in a_list: 
        matches = re.findall(pattern, item)
    return matches
    