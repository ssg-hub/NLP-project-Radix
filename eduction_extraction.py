import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('words')
nltk.download('maxent_ne_chunker')



def extract_education(tokens_with_pos):
    """
    Function to get the education of person out of given text
    """
    education_words = [
    'school',
    'university',
    'certificate',
    'study',
    'diploma',
    'hsc',
    'ssc',
    'college',
    'higher',
    'institute',
    'studies',
    'education',
    'high',
    'master',
    'bachelor',
    'academy',
    'polytechnic',
    'degree',
    'masters',
    'bachelors',
    'phd',
    'b.e',
    'be',
    'b.e.'  
    ]

    edu_institutes = []
    for each, tag in tokens_with_pos:
        if each.lower() in education_words:
            edu_institutes.append(each)

  

    return edu_institutes

    