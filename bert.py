import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from nltk import sent_tokenize

from sentence_transformers import SentenceTransformer

base_document = "This is an example sentence for the document to be compared"
documents = ["This is the collection of documents to be compared against the base_document"]

def process_bert_similarity():
	# This will download and load the pretrained model offered by UKPLab.
	model = SentenceTransformer('bert-base-nli-mean-tokens')

	# Although it is not explicit, it will feed the model by sentences instead of the whole documents.
	sentences = sent_tokenize(base_document)
	base_embeddings_sentences = model.encode(sentences)
	base_embeddings = np.mean(np.array(base_embeddings_sentences), axis=0)

	vectors = []
	for i, document in enumerate(documents):

		sentences = sent_tokenize(document)
		embeddings_sentences = model.encode(sentences)
		embeddings = np.mean(np.array(embeddings_sentences), axis=0)

		vectors.append(embeddings)

		print("making vector at index:", i)

	scores = cosine_similarity([base_embeddings], vectors).flatten()

	highest_score = 0
	highest_score_index = 0
	for i, score in enumerate(scores):
		if highest_score < score:
			highest_score = score
			highest_score_index = i

	most_similar_document = documents[highest_score_index]
	print("Most similar document by Doc2vec with the score:", most_similar_document, highest_score)

process_bert_similarity()
