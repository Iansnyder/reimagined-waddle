#!/bin/bash

user=$(id -u)
if [[ $user -ne 0 ]]; then
    echo "Must root. Exiting."
    exit 1
fi

NUM_ARGS=$#
if [[ $NUM_ARGS -ne 1 ]]; then
    echo "usage: flask-start <flask-app-name>"
    exit 1
fi

export FLASK_APP=$1
python3 -m flask run