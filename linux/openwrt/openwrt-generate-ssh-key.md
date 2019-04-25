### Generate SSH Keys
Dropbear uses a special format to store its keypairs.

1. Generate Keypair
```
dropbearkey -t rsa -f ~/.ssh/id_rsa
```
1. Show Public Key
```
dropbearkey -y  -f ~/.ssh/id_rsa | grep '^ssh-rsa'
```

### Connect to a Machine using the Public Key
```
ssh user@host -i ~/.ssh/id_rsa
```