from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Define the path to the directory containing text files
dir_path = './guides'

# Load the text files into a list
file_list = []
for file in os.listdir(dir_path):
    if file.endswith('.txt'):
        with open(os.path.join(dir_path, file), 'r') as f:
            file_list.append(f.read())

# # Create a CountVectorizer to transform the text into vectors
# vectorizer = CountVectorizer(stop_words='english')
# vectorized_files = vectorizer.fit_transform(file_list)

from InstructorEmbedding import INSTRUCTOR
model = INSTRUCTOR('hkunlp/instructor-xl')
sentence = "3D ActionSLAM: wearable person tracking in multi-floor environments"
instruction = "Represent the Science title:"
# embeddings = model.encode([[instruction,sentence]])
# print(embeddings)

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

user_task = 'Apply for a scan'
query  = [['Represent the task for retrieving supporting documents: ', user_task]]

text = ''
corpus = [['Represent the document for retrieval: ', file] for file in file_list]
# corpus = [['Represent the Wikipedia document for retrieval: ','Capitalism has been dominant in the Western world since the end of feudalism, but most feel[who?] that the term "mixed economies" more precisely describes most contemporary economies, due to their containing both private-owned and state-owned enterprises. In capitalism, prices determine the demand-supply scale. For example, higher demand for certain goods and services lead to higher prices and lower demand for certain goods lead to lower prices.'],
#           ['Represent the Wikipedia document for retrieval: ',"The disparate impact theory is especially controversial under the Fair Housing Act because the Act regulates many activities relating to housing, insurance, and mortgage loansâ€”and some scholars have argued that the theory's use under the Fair Housing Act, combined with extensions of the Community Reinvestment Act, contributed to rise of sub-prime lending and the crash of the U.S. housing market and ensuing global economic recession"],
#           ['Represent the Wikipedia document for retrieval: ','Disparate impact in United States labor law refers to practices in employment, housing, and other areas that adversely affect one group of people of a protected characteristic more than another, even though rules applied by employers or landlords are formally neutral. Although the protected classes vary by statute, most federal civil rights laws protect based on race, color, religion, national origin, and sex as protected traits, and some laws include disability status and other traits as well.']]
query_embeddings = model.encode(query)
corpus_embeddings = model.encode(corpus)
similarities = cosine_similarity(query_embeddings,corpus_embeddings)
print(similarities)
retrieved_doc_id = np.argmax(similarities)
print(retrieved_doc_id)
print(file_list[retrieved_doc_id])

# Define a function to retrieve the most similar file to a given query
# def retrieve_most_similar_file(query):
#     # Vectorize the query
#     vectorized_query = vectorizer.transform([query])
#     # Calculate cosine similarity between the query vector and each file vector
#     similarities = cosine_similarity(vectorized_query, vectorized_files)
#     # Get the index of the most similar file
#     most_similar_index = similarities.argmax()
#     # Return the filename of the most similar file
#     return os.path.basename(os.path.normpath(file_list[most_similar_index]))

# Test the function with a query
# query = "What is the capital of France?"
# most_similar_file = retrieve_most_similar_file(query)
# print(f"The most similar file to the query is {most_similar_file}.")