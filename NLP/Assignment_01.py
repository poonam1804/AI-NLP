##Assignment No.01##


import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "India is my country. Maharashtra is my state."

# Process the text
doc = nlp(text)

# 1️⃣ Tokenization
print("1. Tokenization:")
for token in doc:
    print(token.text, token.idx)

# 2️⃣ Stop Word Removal
print("\n2. Stop Words Removal:")
print([token.text for token in doc if not token.is_stop])

# 3️⃣ Lemmatization
print("\n3. Lemmatization:")
for token in doc:
    if token.text != token.lemma_:
        print(f"{token.text} → {token.lemma_}")

# 4️⃣ Part of Speech Tagging
print("\n4. Part of Speech Tagging:")
for token in doc:
    print(f"{token.text:12} POS: {token.pos_} | {spacy.explain(token.tag_)}")




"""India 0
is 6
my 9
country 12
. 18
Maharashtra 20
is 32
my 35
state 38
. 43
[India, country, ., Maharashtra, state, .]
is : be
is : be
TOKEN: India
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: my
=====
TAG: PRP$       POS: DET
EXPLANATION: pronoun, possessive

TOKEN: country
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: Maharashtra
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: my
=====
TAG: PRP$       POS: DET
EXPLANATION: pronoun, possessive

TOKEN: state
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer"""