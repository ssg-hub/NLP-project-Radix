from nltk import ngrams
from allpages import fromSkillsPDF

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append("/home/becode/Documents/GitHub/NLP-project-Radix/Shilpa")
from functions import extract_lines_tokenized, lines_without_noise, pdf_to_text

doc, text = pdf_to_text("/home/becode/Documents/GitHub/NLP-project-Radix/assets/pdfs/1964.pdf")

text, tags = extract_lines_tokenized(text)

noiseless = lines_without_noise(text)
noiseless = str(noiseless)

n = 2
bigram = ngrams(noiseless.split(), n)

tryout = []
for grams in bigram:
    tryout.append(grams)


skills = fromSkillsPDF(tryout)

print(skills)