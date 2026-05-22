#!/bin/sh
exec ../gxemul -M 32 -X -x -v -v -e ibm860 -d s6:hd.img -d R:P91G1671.IMG -d n:860.nvram.windows -V -q -c 'script nt40-run-boot-shutdown.dbg'
