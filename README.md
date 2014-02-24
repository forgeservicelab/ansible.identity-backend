# Identity backend

This repo contains playbook for identity backend. It will install openldap and the root domain entry in the LDAP tree.

In future, it will also install some web interface.

## Usage

1. Get a virtual machine, find out its public IP, get the IP to inventory. Simple inventory can be
```
[dev_machines]
193.166.1.18
```
2. Get the roles. First create directory called roles and then download the roles to it. See the main yml file for where to get the roles.


Then run the main playbook on the machine:
```
$ ansible-playbook -v identity.yml -e h=193.166.1.18
```


