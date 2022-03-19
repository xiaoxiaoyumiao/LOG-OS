# Login to Remote with SSH Keys

## Basic

* 以 Linux 环境为例，其他 OS 上过程基本相同。
* 基本运作原理是：通过 ssh-keygen 工具创建一对公私钥，把私钥保存在 local 机器上，把公钥保存在 host 机器上，从 local 登录到远程的 host 时，将私钥位置告知 ssh，ssh 利用给定的私钥完成认证。
* TODO：ssh-agent 自启动
  * [http://mah.everybody.org/docs/ssh\#run-ssh-agent](http://mah.everybody.org/docs/ssh#run-ssh-agent)
  * [https://stackoverflow.com/questions/18880024/start-ssh-agent-on-login](https://stackoverflow.com/questions/18880024/start-ssh-agent-on-login)

```bash
# ~/.ssh is a default directory that SSH looks into.
# Make sure you have one.
mkdir -p ~/.ssh
# restrcit permissions to this directory
chmod 700 ~/.ssh

# create a new key pair
ssh-keygen -t rsa
# 创建时会要求设定私钥的存储路径和一个 passphrase。
# 存储路径不一定要在 .ssh 目录，但在之后 ssh 登录时需要用作参数，所以记好。
# passphrase 相当于给这个私钥的使用再加上一层密码保护。可以为空。
# ssh-keygen 会在给定目录下生成私钥和一个同名但有 pub 后缀的公钥文本文件。

# copy the public key to the cloud server
# remote host 的 ~/.ssh/authorized_keys 是一个文本文件，
# 存储所有许可的公钥。我们需要把新创建的公钥内容添加到这个文件中。
# 可以通过 scp 等直接复制粘贴，也可以使用 ssh-copy-id 工具：
ssh-copy-id -i /path/to/pub-key.pub user@server
# 当然此时仍然需要输入登录 host 的密码。

# 此时你就可以使用 ssh 配合私钥登录服务器了。
# ssh 的 -i 参数接受一个 identity file 的路径，
# 这里的 identity file 也就是我们创建的私钥文件。
ssh -i /path/to/private-key user@server
# 如果设置了 passphrase，此时还需要输入 passphrase。

# 如果觉得每次指定私钥路径和输入 passphrase 过于麻烦，
# 可以使用 ssh-agent 帮助管理公私钥。
ssh-agent $BASH
ssh-add /path/to/private-key
# 在 add 的时候会要求输入一次 passphrase。
# 这样就可以在使用 ssh 登录时省略参数和 passphrase 了。

# 还有一种可以简化 ssh 登录命令的方法，即是使用 config file。
# 这是 ssh 的一种配置文件，其中可包含 host 的地址、登录使用的 identity file 以及
# 更加 advanced 的配置信息，相当于省下了每次登录设置命令行参数的工作。
# 一个典型的 config file 内容如下：
Host myserver
  HostName 123.456.7.89
  User david
  Port 233
  IdentityFile /path/to/private-key

# ssh 的 -F 参数接受一个 config file 的路径，
# 在不指定时默认先寻找用户的配置文件 ~/.ssh/config，再寻找系统全局的配置文件。
# 在建立 config file 后，ssh 登录时就可以不用输入冗长的参数。
# 例如使用上面的配置后，执行 ssh myserver 就可以登录 david@123.456.7.89:233 了。
# 配合 ssh-agent 就可以连 passphrase 的输入也一并省略。
```

## Jump Host

* 有时登录 remote host 时需要经过另一台 host 中转，这一台 host 称为 jump host。ssh 提供了相应的参数以省略反复登录服务器的冗长流程。当然也可以使用 private key 来做到无需输入密码登录。

```bash
# 对于较新版本的 ssh，-J 参数接受一个 jump host 的地址和端口。例如：
ssh -J user1@jumpserver:port user2@targetserver
# 它对应了 config file 里的 ProxyJump 参数。

# 而旧版本的 ssh 需要使用 config file 里的 ProxyCommand 参数来实现转发。
ssh -o ProxyCommand="ssh -W %h:%p host" user2@target
# 这里的 host 是在 config file 中为 jump host 设置的名称，
# 当然要使用用户名加地址也是可以的。

# 同样可以在 config file 中为 remote host 添加 identity file，
# 其路径应当仍设置为在 local 机器上 private key 的路径。
# 注意把私钥放在一个公共服务器上的行为是有风险的。
# 顺便提及，两台 host 其实可以使用相同的 private key。
```

* 踩坑：
  * VS Code Server failed to start:
    * [https://github.com/microsoft/vscode-remote-release/issues/4307](https://github.com/microsoft/vscode-remote-release/issues/4307)
  * VS Code: write to a nonexistent pipe
    * [https://stackoverflow.com/questions/60335069/vscode-remote-connection-error-the-process-tried-to-write-to-a-nonexistent-pipe](https://stackoverflow.com/questions/60335069/vscode-remote-connection-error-the-process-tried-to-write-to-a-nonexistent-pipe)
    * VS Code 的 remote SSH 工具可以使用 ssh 和 config file 实现在编辑器中操作远程服务器的内容，但其默认 ssh 工具实现上有一些问题，在 Windows 上可以安装 OpenSSH 并使用其提供的 ssh 工具来做转发。在配置中可以这样写：

```text
ProxyCommand /path/to/openSSH/ssh.exe -W %h:%p host
```

## Reference

\[1\] [https://upcloud.com/community/tutorials/use-ssh-keys-authentication/](https://upcloud.com/community/tutorials/use-ssh-keys-authentication/)

\[2\] [https://www.cyberciti.biz/faq/linux-unix-ssh-proxycommand-passing-through-one-host-gateway-server/](https://www.cyberciti.biz/faq/linux-unix-ssh-proxycommand-passing-through-one-host-gateway-server/)

\[3\] [https://code.visualstudio.com/docs/remote/troubleshooting](https://code.visualstudio.com/docs/remote/troubleshooting)

\[4\] [https://serverfault.com/questions/827361/ssh-jump-host-without-agent-forwarding](https://serverfault.com/questions/827361/ssh-jump-host-without-agent-forwarding)

\[5\] [https://serverfault.com/questions/934642/ssh-from-a-through-b-to-c-using-private-key-on-a](https://serverfault.com/questions/934642/ssh-from-a-through-b-to-c-using-private-key-on-a)

\[6\] [https://unix.stackexchange.com/questions/494483/specifying-an-identityfile-with-ssh](https://unix.stackexchange.com/questions/494483/specifying-an-identityfile-with-ssh)

\[7\] [https://code.visualstudio.com/blogs/2019/10/03/remote-ssh-tips-and-tricks](https://code.visualstudio.com/blogs/2019/10/03/remote-ssh-tips-and-tricks)

\[8\] [https://www.tecmint.com/access-linux-server-using-a-jump-host/](https://www.tecmint.com/access-linux-server-using-a-jump-host/)

\[9\] [https://blog.csdn.net/weixin\_42096901/article/details/105193366](https://blog.csdn.net/weixin_42096901/article/details/105193366)

\[10\] [https://docs.microsoft.com/zh-cn/windows-server/administration/openssh/openssh\_overview](https://docs.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_overview)

