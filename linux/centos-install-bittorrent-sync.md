CentOS 安装BitTorrent Sync详细步骤
==================================

这个软件安装完后通过网页浏览器设置共享目录并生成同步Secret，异地的客户端可以通过这个同步Secret访问共的目录，其中有读写和只读两种同步方式选择，以点对点的形式传送数据，其实可以理解为一种新型的P2P分享方式。

这里我们可以用这个软件来同步备份下载盒子上的指定目录的所有文件，下面的内容是盒子端的配置过程。
linux系统下的安装与配置（使用root用户登录）

1. 首先要下载应用程序解压，根据系统的字长选择

32位系统

```sh
wget http://btsync.s3-website-us-east-1.amazonaws.com/btsync_i386.tar.gz
tar zxvf btsync_i386.tar.gz
cd btsync*
```

64位系统

```sh
wget http://btsync.s3-website-us-east-1.amazonaws.com/btsync_x64.tar.gz 
tar zxvf btsync_x64.tar.gz
cd btsync*
```

2. 运行程序输出配置模板文件

```sh
./btsync --dump-sample-config > btsync.conf
```

3. 编辑上一步输出的btsync.conf

```sh
vi btsync.conf
```

将下面的<>部分改为你自己的服务器的信息。例如“<设备名>”改为“My BT Server”.
端口不要设置成80、8112、9091、443之类的，避免与其他软件应用冲突。

```vim
{ "device_name": "<设备名>", "listening_port" : 0, // 0 - randomize port "storage_path" : "/home/root/.sync", // uncomment next line if you want to set location of pid file // "pid_file" : "/var/run/syncapp/syncapp.pid", "check_for_updates" : true, "use_upnp" : true, // use UPnP for port mapping "download_limit" : 0, "upload_limit" : 0, "webui" : { "listen" : "<服务器的IP地址>:<端口>", "login" : "<登陆用户名>", "password" : "<登陆密码>" } // Advanced preferences can be added to config file. // Info is available in BitTorrent Sync User Guide. }
```

4. 运行BT sync，此时系统会新增一个btsync进程

```sh
./btsync --config btsync.conf
```

如果想关闭BT sync可以使用killall命令关闭

```sh
killall btsync
```

5. 把BT sync加入开机启动

```sh
vi /etc/rc.local
```

exit 0 前一行加入

```sh
cd /$BTSYNC_DIR ./btsync --config btsync.conf
```

通过本地浏览器打开<服务器的IP地址>:<端口>/gui 登陆以后即可设置同步目录。





