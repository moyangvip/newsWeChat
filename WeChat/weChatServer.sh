#!/bin/bash

showHelp()
{
    echo "1、输入\"./weChatServer.sh start\"    启动（或重启）微信服务，且微信服务在后台运行"
    echo "2、输入\"./weChatServer.sh end\"    退出微信服务"
    echo "3、输入\"./weChatServer.sh hStart\"    在前台启动(或重启)微信服务，用于调试"
}

exitServer()
{
    #获取原服务的进程ids
    serverIds=$(ps -aux | grep 'python ./main.py 80' | awk '{print $2}')

    memcachedIds=$(ps -aux | grep 'memcached -m 500 -p 11333 -uroot' | awk '{print $2}')

    #遍历并强制退出原服务
    for serverId in ${serverIds}
    do
        kill -9 ${serverId}
        echo "已删除微信服务：${serverId}"
    done

    #遍历并强制退出memcached
    for memcachedId in ${memcachedIds}
    do
        kill -9 ${memcachedId}
        echo "已删除memcached服务：${memcachedId}"
    done
}

startServer()
{
    #先重启memcached
    nohup memcached -m 500 -p 11333 -uroot &

    #重新开启服务
    if [ $1 == 1 ];then
        #当前服务在后台运行，绑定端口为80，将日志输出到weChatOut.log文件,将错误信息输出到weChatErr.log
        nohup python ./main.py 80 >> weChatOut.log 2>> weChatErr.log &
        if [ $? -eq 0 ];then
            echo "开启服务成功，绑定端口为80，输出日志为weChatOut.log"
        fi
    else
        python ./main.py 80
    fi
}
args=$1
if [ $args == "" ]; then
    showHelp
    echo "no"
elif [ $args == "start" ]; then
    #退出原服务
    exitServer
    #开启新服务
    startServer 1

    
elif [ $args == "end" ]; then
    #退出原服务
    exitServer
    echo "退出服务成功"


elif [ $args == "hStart" ]; then
    echo "hStart"
    #退出原服务
    exitServer
    #开启新服务
    startServer 0
fi
exit 0