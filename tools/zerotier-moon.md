

<https://zczc.cz/2018/03/14/ZeroTier-moon-%E8%AE%BE%E7%BD%AE%E6%95%99%E7%A8%8B/>


不同系统下的 ZeroTier 目录位置：

```sh
Windows: C:/ProgramData/ZeroTier/One
Macintosh: /Library/Application Support/ZeroTier/One
Linux: /var/lib/zerotier-one
FreeBSD/OpenBSD: /var/db/zerotier-one
```

## Server Side

```sh
# Create docker instance
docker run --name zerotier-moon -d -p 9993:9993 -p 9993:9993/udp seedgou/zerotier-moon -4 65.49.206.47

# Create custom docker instance

docker run --name zerotier-moon -d -p 9993:9993 -p 9993:9993/udp -v /root/zerotier-one:/var/lib/zerotier-one seedgou/zerotier-moon -4 65.49.206.47 -6 fe80::a8aa:ff:fe0b:7f2e

# get moon id
docker logs zerotier-moon
IPv4 address: 65.49.206.47
IPv6 address: fe80::a8aa:ff:fe0b:7f2e
Your ZeroTier moon id is ccba261347, you could orbit moon using "zerotier-cli orbit ccba261347 ccba261347"

# other commands

docker exec zerotier-moon /zerotier-cli help
docker exec zerotier-moon /zerotier-cli info
docker exec zerotier-moon /zerotier-cli listpeers
docker exec -it zerotier-moon /bin/sh
```

## Client Side

```sh
docker run --device=/dev/net/tun --net=host --cap-add=NET_ADMIN --cap-add=SYS_ADMIN -d -v /var/lib/zerotier-one:/var/lib/zerotier-one --name zerotier-one zerotier/zerotier-containerized


docker exec -it zerotier-one /bin/sh

docker exec zerotier-one /zerotier-cli orbit ccba261347 ccba261347
docker exec zerotier-one /zerotier-cli listpeers
docker exec zerotier-one /zerotier-cli listnetworks


# inside docker instance
cd /var/lib/zerotier-one/
mkdir moons.d
```

