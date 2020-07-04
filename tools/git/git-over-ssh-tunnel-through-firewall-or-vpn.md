
Git over an ssh tunnel (like through a firewall or VPN)
=======================================================

Rerfer to <https://randyfay.com/content/git-over-ssh-tunnel-through-firewall-or-vpn>


```sh
ssh -L3333:github.com:22 root@my-vps.com -p22
git clone ssh://git@localhost:3333/jezhang/kbase.git

```