# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
import os

# Define the path to the directory containing text files
dir_path = '../data_library'
# dir_path = '../data_library_hebrew'

from InstructorEmbedding import INSTRUCTOR

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

import boto3
aws_access_key_id = "AKIAUJVBNW2TBB5VTU5S"
aws_secret_access_key = "j0o29riJ413mocUN77PYIbNZB0774Gbaha92/5ny"



# user_task = 'Take an injection for your allergy'
model = INSTRUCTOR('hkunlp/instructor-xl')

def retrieve_document(user_task):
    # Load the text files into a list
    file_list = []
    file_names = []
    for file in os.listdir(dir_path):
        if file.endswith('.txt'):
            with open(os.path.join(dir_path, file), 'r') as f:
                file_list.append(f.read())
                file_names.append(file)

    # translate the user task to english
    user_task = translate_text(user_task, target_language='en')
    query = [['Represent the task for retrieving supporting documents:', user_task]]
    print('*******************:', query)
    corpus = [['Represent the document for retrieval: ', file] for file in file_list]

    query_embeddings = model.encode(query)
    corpus_embeddings = model.encode(corpus)
    similarities = cosine_similarity(query_embeddings,corpus_embeddings)
    print(similarities)
    retrieved_doc_id = np.argmax(similarities)
    print(retrieved_doc_id)
    print(file_names[retrieved_doc_id])
    return file_names[retrieved_doc_id]



def translate_text(text, target_language='en'):
    # Set up the AWS Translate client
    translate = boto3.client(service_name='translate',
                            region_name='us-west-2', aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key)

    # Translate the text
    result = translate.translate_text(Text=text, SourceLanguageCode='he' if target_language=='en' else 'he', TargetLanguageCode=target_language)

    # Print the translated text
    print(f'Translated text: {result["TranslatedText"]}')
    return result["TranslatedText"]


