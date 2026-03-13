
import json,datetime

trends=json.load(open("data/trends.json"))

txt="AI Trend Report\n"
txt+=str(datetime.datetime.utcnow())+"\n\n"

for t in trends:
    txt+=f"cluster {t['cluster']} size {t['size']}\n"

open("reports/report.txt","w").write(txt)

print("report created")
