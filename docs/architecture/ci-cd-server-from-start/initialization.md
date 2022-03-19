# Initialization

* [https://www.howtogeek.com/117435/htg-explains-the-linux-directory-structure-explained/](https://www.howtogeek.com/117435/htg-explains-the-linux-directory-structure-explained/)
* 初始包含的工具包（仅列出常用工具）：
  * apt - 包管理工具
  * bash - 命令行工具
  * bzip2 & gzip & tar - 压缩工具
  * gcc - C 编译工具
  * mawk - 基于模式匹配的文本处理工具
  * python2.7 & python3.7
  * sed - 基于流的文本处理工具
  * vi - 文本编辑器
  * wget - 下载工具
* 安装的工具包：
  * curl
  * sudo
  * vim
  * git + fix-broken
* docker
  * [https://docs.docker.com/engine/install/debian/\#prerequisites](https://docs.docker.com/engine/install/debian/#prerequisites)
* gitlab-runner
  * [https://docs.gitlab.com/runner/install/linux-manually.html](https://docs.gitlab.com/runner/install/linux-manually.html)
  * sbin 目录中包含一些和系统相关、运行存在危险的可执行文件，一般不在用户的 PATH 中
  * [https://unix.stackexchange.com/questions/232782/is-there-a-reason-i-would-not-add-usr-local-sbin-usr-sbin-sbin-to-my-path-o](https://unix.stackexchange.com/questions/232782/is-there-a-reason-i-would-not-add-usr-local-sbin-usr-sbin-sbin-to-my-path-o)
  * 查看 /etc/profile 可以看到 PATH 初始化的默认操作
  * su 登录 root 时需要加上 --login 参数使得 sbin 被添加到 PATH 中
  * [https://unix.stackexchange.com/questions/466373/setting-the-root-path-for-su](https://unix.stackexchange.com/questions/466373/setting-the-root-path-for-su)
* register a runner
  * [https://docs.gitlab.com/runner/register/](https://docs.gitlab.com/runner/register/)
* keil C51 无法在 linux 上运行，windows docker 映像无法在 linux 上运行，考虑虚拟机
  * 服务器 CPU 不支持虚拟化

