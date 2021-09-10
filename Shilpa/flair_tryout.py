from functions import preprocess, named_entities, pdf_to_text

from flair.data import Sentence
from flair.models import SequenceTagger


# Load the model
tagger = SequenceTagger.load('ner-ontonotes-large')

# pdf model
pdf = "/home/becode/Documents/GitHub/NLP-project-Radix/assets/pdfs/16.pdf"

pages, text = pdf_to_text(pdf)

# take a sentence
s = Sentence(text)

# run NER over sentence
tagger.predict(s)
# print(s)
# print(s.to_tagged_string)


# iterate and print
for entity in s.get_spans('ner'):
    print(entity)
# print(s.to_dict(tag_type='ner'))