
import snscrape.modules.twitter as sntwitter
import pandas as pd
from config.settings import KEYWORDS,MAX_POSTS

rows=[]

for k in KEYWORDS:
    query=f"{k} lang:ja OR lang:en"
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i>MAX_POSTS:
            break

        rows.append({
            "date":str(tweet.date),
            "text":tweet.content,
            "user":tweet.user.username,
            "followers":tweet.user.followersCount,
            "lang":tweet.lang,
            "location":tweet.user.location
        })

df=pd.DataFrame(rows)

df.to_json("data/posts.json",orient="records",force_ascii=False)

print("collected",len(df))
