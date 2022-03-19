# tmux

* 方便地实现连接与进程解耦的程序
  * [https://www.ruanyifeng.com/blog/2019/10/tmux.html](https://www.ruanyifeng.com/blog/2019/10/tmux.html)
  * [https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/)

```text
# 直接运行 tmux 就可以创建一个新的会话
tmux
# tmux 的命令都需要一个共同的前缀，默认是 ctrl+B。前缀可以自定义。
# ctrl+B 后通过 page up/down 可以正常 scroll 窗口，通过 esc 退出。
# ctrl+D 删除当前会话。
# ctrl+B D 可以 detach 当前会话。
# 查看当前运行的会话，通过 tmux 命令直接创建的会话默认带有序号作为 session name
tmux ls
# 会话可以被重命名
tmux rename-session -t [original_name] [new_name]
# 当前窗口 attach 到一个正在运行的会话
tmux attach -t [session_name]
# 手动删除一个会话
tmux kill-session -t [session_name]
```

