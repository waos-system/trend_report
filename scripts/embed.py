
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

df=pd.read_json("data/clean.json")

model=SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

emb=model.encode(df.text.tolist())

np.save("data/embeddings.npy",emb)

print("embedded",len(emb))
