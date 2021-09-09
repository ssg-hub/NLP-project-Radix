from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from fuzzywuzzy import process, fuzz

from cv_dataframe import df

language_col = df['Languages'].tolist()

# https://www.geeksforgeeks.org/fuzzywuzzy-python-library/
lang_i_list = []
for i, x in enumerate(language_col):
    #print(fuzz.partial_ratio('english', x), i, x)
    #print(fuzz.ratio('english', x), i, x)
    #print(fuzz.token_set_ratio('english', x), i, x)
    #print(fuzz.token_sort_ratio('english', x), i, x)
    wratio_lang = fuzz.WRatio('english', x)
    #print(fuzz.WRatio('english', x), i, x)
    if wratio_lang >= 70 : lang_i_list.append(i)
    #process.extract('english', language_col, scorer=fuzz.token_sort_ratio)

skills_col = df['Skills'].tolist()

# https://www.geeksforgeeks.org/fuzzywuzzy-python-library/
skills_i_list = []
for i, x in enumerate(skills_col):
    #print(fuzz.partial_ratio('english', x), i, x)
    #print(fuzz.ratio('english', x), i, x)
    #print(fuzz.token_set_ratio('english', x), i, x)
    #print(fuzz.token_sort_ratio('english', x), i, x)
    wratio_skills = fuzz.WRatio('Access', x)
    print(wratio_skills, i, x)
    if wratio_skills >= 70 : lang_i_list.append(i)
    #process.extract('english', language_col, scorer=fuzz.token_sort_ratio)

'''print("Check PG values in Position column:\n")
df1 = df['Position'].str.contains("PG")
print(df1)'''