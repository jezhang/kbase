```sh
docker run -d --restart=unless-stopped --name kasmweb -p 6901:6901 -e VNC_PW=password -e LANG=zh_CN.UTF-8 -e LANGUAGE=zh_CN:zh -e LC_ALL=zh_CN.UTF-8 -v /root/data/kasmweb:/home/kasm-user/shares --shm-size=1024m kasmweb/desktop:1.14.0

# kasmweb/ubuntu-jammy-desktop:1.14.0
# kasmweb/desktop:1.14.0
```
