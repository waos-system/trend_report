
import numpy as np
import json
from sklearn.cluster import DBSCAN

emb=np.load("data/embeddings.npy")

model=DBSCAN(eps=0.6,min_samples=5,metric="cosine")

labels=model.fit_predict(emb)

clusters={}

for i,l in enumerate(labels):
    if l==-1:
        continue
    clusters.setdefault(str(l),[]).append(int(i))

json.dump(clusters,open("data/clusters.json","w"))

print("clusters",len(clusters))
