#!/bin/bash
#该脚本被配置在crontab中
# crontab -e
# * 8,12,18 * * * /opt/MT/MtCrawler/start.sh
# 将会在每天早晨8点、12点、晚上6点执行
oldpwd=`pwd`

cd /opt/MT/MtCrawler/

python ./start.py >>../crawlerOut.log 2> /dev/null &

cd $oldpwd
