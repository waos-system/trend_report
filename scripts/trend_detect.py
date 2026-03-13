
import json
import pandas as pd

clusters=json.load(open("data/clusters.json"))
df=pd.read_json("data/clean.json")

trends=[]

for cid,ids in clusters.items():
    sample=df.iloc[ids].text.tolist()[:3]

    trends.append({
        "cluster":cid,
        "size":len(ids),
        "sample":sample
    })

json.dump(trends,open("data/trends.json","w"),ensure_ascii=False)
