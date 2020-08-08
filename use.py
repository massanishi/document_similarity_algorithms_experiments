from sklearn.metrics.pairwise import cosine_similarity

import tensorflow as tf
import tensorflow_hub as hub

base_document = "This is an example sentence for the document to be compared"
documents = ["This is the collection of documents to be compared against the base_document"]

def process_use_similarity():
	filename = "./models/universal-sentence-encoder_4"

	model = hub.load(filename)

	base_embeddings = model([base_document])[0]

	embeddings = model(documents)

	scores = cosine_similarity([base_embeddings], embeddings).flatten()

	highest_score = 0
	highest_score_index = 0
	for i, score in enumerate(scores):
		if highest_score < score:
			highest_score = score
			highest_score_index = i

	most_similar_document = documents[highest_score_index]
	print("Most similar document by USE with the score:", most_similar_document, highest_score)

process_use_similarity()
