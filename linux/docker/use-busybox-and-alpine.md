通过Busybox和Alpine来精简Docker镜像
================================

## 使用一个最小的Linux构建版本，如BusyBox或者Alpine

如果用户的目标是小而精，那么BusyBox可能是首选。BusyBox镜像的大小竟然精简到了小于2.5MB！
倘若用户以如下命令启动一个BusyBox镜像，那么可能会发生一些意外情况：

```sh
➜  ~ git:(master) ✗ docker run -ti busybox /bin/bash
Unable to find image 'busybox:latest' locally
latest: Pulling from library/busybox
0f8c40e1270f: Pull complete
Digest: sha256:1303dbf110c57f3edf68d9f5a16c082ec06c4cf7604831669faf2c712260b5a0
Status: Downloaded newer image for busybox:latest
docker: Error response from daemon: OCI runtime create failed: container_linux.go:345: starting container process caused "exec: \"/bin/bash\": stat /bin/bash: no such file or directory": unknown.
```

BusyBox甚至已经精简到了没有bash的程度！取而代之的是它使用ash，这是一个兼容posix的shell———实际上它是像bash和ksh这样更高级shell的一个受限版本：

```sh
docker run -ti busybox /bin/ash
```

其他维护人员已经给BusyBox加上了包管理功能。举个例子，progrium/busybox(5MB)，但是它有opkg，这意味着用户可以轻松地安装其他常用软件包，同时将镜像的大小保持为绝对最小。举个例子，如果缺少bash的话，可以像下面这样安装它：

```sh
docker run -ti progrium/busybox /bin/ash
```

在提交时，这会生成一个6MB的镜像。

有一个不太完善但是很有意思的docker镜像（可能会取代progrium/busybox）便是gliderlabs/alpine。它和BusyBox很像，但是有更广泛的软件包。