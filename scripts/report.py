
import datetime
import json
import os

trends=json.load(open("data/trends.json"))

txt="AI Trend Report\n"
txt+=str(datetime.datetime.utcnow())+"\n\n"

for t in trends:
    txt+=f"cluster {t['cluster']} size {t['size']}\n"

out_dir=os.path.join("docs","reports")
os.makedirs(out_dir, exist_ok=True)
open(os.path.join(out_dir,"report.txt"),"w").write(txt)

print("report created")
