# Package

一个 catkin 包（package）对应一个文件夹，这个文件夹的根目录必须包含：

* `package.xml` - 包含包的元数据
* `CMakeLists.txt` - 基于 catkin 的 CMake 格式文件

先前创建的 workspace `catkin_ws` 可以包含多个 catkin 包，每个包对应 `catkin_ws/src` 中的一个文件夹。包之间不能嵌套，但可以有依赖关系。通过以下步骤可以在这个 workspace 中创建一个新的包。

切换当前目录到 `catkin_ws/src` ，调用命令

```text
catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
```

这条命令创建了一个名为 `beginner_tutorials` 的包，它依赖于另外三个包：`std_msgs` ,`rospy` , `roscpp` 。可以观察新生成的包的结构。它的 `package.xml` 文件中包含了作者、license、依赖等信息，可以根据需要来编辑修改。

然后切回 workspace 的根目录 `catkin_ws` ，执行 `catkin_make` 以编译 `src` 目录中的所有包（目前只有新创建的 `beginner_tutorials` ）。

此时会在 workspace 根目录下生成一个 `devel` 目录。（这里 tutorial 提示执行 `devel/setup.bash` 以将 workspace 加入 ROS 环境，但之前已经执行过，尚不清楚此时再执行有何作用）

查询包依赖：

```text
rospack depends1 [package_name] # 一层依赖
rospack depends [package_name] # 递归查找所有依赖
```

## Reference

\[1\] [http://wiki.ros.org/ROS/Tutorials/CreatingPackage](http://wiki.ros.org/ROS/Tutorials/CreatingPackage)

\[2\] [http://wiki.ros.org/ROS/Tutorials/BuildingPackages](http://wiki.ros.org/ROS/Tutorials/BuildingPackages)





