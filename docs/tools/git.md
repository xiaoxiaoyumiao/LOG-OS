# Git

* 传输文件过大时可能会因缓存不够而中断连接：
  * [https://stackoverflow.com/questions/6842687/the-remote-end-hung-up-unexpectedly-while-git-cloning](https://stackoverflow.com/questions/6842687/the-remote-end-hung-up-unexpectedly-while-git-cloning)
* 如何 clone 单个分支的内容：
  * `git clone --single-branch --branch <branchname> <remote-repo>` 可以拉取 url 为 \<remote-repo> 的  \<branch\_name> 分支
  * ref: [https://stackoverflow.com/questions/1911109/how-do-i-clone-a-specific-git-branch](https://stackoverflow.com/questions/1911109/how-do-i-clone-a-specific-git-branch)
* cherry-pick
  * 将来自其他分支的单个 commit 的修改应用于分支。
