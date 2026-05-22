#!/bin/sh

# Expand installed nt 4 disk.
gzip -d < hd.img.gz > hd.img

# Test nt 4 can boot and shut down
./nt40.sh
python3 ./check-nt-shutdown.py
