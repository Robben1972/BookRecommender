import pandas as pd
import numpy as np
import faiss
import requests



def create_textual_representation(row):
    textual_representation = f"""Subtitle: {row['subtitle']},
Title: {row['title']},
Authors: {row['authors']},
Categories: {row['categories']},
Published_year: {row['published_year']},
Num_pages: {row['num_pages']},
Description: {row['description']}
"""
    return textual_representation



if __name__ == '__main__':
    dim = 3072

    index = faiss.IndexFlatL2(dim)

    df = pd.read_csv('books.csv')
    df['textual_representation'] = df.apply(create_textual_representation, axis=1)

    X = np.zeros((len(df['textual_representation']), dim), dtype='float32')

    for i, representaion in enumerate(df['textual_representation']):
        if i % 200 == 0:
            print(f'processing {i}th value')

        res = requests.post('http://localhost:11434/api/embeddings', json={'model': 'llama3.2', 'prompt': representaion})

        embedding = res.json()['embedding']

        X[i] = np.array(embedding)

    index.add(X)

    faiss.write_index(index, 'index')