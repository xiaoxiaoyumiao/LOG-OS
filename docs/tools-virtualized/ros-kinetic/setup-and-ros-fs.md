# Setup & ROS FS

## Setup

因为是直接从 `adacomplab/ros_kinetic` 这个 docker image 开始配置，所以不记录从 Ubuntu 开始装 ROS 的步骤了。

在本地创建一个 `catkin_ws` 文件夹，运行 docker image 时使用如下命令，把本地的 `catkin_ws` 挂载到  docker 中的 `catkin_ws` 目录，这个目录将会是我们的 workspace。

```bash
docker run -p 6080:80 \
 --mount type=bind,source="$(pwd)"/catkin_ws,target=/root/catkin_ws \
 adacomplab/ros_kinetic
```

启动后打开一个 shell，在 shell 中执行：

```text
source /opt/ros/kinetic/setup.bash
```

这个脚本负责为 catkin 做环境初始化。catkin 是 ROS 中类似 CMake 一样的东西，用来组织和编译项目。每次打开新的 shell 时都需要执行这条命令。（不过这个 image 的 .bashrc 中已经添加了这条命令，其实不需要再手动执行了。）

下面初始化我们的 workspace：

```text
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```

`catkin_make` 工具会完成项目的初始化工作，包括但不限于在 src 文件夹中创建一个 `CMakeList.txt` 文件，以及产生 `build` 和 `devel` 两个新文件夹。

此时可以注意一下 `ROS_PACKAGE_PATH` 变量的内容：

```text
echo $ROS_PACKAGE_PATH
/opt/ros/kinetic/share
```

执行 `devel` 文件夹中的 `setup.bash` 文件，它和前面执行的 `setup.bash` 的内容似乎没有不同，不过它可以更新当前工作的环境。再次打印 `ROS_PACKAGE_PATH` 变量：

```text
echo $ROS_PACKAGE_PATH
/root/catkin_ws/src:/opt/ros/kinetic/share
```

可以看到新创建的 src 目录被加入了 PATH 变量。这个变量就是 ROS 包管理的环境变量，例如接下来介绍的各个 FS 命令就依赖于这个变量。

## File System

官方提供了一个教学用的包，帮助熟悉 ROS FS 相关的各种命令：

```text
sudo apt-get install ros-<distro>-ros-tutorials
```

首先 `rospack` 可以用来管理包。`rospack find` 命令可以用来查找一个 ROS 包的路径：

```text
rospack find roscpp
```

`roscd` 可以快捷地跳转到某个包的目录或子目录：

```text
usage:
roscd <package-or-stack>[/subdir]
example:
roscd roscpp
roscd log # where ROS store all log files
```

`rosls` 可以快捷地展示某个包的目录或子目录的内容：

```text
usage:
rosls <package-or-stack>[/subdir]
example:
rosls roscpp_tutorials
```

和熟悉的 cd 或 ls 工具一样，这些命令都可以使用 tab 补全。此外，它们都只能查找 `ROS_PACKAGE_PATH` 包含的路径。

## Reference

\[1\] [http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)

\[2\] [http://wiki.ros.org/ROS/Tutorials/NavigatingTheFilesystem](http://wiki.ros.org/ROS/Tutorials/NavigatingTheFilesystem)

