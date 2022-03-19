# Port Forwarding

将远端端口上的数据转发到本地

```text
ssh -N -f -L localhost:16006:localhost:6006 <user@remote>
```

在 config 文件中可以使用如下的语句：

```text
LocalForward [local_port] [host]:[remote_port]
```

VSCODE 其实有 PORT 转发的配置窗口。

## Reference

\[1\] [https://stackoverflow.com/questions/37987839/how-can-i-run-tensorboard-on-a-remote-server](https://stackoverflow.com/questions/37987839/how-can-i-run-tensorboard-on-a-remote-server)

