# Identity backend

This repo contains playbook for identity backend. It will install openldap and the root domain entry in the LDAP tree.

In future, it will also install some web interface.

## Usage

Get a virtual machine, find out its public IP, get the IP to inventory. Simple inventory can be
```
[dev_machines]
193.166.1.18
```

Then run the main playbook on the machine:
```
$ ansible-playbook -v identity.yml -e h=193.166.1.18
```


