#!/bin/bash

kill $(cat /home/ubuntu/ControverseSite/controverse.pid)
source /home/ubuntu/ControverseSite/venv/bin/activate
/home/ubuntu/ControverseSite/venv/bin/gunicorn --daemon -b '0.0.0.0:80' --pid=/home/ubuntu/ControverseSite/controverse.pid server:app