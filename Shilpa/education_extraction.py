
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