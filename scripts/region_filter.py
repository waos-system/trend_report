
import pandas as pd

df=pd.read_json("data/posts.json")

regions=["japan","tokyo","osaka","usa","united states","uk","germany","france"]

def region_ok(x):
    if not isinstance(x,str):
        return False
    x=x.lower()
    return any(r in x for r in regions)

df=df[df.location.apply(region_ok)]

df.to_json("data/region_filtered.json",orient="records",force_ascii=False)

print("region filtered",len(df))
