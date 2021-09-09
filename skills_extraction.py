import nltk
nltk.download('stopwords')
#nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('words')
nltk.download('maxent_ne_chunker')
from pyresparser import ResumeParser

def extract_skills(pdf):
    """
    Function to get the skills of the person
    """
    everything = ResumeParser(pdf).get_extracted_data()
    skills = everything['skills']
    return skills


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

    