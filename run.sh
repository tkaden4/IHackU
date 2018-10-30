#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

./dockerlets_run.sh

python Netcat/EchoMyNumber.py &
python Netcat/CTFAddition.py &
