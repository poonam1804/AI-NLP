# ##Assignment No.02##

# #Title:Assignment to implement Bag of Words and TFIDF using Gensim library.

# Import required libraries
from gensim import corpora, models
from gensim.utils import simple_preprocess

# Step 1: Input multiple text documents
text = [
    "I love programming. Python is my favorite language.",
    "Programming helps me solve real-world problems.",
    "Python programming is fun and powerful."
]

# Step 2: Preprocess text
tokens = [simple_preprocess(sentence) for sentence in text]

# Step 3: Create dictionary (word-ID mapping)
dictionary = corpora.Dictionary(tokens)
print("Dictionary (word to ID):")
print(dictionary.token2id)

# Step 4: Convert to Bag of Words
bow_corpus = [dictionary.doc2bow(token) for token in tokens]
print("\nBag of Words (word_id, count):")
print(bow_corpus)

# Step 5: Apply TF-IDF model
tfidf_model = models.TfidfModel(bow_corpus)

# Step 6: Show TF-IDF for each document
print("\nTF-IDF (word, weight):")
for doc in bow_corpus:
    tfidf = tfidf_model[doc]
    for word_id, weight in tfidf:
        print(dictionary[word_id], ":", round(weight, 3))
    print("----")