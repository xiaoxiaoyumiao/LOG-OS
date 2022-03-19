# useradd

Add an user on Ubuntu.

```
sudo useradd -s /bin/bash -d /home/newuser/ -m -G sudo newuser
# -s /bin/bash - set bash as login shell of this user
# -d /home/newuser - set /home/newuser as home directory(~) of this user
# -m - create the home directory
# -G sudo - gives admin access
```

See [ssh](../ssh/ "mention") part on installing ssh key pairs for the new user.

## Reference

\[1] [https://www.cyberciti.biz/faq/create-a-user-account-on-ubuntu-linux/](https://www.cyberciti.biz/faq/create-a-user-account-on-ubuntu-linux/)
