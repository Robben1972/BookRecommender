import faiss
import requests
import numpy as np
import pandas as pd
from createModel import create_textual_representation

df = pd.read_csv('books.csv')

index = faiss.read_index('index')

df['textual_representation'] = df.apply(create_textual_representation, axis=1)

favourite_movie = df.iloc[1358]

res = requests.post('http://localhost:11434/api/embeddings', json={'model': 'llama3.2', 'prompt': favourite_movie['textual_representation']})
embedding = np.array([res.json()['embedding']], dtype='float32')

D, I = index.search(embedding, 5)

best_matches = np.array(df['textual_representation'])[I.flatten()]

for match in best_matches:
    print('Next Book:')
    print(match)
    print()
