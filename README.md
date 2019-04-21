Role Name
=========

Install PPTP VPN via Ansible.

Requirements
------------

This role requires Ansible 2.7 or higher and Centos 7 as platform.

Dependencies
------------

None

Example Playbook
----------------

Install PPTP without any users/passwords:

In playbook `pptp-vpn.yml`:

```
- hosts: vpn-servers
  roles:
    - role: pptpd
```

Create users and passwords:

```
ansible-playbook pptp-vpn.yml --extra-vars "@vpn-users.yml"
```

In vars-file `vpn-users.yml`:

```
pptp_users:
  - user: vpnuser
    passwd": "T0p5eCr3T"
  - user: john
    passwd": "P@55w0rd"
```

Note: You can use `--tags users` to only execute user update tasks.

License
-------

WTFPL

Author Information
------------------

**Denis Kadyshev**

- GitHub: @[METAJIJI](https://github.com/METAJIJI)
