收集一些有趣的docker镜像
======================

## docker一键安装脚本

```sh
wget -qO- get.docker.com | sh
```

## 镜像1：rastasheep/ubuntu-sshd （带ssh的ubuntu）

地址：<https://hub.docker.com/r/rastasheep/ubuntu-sshd/>

```sh
sudo docker run -d  -p 22:22  rastasheep/ubuntu-sshd:16.04
```
用户名、密码为root

## 镜像2：itscaro/debian-ssh （带ssh的ubuntu） 

地址：<https://hub.docker.com/r/itscaro/debian-ssh/>

```sh
sudo docker run -d -p 22:22  itscaro/debian-ssh
```

用户名、密码为root

## 镜像3：tutum/centos （带ssh的centos） 

地址：<https://hub.docker.com/r/tutum/centos/>

```sh
 sudo docker run -d -p 22:22  tutum/centos
```

（centos7：tutum/centos:centos7 ）

用户名root，

密码随机，请执行 docker logs <CONTAINER_ID> 查看

这个作者还有好多好东西：<https://hub.docker.com/r/tutum/centos/>

## 镜像4：alexwhen/docker-2048（游戏2048）

地址：<https://hub.docker.com/r/alexwhen/docker-2048/>

```sh
sudo docker run -d -p 80:80 alexwhen/docker-2048
```

## 镜像5：dorowu/ubuntu-desktop-lxde-vnc（noVNC、Firefox51）

地址：<https://hub.docker.com/r/alexwhen/docker-2048/>

docker run -it  -p 80:80 dorowu/ubuntu-desktop-lxde-vnc

Browse <http://localhost/>

## 镜像6：consol/centos-xfce-vnc （VNC、noVNC、密码、chrome、Firefox45）

地址：<https://hub.docker.com/r/consol/ubuntu-xfce-vnc/>

```sh
run -it -p 5901:5901 -p 6901:6901 -e "VNC_PW=my-new-password" -e VNC_RESOLUTION=800x600 consol/centos-xfce-vnc
```

默认VNC密码：vncpassword

VNC-Server (default VNC port 5901)

noVNC - HTML5 VNC client (default http port 6901)

其他相关

onsol/centos-xfce-vnc: Centos7 with Xfce4 UI session

consol/ubuntu-xfce-vnc: Ubuntu with Xfce4 UI session

consol/centos-icewm-vnc: dev     Centos7 with IceWM UI session

consol/ubuntu-icewm-vnc: dev      Ubuntu with IceWM UI session

## 镜像7：fish/peerflix-server （支持磁力，种子）

地址：<https://hub.docker.com/r/dorowu/ubuntu-desktop-lxde-vnc/>

```sh
docker run -it  -p 9000:9000 fish/peerflix-server
```

Browse <http://localhost:9000/>

## 镜像8：jpillora/cloud-torrent（种子下载，搜索）

地址：<https://hub.docker.com/r/jpillora/cloud-torrent/>

```sh
docker run -d -p 3000:3000 -v /path/to/my/downloads:/downloads jpillora/cloud-torrent
```

Browse <http://localhost:80/>


## 镜像9：jim3ma/google-mirror（google镜像，如需ssl要手动添加）

地址：<https://hub.docker.com/r/jim3ma/google-mirror/>

```sh
docker run -d -p 80:80 jim3ma/google-mirror
```

Browse <http://ip:80/>

## 镜像10：google-reverse-proxy（google镜像，有ssl）

地址：<https://hub.docker.com/r/jokester/google-reverse-proxy/>

```sh
docker run -d --publish 54321:20081 --restart=always jokester/google-reverse-proxy
```

Browse <http://ip:54321/>

## 镜像11：forsaken-mail（临时邮箱）

地址：<https://hub.docker.com/r/rockmaity/forsaken-mail/>

```sh
docker run --name forsaken-mail -itd -p 25:25 -p 3000:3000 rockmaity/forsaken-mail
```

Browse <http://ip:3000/>

## 镜像12：imdjh/owncloud-with-ocdownloader（owncloud,torrent,aria2,youtube-dl）

地址：<https://hub.docker.com/r/imdjh/owncloud-with-ocdownloader/>

```sh
docker run -d -p 80:80 -e OWNCLOUD_VERSION=9.1.4 -v /var/www/html/data:/var/www/html/data imdjh/owncloud-with-ocdownloader
```

Browse <http://ip/>

## 镜像13：v2ray/official（v2ray）

地址：<https://hub.docker.com/r/v2ray/official/>

```sh
docker run -d -p 8001:8001 v2ray/official
```

参考：<https://liyuans.com/archives/arukas-build-v2ray.html>

## 镜像14：timonier/aria2

地址：<https://hub.docker.com/r/timonier/aria2/>

```sh
docker run -i  -t -v /data:/data --net host timonier/aria2 --dir=/data --enable-rpc --rpc-listen-all=true
```

配合使用：timonier/webui-aria2（aria2web管理）

地址：<https://hub.docker.com/r/timonier/webui-aria2/>

```sh
docker run  -i -t -p 80:80 timonier/webui-aria2
```

## 镜像15：jaegerdocker/pan

Docker Hub: <https://hub.docker.com/r/jaegerdocker/pan/>

简介：Docker-Pan: Filerun + AriaNg + Aria2 实现离线下载及在线播放

详细介绍：老司机使用 docker-pan 一键搭建可离线磁力种子的私有云盘,可在线播放预览文件 

<https://www.v2ex.com/t/383801>

## 镜像16：aria2-ariang-x-docker-compose

代码地址：<https://github.com/wahyd4/aria2-ariang-x-docker-compose>

简介：docker-compose: docker-pan 老司机优化版 / 在线下载 BT 磁链 / 在线观看 / 全功能文件管理 / 云盘应用

详情：老司机优化版：使用 docker / docker-compose 搭建在线下载 BT, 磁力链接，在线观看，全功能文件管理，云盘应用 

<https://www.v2ex.com/t/385118>








 