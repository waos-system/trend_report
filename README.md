# TODO
snscrapeが使用できない、X APIは有料のため開発を中断
Github Actionも停止中


AI Trend Monitor Ultra

Features
- Region filtering (Japan / US / Europe)
- Bot filtering
- BERT embeddings
- Event clustering
- Trend detection
- Time-series trend DB
- Trend search
- Trend map
- Automated reports

Setup

pip install -r requirements.txt

Run pipeline

python scripts/collect_x.py
python scripts/region_filter.py
python scripts/bot_filter.py
python scripts/embed.py
python scripts/cluster.py
python scripts/trend_detect.py
python scripts/timeseries.py
python scripts/trend_map.py
python scripts/report.py

GitHub Actions data collection flow

Workflow: .github/workflows/run.yml

Trigger
- Schedule: every 10 minutes (cron: */10 * * * *)
- Manual: workflow_dispatch

Steps
- Checkout repository
- Setup Python 3.10
- Install dependencies: pip install -r requirements.txt
- Prepare Pages output: copy web/* to docs/
- Run pipeline in order:
  - scripts/collect_x.py
  - scripts/region_filter.py
  - scripts/bot_filter.py
  - scripts/embed.py
  - scripts/cluster.py
  - scripts/trend_detect.py
  - scripts/timeseries.py
  - scripts/trend_map.py (writes docs/data/trend_map.json)
  - scripts/report.py (writes docs/reports/report.txt)

Output
- Static site: docs/index.html and docs/trendmap.html
- Data for UI: docs/data/trend_map.json
- Report: docs/reports/report.txt
