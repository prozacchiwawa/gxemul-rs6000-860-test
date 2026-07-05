#!/bin/sh

set -e

# Test basic firmware operation
./run860.sh
python3 ./compare-image.py vdsk.json

# Expand installed nt 4 disk.
gzip -d < hd.img.gz > hd.img

# Test nt 4 can boot and shut down
./nt40.sh
python3 ./compare-image.py nt-shutdown.json

# Test aix 4.1.5 can get fully booted
gzip -d < hd2.img.gz > hd2.img
./aix415.sh
python3 ./compare-image.py aix415-boot.json
