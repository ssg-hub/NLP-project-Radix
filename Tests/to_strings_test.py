from io import StringIO
import os

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

import spacy
from spacy.tokens import span
import dateparser

# def get_string():
output_string = StringIO()
with open('pdf/27.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

# print(output_string.getvalue())
# print(type(output_string))


nlp = spacy.load("en_core_web_sm")

sents = nlp(output_string)
# [ee for ee in sents.ents if ee.label_ == 'PERSON']

def person_entities(doc):
    new_ents = []
    for ent in doc.ents:
        # Only check for title if it's a person and not the first token
        if ent.label_ == "PERSON":
            if ent.start != 0:
                # if person preceded by title, include title in entity
                prev_token = doc[ent.start - 1]
                if prev_token.text in ("Dr", "Dr.", "Mr", "Mr.", "Ms", "Ms."):
                    new_ent = span(doc, ent.start - 1, ent.end, label=ent.label)
                    new_ents.append(new_ent)
                else:
                    # if entity can be parsed as a date, it's not a person
                    if dateparser.parse(ent.text) is None:
                        new_ents.append(ent) 
        else:
            new_ents.append(ent)
    doc.ents = new_ents
    return doc

# Add the component after the named entity recognizer
# nlp.remove_pipe('expand_person_entities')
nlp.add_pipe(person_entities, after='ner')

doc = nlp(output_string)
[(ent.text, ent.label_) for ent in doc.ents if ent.label_=='PERSON']
