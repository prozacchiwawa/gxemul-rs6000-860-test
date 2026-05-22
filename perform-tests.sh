#!/bin/sh

gzip -d < hd.img.gz > hd.img
script -c 'nt40.sh 2>/dev/null' < /dev/null
python3 ./check-nt-shutdown.py
