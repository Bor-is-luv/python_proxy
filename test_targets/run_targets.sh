#!/bin/bash

export PYTHONPATH=$(pwd)

cd src
for VARIABLE in 5001 5002 5003 5004 5005
do
    echo "start target on $VARIABLE port"
    gunicorn --bind=0.0.0.0:$VARIABLE --workers=1 src.app:app &
    echo "start count handling requests for app on $VARIABLE port"
    python count_handling_requests.py $VARIABLE &
    sleep 4
done

../send_requests.sh &

echo 'sleep 100'
sleep 100

echo 'kill target on 5003 port'
kill -s 15 $(lsof -t -i:5003)

echo 'sleep 100'
sleep 100

echo 'start target on 5003 port'
gunicorn --bind=0.0.0.0:5003 --workers=1 src.app:app &

echo '--------------------------------------------'
echo 'sleep 100'
sleep 100

echo 'stop sending requests'
kill -s 9 $(pgrep -f send_requests.sh)

for VARIABLE in 5001 5002 5003 5004 5005
do
    echo "kill $VARIABLE port"
    kill -s 15 $(lsof -t -i:$VARIABLE)
done

echo "kill count handling requests for all targets"
kill -s 9 $(pgrep -f count_handling_requests.py)

exit 0
