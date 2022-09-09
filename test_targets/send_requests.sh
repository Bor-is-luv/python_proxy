#!/bin/bash

while :
do
    curl -s -o /dev/null -X GET http://test_task:5000/ &
    sleep 0.20
done