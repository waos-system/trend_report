
import pandas as pd, json, datetime, os

df=pd.read_json("data/clean.json")

models=["chatgpt","claude","gemini"]

counts={}

for m in models:
    counts[m]=df.text.str.lower().str.contains(m).sum()

entry={
"time":str(datetime.datetime.utcnow()),
"counts":counts
}

path="data/timeseries.json"

if os.path.exists(path):
    with open(path) as f:
        data=json.load(f)
else:
    data=[]

data.append(entry)

json.dump(data,open(path,"w"))
