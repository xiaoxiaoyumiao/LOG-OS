# Basics

## Basic Concepts & Commands

* 容器/container
  * 是一个与所在机器，或者说 host 的其他所有进程独立的进程
  * 拥有自己独立的文件系统，这一系统由镜像/image 提供。
* 镜像/image
  * 镜像为文件与 meta data 的集合
  * 镜像分层，每层可以修改文件成为新的镜像
  * 不同镜像可共享相同的层 /layout
  * 只读
  * 所有镜像构成树（森林），一个镜像依赖的父节点由 Dockerfile 的 FROM 声明。特别地，无依赖的镜像为 FROM scratch
* Dockerfile
  * Dockerfile 文件描述了一个 image 如何被构建。如果你拥有一个 Dockerfile，就可以在它所在目录下运行 `docker build .` ，这个命令会在当前目录下查找名为 Dockerfile （注意是大小写敏感的）的文件并执行文件中描述的构建动作。
  * 简要介绍 Dockerfile 可包含的构建动作。如上所述，FROM 会定义这个 image 依赖的 image，构建时会拉取其依赖。RUN 会执行一个给定的指令。CMD 指定 container 在这个 image 上运行的默认指令。
  * 可以在 build 时带上参数`-t <tag>` 来赋予 image 一个 human readable 的 name。之后执行 run 之类的指令就可以用这个 name 作为参数。
* Docker Dashboard
  * 一个用来方便地浏览和操作当前拥有的 Containers/Apps、Images 的界面
  * 任务栏图标右键菜单中选择 Dashboard 即可运行
* 关于 Getting Started 中做的事情
  * `docker run <image_name>` will first create a container layer over specified image, and then starts it using the specified command.
    * `-d` 参数使得创建的 container 在 detached mode（后台）运行，`-p` 可以在指定的 host 端口和 container 端口之间建立映射。
    * `-w <directory>` 可以指定 specified command 的执行路径，即 working directory。
  * `docker ps -a` 可以查看当前所有建立的 container
  * `docker rm <container_name>` 可以删除一个已经建立的 container
    * 也可以使用 container ID（使用 ps 指令可以看到）来指定 container，并且只需要输入部分位数，docker 会寻找匹配结果
    * 一个处于 running 状态的 container 是无法通过 `rm` 删除的，需要先停止或通过加 `-f` 来删除。
  * `docker stop <container_name>` 可以停止运行一个正在运行的 container
  * `docker login -u <user_name>` 可以在本地命令行登陆 Docker Hub，从而执行远程相关操作
  * `docker tag` 可以为一个 image 添加新的名称（类似一个 URL 重定向？） 
  * `docker push <image_name>` 可以把一个本地的 image 推送到远端同名 repo
* Container Volumes
  * container 可以通过 volume 将它的文件系统中特定的路径关联到 host 的路径，从而实现 container 的数据持久化。
  * named volumes 由 docker 维护存储，从而只需要通过 volume 的名字来操作它们。
  * `docker volme create <volume_name>` 可以创建一个指定名字的 named volume。
  * `docker run` 的 `-v <volume_name>:<file_system_path>` 可以把一个 named volume mount 到 docker 的文件系统的指定路径上。
  * 使用 `docker volume inspect <volume_name>` 可以看到 named volume 的信息，包括它的实际存储位置。
  * bind mount 则由 docker 使用者维护，这一种 volume 的存储路径可以自由指定，常用于和 container 进行数据交换。例如，把本地的代码 mount 到 container 上。

## Reference

docker 文档 [https://docs.docker.com/reference/](https://docs.docker.com/reference/)

docker基础知识 [https://yq.aliyun.com/articles/734130?spm=5176.12281978.0.0.37722232dFdRyd](https://yq.aliyun.com/articles/734130?spm=5176.12281978.0.0.37722232dFdRyd)

关于Dockerfile [https://yq.aliyun.com/articles/735190?spm=5176.12281978.0.0.37722232dFdRyd](https://yq.aliyun.com/articles/735190?spm=5176.12281978.0.0.37722232dFdRyd)

\[1\] [https://docs.docker.com/desktop/dashboard/](https://docs.docker.com/desktop/dashboard/)



