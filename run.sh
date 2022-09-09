#!/bin/bash

sudo docker-compose up --build | grep -e 'start\|sleep\|kill\|stop\|exited\|equals'
# cat file.txt | grep -e '(start|sleep|kill|stop|exited|equals)'