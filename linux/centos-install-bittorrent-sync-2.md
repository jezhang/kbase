在Linux上安装配置BitTorrent Sync
================================

### 背景介绍

目前我们线上的前端服务器数量比较多，超过200多台，每次发布新应用的时候，都是将软件包放在一台专门的Push服务器上，再由所有的前端服务器通过rsync自动同步。但随着前端服务器的数量越来越多，Push服务器的带宽已经成为了瓶颈。
而BitTorrent Sync这种P2P方式的同步则是一种解决方案。同时它的跨平台支持也非常好，无论是Windows，Linux，Mac OS，甚至手机端都有相应的客户端。虽然目前尚未开源，但可以免费使用，还是很不错的。

#### 1. 下载BitTorrent Sync，在所有服务器上：

```sh
$ sudo wget http://download-lb.utorrent.com/endpoint/btsync/os/linux-glibc23-x64/track/stable -O /tmp/btsync_glibc23_64.tar.gz
$ sudo mkdir /opt/btsync
$ cd /opt/btsync
$ sudo tar xzf /tmp/btsync_glibc23_64.tar.gz
$ sudo vim /etc/init.d/btsync
$ sudo chmod +x /etc/init.d/btsync
```

#### 2. 创建服务管理脚本，在所有服务器上：

```sh
#!/bin/sh
#
# description: starts and stops the btsync client

CONF=/opt/btsync/btsync.cfg
PROC=/opt/btsync/btsync
PIDFILE=/opt/btsync/btsync.pid

start() {
  PID1=$(pidof btsync)
  if [ -z ${PID1} ]; then
    echo -n "Starting BitTorrent Sync: "
    ${PROC} --config ${CONF}
  else
    echo "BitTorrent Sync is already running at pid:${PID1}"
  fi
  return $?
}

stop() {
  echo -n "Stopping BitTorrent Sync: "
  PID1=$(pidof btsync)
  if [ ! -z ${PID1} ]; then
    kill -9 ${PID1}
    echo "OK"
  else
    echo "Failed"
  fi
  return $?
}

status() {
  PID1=$(pidof btsync)
  PID2=$(cat ${PIDFILE})
  echo -n "Checking BitTorrent Sync: "
  if [ ! -z ${PID1} ] && [ "${PID1}" -eq "${PID2}" ]; then
    echo "OK"
  else
    echo "Failed"
  fi
  return $?
}

case "$1" in
  start)
   start
  ;;
  stop)
    stop
  ;;
  restart)
    stop
    sleep 1
    start
  ;;
  status)
    status
  ;;
  *)
    echo $"Usage: $0 {start|stop|restart|status}"
    exit 2
esac
```

#### 3. 创建用于同步的目录，在所有服务器上：

```sh
$ sudo mkdir /opt/btsync_transfer
$ sudo vim /opt/btsync/btsync.cfg
```

#### 4. 创建配置文件，在btsync-server上：

```sh
{
  "device_name": "btsync-server",
  "listening_port" : 0, // 0 - randomize port

  "storage_path" : "/opt/btsync",
  "pid_file" : "/opt/btsync/btsync.pid",

  "download_limit" : 0, // 0 - no limit
  "upload_limit" : 0,

  "webui" :
  {
    "listen" : "0.0.0.0:8888",
    "login" : "admin",
    "password" : "btsync"
  }

  ,
  "folder_rescan_interval" : 60,
  "lan_encrypt_data" : false,
  "lan_use_tcp" : true
}
```

#### 5.  创建同步所需的密钥，在btsync-server上：

```sh
sudo /etc/init.d/btsync start
```
