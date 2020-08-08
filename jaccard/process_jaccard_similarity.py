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

def calculate_jaccard(word_tokens1, word_tokens2):
	# Combine both tokens to find union.
	both_tokens = word_tokens1 + word_tokens2
	union = set(both_tokens)

	# Calculate intersection.
	intersection = set()
	for w in word_tokens1:
		if w in word_tokens2:
			intersection.add(w)

	jaccard_score = len(intersection)/len(union)
	return jaccard_score

def process_jaccard_similarity():

	# Tokenize the base document we are comparing against.
	base_tokens = preprocess(base_document)

	# Tokenize each ducment
	all_tokens = []
	for i, document in enumerate(documents):
		tokens = preprocess(document)
		all_tokens.append(tokens)

		print("making word tokens at index:", i)

	all_scores = []
	for tokens in all_tokens:
		score = calculate_jaccard(base_tokens, tokens)

		all_scores.append(score)

	highest_score = 0
	highest_score_index = 0
	for i, score in enumerate(all_scores):
		if highest_score < score:
			highest_score = score
			highest_score_index = i

	most_similar_document = documents[highest_score_index]

	print("Most similar document by Jaccard with the score:", most_similar_document, highest_score)

process_jaccard_similarity()
