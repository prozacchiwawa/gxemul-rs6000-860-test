#!/bin/sh
exec ../gxemul -M 128 -X -x -v -v -e ibm860 -d s3:hd2.img -d R:P91G1671.IMG -d n:860.nvram.aix415 -V -q -c 'script aix415-boot.dbg'
