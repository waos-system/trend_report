
import json,sys

keyword=sys.argv[1]

data=json.load(open("data/timeseries.json"))

series=[]

for d in data:
    v=d["counts"].get(keyword.lower(),0)
    series.append({
        "time":d["time"],
        "value":v
    })

print(json.dumps(series))
