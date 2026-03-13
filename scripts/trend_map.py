
import json
import os
import pandas as pd

df=pd.read_json("data/clean.json")

regions={
"japan":["tokyo","osaka","japan"],
"usa":["usa","new york","california"],
"europe":["germany","france","uk"]
}

result={}

for r,keys in regions.items():
    result[r]=0
    for k in keys:
        result[r]+=df.location.str.lower().str.contains(k).sum()

out_dir=os.path.join("docs","data")
os.makedirs(out_dir, exist_ok=True)
json.dump(result,open(os.path.join(out_dir,"trend_map.json"),"w"))
