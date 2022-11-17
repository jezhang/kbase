## AC86U安装OPKG和Python3

路由机型：AC86U arm架构安装python3与pip

### 安装opkg软件源

1、创建软件安装目录

```sh
cd /jffs
mkdir /jffs/opt
ln -nsf /jffs/opt /tmp/opt
```

2、安装opkg

```sh
wget https://pkg.entware.net/binaries/armv7/installer/entware_install.sh
sh ./entware_install.sh
 
#软件源地址
https://pkg.entware.net/binaries/armv7/installer/
#注意
梅林固件自带一个entware.sh的安装脚本，但是要求必须插上一个ext4等linux文件系统的U盘。这里下载的这个安装脚本不需要插u盘。如果你的路由器存储空间比较小，不建议使用本方法。
```


3、自动挂载opt分区

```sh
在/jffs/scripts位置建立文件，文件名：post-mount
#内容如下:(如原来就有内容就追加)
#!/bin/sh
ln -nsf /jffs/opt /tmp/opt
```

4、给脚本增加权限

```sh
chmod a+rx /jffs/scripts/post-mount 
```

到此路由器上已经安装opkg软件

### 安装python3与pip

```sh
opkg install python3
opkg install python3-pip
```

mips架构的自行参见上方安装方式安装即可

```sh
#软件源安装脚本：
http://pkg.entware.net/binaries/mipsel/installer/installer.sh
#软件源目录
http://pkg.entware.net/binaries/mipsel/
```