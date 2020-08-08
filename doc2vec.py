from gensim.models.doc2vec import Doc2Vec
from sklearn.metrics.pairwise import cosine_similarity

import string
import nltk

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

base_document = "This is an example sentence for the document to be compared"
documents = ["This is the collection of documents to be compared against the base_document"]

def preprocess(text):
	# Steps:
	# 1. lowercase
	# 2. Lammetize. (It does not stem. Try to preserve structure not to overwrap with potential acronym).
	# 3. Remove stop words.
	# 4. Remove punctuations.
	# 5. Remove character with the length size of 1.

	lowered = str.lower(text)

	stop_words = set(stopwords.words('english'))
	word_tokens = word_tokenize(lowered)

	words = []
	for w in word_tokens:
		if w not in stop_words:
			if w not in string.punctuation:
				if len(w) > 1:
					lemmatized = lemmatizer.lemmatize(w)
					words.append(lemmatized)

	return words

def process_doc2vec_similarity():

	# Both pretrained models are publicly available at public repo of jhlau.
	# URL: https://github.com/jhlau/doc2vec

	# filename = './models/apnews_dbow/doc2vec.bin'
	filename = './models/enwiki_dbow/doc2vec.bin'

	model= Doc2Vec.load(filename)

	tokens = preprocess(base_document)

	# Only handle words that appear in the doc2vec pretrained vectors. enwiki_ebow model contains 669549 vocabulary size.
	tokens = list(filter(lambda x: x in model.wv.vocab.keys(), tokens))

	base_vector = model.infer_vector(tokens)

	vectors = []
	for i, document in enumerate(documents):

		tokens = preprocess(document)
		tokens = list(filter(lambda x: x in model.wv.vocab.keys(), tokens))
		vector = model.infer_vector(tokens)
		vectors.append(vector)

		print("making vector at index:", i)

	scores = cosine_similarity([base_vector], vectors).flatten()

	highest_score = 0
	highest_score_index = 0
	for i, score in enumerate(scores):
		if highest_score < score:
			highest_score = score
			highest_score_index = i

	most_similar_document = documents[highest_score_index]
	print("Most similar document by Doc2vec with the score:", most_similar_document, highest_score)

process_doc2vec_similarity()
