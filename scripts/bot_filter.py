
import pandas as pd

df=pd.read_json("data/region_filtered.json")

df=df[df.followers>30]

df=df[~df.user.str.contains("bot")]

df=df.drop_duplicates(subset=["text"])

df.to_json("data/clean.json",orient="records",force_ascii=False)

print("bot filtered",len(df))
