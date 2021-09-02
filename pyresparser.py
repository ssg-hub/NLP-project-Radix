# -*- coding: utf-8 -*-
"""pyresparser

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IGz6iPVAu-gtbhOvNBovMYiY8vawpRnf
"""

!pip install pyresparser

import nltk
nltk.download('stopwords')

from pyresparser import ResumeParser

data = ResumeParser('/3254.pdf').get_extracted_data()

data

data

skills = data['skills']
skills

phone = data['mobile_number']
phone

email = data['email']
email