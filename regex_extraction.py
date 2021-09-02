import re


# using regex to extract phone
phone_regex = re.compile(r'[\+\(]*[1-9][0-9 .\-\(\)]{8,}[0-9]')

# function 
def extract_phone_number(cv_text):
    """
    Function to use the regex to extract phone number from text
    """
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
        if len(phone_numbers) > 1: return phone_numbers
        else : return phone_numbers[0]

    # return none if no numbers found as per regex rule
    return None


#using regex to extract email address
email_regex = re.compile(r'[\w._-]+@[\w-]+\.[\w.-]+')

#function
def extract_email_address(cv_text : str):
    """
    Function to extract emails using regex
    """

    # matching all using regex
    emails = re.findall(email_regex, cv_text)
    
    # check if matches are found
    if emails :
        # if more than one email found return as a list
        if len(emails) > 1: return emails
        else : return emails[0]

    # return none if no numbers found as per regex rule
    return None

    