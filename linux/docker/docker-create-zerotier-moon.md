
### Docker create ZeroTier moon
<https://hub.docker.com/r/seedgou/zerotier-moon/>
```sh
docker run --name zerotier-moon -d --restart always -p 9993:9993/udp seedgou/zerotier-moon -4 140.252.10.1

docker logs zerotier-moon
docker exec zerotier-moon /zerotier-cli info
```

### ZeroTier One for container-oriented distributions like CoreOS
<https://hub.docker.com/r/zerotier/zerotier-containerized/>

```sh
docker run --device=/dev/net/tun --net=host --cap-add=NET_ADMIN --cap-add=SYS_ADMIN -d -v /var/lib/zerotier-one:/var/lib/zerotier-one --name zerotier-one zerotier/zerotier-containerized


docker exec zerotier-one /zerotier-cli join 8056c2e21c000001
docker exec zerotier-one /zerotier-cli orbit 0a2f8d1f33 0a2f8d1f33
docker exec zerotier-one /zerotier-cli info
```
