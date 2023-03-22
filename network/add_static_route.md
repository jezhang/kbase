## Linux 添加静态路由

```sh
192.168.50.1(ac86u.ztm.me)
route add -net 192.168.10.0/24 gw 192.168.50.70
route add -net 192.168.123.0/24 gw 192.168.50.70
route add -net 192.168.195.0/24 gw 192.168.50.70

route del -net 192.168.10.0/24 gw 192.168.195.71
route del -net 192.168.123.0/24 gw 192.168.195.72
route del -net 192.168.195.0/24 gw 0.0.0.0

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


您可以尝试在订阅中心更换为其他的订阅地址，选择 SSR 协议，选择应用保持默认，然后在科学上网中尝试订阅。

在软件中心上方的 外部网络 WAN 中，寻找 自动接入互联网 DNS，改成否，并设定 223.5.5.5，只设置这一个，其他的留空，点击保存。然后在科学上网的 DNS 设置修改为基础，并把国内和节点解析的 IP 也设定为 223.5.5.5，国外保持 8.8.8.8 不变。设置好后重启一下您的路由器和光猫，一般就可以正常使用。


下面的节点解析域名修改为 223.5.5.5

科学上网中节点列表可能会显示测试失败，这是正常的，请连接上尝试能否正常打开 google。

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