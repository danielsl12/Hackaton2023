from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Define the path to the directory containing text files
dir_path = './data_library'

# Load the text files into a list
file_list = []
for file in os.listdir(dir_path):
    if file.endswith('.txt'):
        with open(os.path.join(dir_path, file), 'r') as f:
            file_list.append(f.read())

from InstructorEmbedding import INSTRUCTOR
model = INSTRUCTOR('hkunlp/instructor-xl')

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

user_task = 'Take an injection for your allergy'
query  = [['Represent the task for retrieving supporting documents: ', user_task]]

text = ''
corpus = [['Represent the document for retrieval: ', file] for file in file_list]

query_embeddings = model.encode(query)
corpus_embeddings = model.encode(corpus)
similarities = cosine_similarity(query_embeddings,corpus_embeddings)
print(similarities)
retrieved_doc_id = np.argmax(similarities)
print(retrieved_doc_id)
print(file_list[retrieved_doc_id])
