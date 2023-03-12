## Linux 添加静态路由

```sh
192.168.50.1(ac86u.ztm.me)
route add -net 192.168.10.0/24 gw 192.168.195.71
route add -net 192.168.123.0/24 gw 192.168.195.72

192.168.10.1(route@home.ztm.me)
route add -net 192.168.50.0/24 gw 192.168.10.70
route add -net 192.168.195.0/24 gw 192.168.10.70
route add -net 192.168.123.0/24 gw 192.168.10.70

192.168.10.70(macmini2014late)
sudo route add -net 192.168.50.0/24 gw 192.168.195.10
sudo route add -net 192.168.123.0/24 gw 192.168.195.72


192.168.123.1(route@wjjhome)
route add -net 192.168.50.0/24 gw 192.168.123.70
route add -net 192.168.195.0/24 gw 192.168.123.70
route add -net 192.168.10.0/24 gw 192.168.123.70

192.168.123.70(datang mini computer)
sudo route add -net 192.168.50.0/24 gw 192.168.195.10
sudo route add -net 192.168.10.0/24 gw 192.168.195.71

macmini2014late
sudo iptables -I FORWARD -i zt7nnngyti -j ACCEPT
sudo iptables -I FORWARD -o zt7nnngyti -j ACCEPT
sudo iptables -t nat -I POSTROUTING -o zt7nnngyti -j MASQUERADE
#其中的 ztyqbub6jp 在不同的机器中不一样，你可以在路由器ssh环境中用 zerotier-cli listnetworks 或者 ifconfig 查询zt开头的网卡名
sudo iptables-save #保存配置到文件,否则重启规则会丢失.
```