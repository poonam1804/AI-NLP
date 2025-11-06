###  Assignment No 4 ###

"""Assignment Title : Implement Bi-gram, Tri-gram word sequence and its count in text input
data using NLTK library"""
# Import ngrams from nltk
from nltk import ngrams

# Input sentence
sentence = "Earth is the third planet from the Sun in our solar system and the only known celestial body to support life."

# Split the sentence into words
words = sentence.split()

# ---------- UNIGRAM ----------
print("\n*** UNIGRAM ***")
for gram in ngrams(words, 1):
    print(gram)

# ---------- BIGRAM ----------
print("\n*** BIGRAM ***")
for gram in ngrams(words, 2):
    print(gram)

# ---------- TRIGRAM ----------
print("\n*** TRIGRAM ***")
for gram in ngrams(words, 3):
    print(gram)