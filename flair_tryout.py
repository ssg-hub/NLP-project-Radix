from functions import preprocess, named_entities, pdf_to_text
import flair
from flair.data import Sentence
from flair.models import SequenceTagger


# Load the model
tagger = SequenceTagger.load('ner')

# pdf model
pdf = '/home/becode/Documents/Projects/9.RadixNLP/curriculum_vitae_data-master/pdf/526.pdf'

pages, text = pdf_to_text(pdf)

# take a sentence
s= Sentence('GeeksforGeeks is Awesome.')

# run NER over sentence
tagger.predict(s)
print(s)
print(s.to_tagged_string)
  
# iterate and print
for entity in s.get_spans('ner'):
    print(entity)

print(s.to_dict(tag_type='ner'))
