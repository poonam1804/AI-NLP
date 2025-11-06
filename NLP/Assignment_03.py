
# Assignment 3: Named Entity Recognition using spaCy

import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Function to perform NER
def perform_ner(text):
    doc = nlp(text)   # Process the text
    for ent in doc.ents:
        print(ent.text, "-", ent.label_)   # Print each entity and its type

# Example text
text = "Earth is the third planet from the Sun in our solar system."

print("Named Entities found:\n")
perform_ner(text)