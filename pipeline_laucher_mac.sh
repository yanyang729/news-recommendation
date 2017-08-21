#!/bin/bash
source activate news
redis-server &
mongod &

cd news_pipeline
python news_monitor.py &
python news_fetcher.py &
python news_deduper.py &

echo "=================================================="
read -p "PRESS [ANY KEY] TO TERMINATE PROCESSES." PRESSKEY

sudo killall python
sudo killall mongod
redis-cli shutdown
source deactivate news
