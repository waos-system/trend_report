
import json,pandas as pd

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

json.dump(result,open("data/trend_map.json","w"))
