# WSL

## Installation

{% embed url="https://docs.microsoft.com/zh-cn/windows/wsl/install-win10" caption="" %}

## Miscellaneous

* chmod 命令对（windows 文件系统中的）文件不起作用
* 解决：在 `/etc/wsl.conf` （如果没有则创建）中增加如下内容：

```text
[automount]
options = "metadata"
```

* 然后在 PowerShell 中执行 `wsl --shutdown` ，重新打开 wsl 命令行时 chmod 即生效
* ref: [https://stackoverflow.com/questions/46610256/chmod-wsl-bash-doesnt-work](https://stackoverflow.com/questions/46610256/chmod-wsl-bash-doesnt-work)

