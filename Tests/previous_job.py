import pandas as pd

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append("/home/becode/Documents/GitHub/NLP-project-Radix/Shilpa")
from functions import pdf_to_text, preprocess, extract_lines_tokenized, remove_noise, lines_without_noise

pdf = "/home/becode/Documents/GitHub/NLP-project-Radix/assets/pdfs/222.pdf"

check = str(pdf_to_text(pdf))
to_check = list(extract_lines_tokenized(check))
# print(to_check)

job_titles = pd.read_csv("/home/becode/Documents/GitHub/NLP-project-Radix/Tests/job_titles.csv")
print(job_titles.head(20))