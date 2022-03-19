# Nodes, Topics, Services & Parameters

## Nodes

节点（node） 是 ROS 中的基本概念，大体上相当于一个进程。

作为示例，安装如下教程包：

```text
sudo apt-get install ros-kinetic-ros-tutorials
```

在运行 ROS 程序之前，首先启动 `roscore` 。它是 ROS 的内核或者说服务端。

管理 node 的工具是 `rosnode` 。

```text
rosnode list # 列出当前运行的所有 node。
             # 仅 roscore 运行时，执行结果是 /rosout。这是一个负责输出的 node。
rosnode info [node_name] # 查询一个 node 的属性。
    # 执行可以看到 node 的 publications、subscriptions、 services 等。
    # 这些属性代表了 node 与其他 node 的通信关系。
    
rosnode ping [node_name] # ping 一个节点
```

运行 node 的工具是 `rosrun` 。事实上 `rosrun` 的效果和直接运行节点对应的可执行文件并没有什么区别，其主要作用就是可以不用知道包和可执行文件的具体位置。后文使用 python 编写节点时也会看到 `rosrun some_package some_node.py` 这样的语句，和直接调用 python 解释器运行脚本的效果是一样的。（ref: \[5\]）

```text
rosrun [package_name] [node_name] # 运行某个包中的某个节点。例如：
rosrun turtlesim turtlesim_node # 运行经典的小乌龟例程
rosrun [package_name] [node_name] __name:=[new_name] # 以其他名字运行节点
    # 它会改变执行 rosnode list 时看到的节点名。
```

## Topics

话题（topic）是节点间的一种通信方式。以 turtlesim 为例，执行如下命令：

```text
roscore # 启动内核
# in a new terminal:
rosrun turtlesim turtlesim_node # 运行小乌龟节点
# in a new terminal:
rosrun turtlesim turtle_teleop_key # 运行交互节点
```

运行 `turtle_teleop_key` 后，该节点从 shell 接收用户的方向键输入，并将输入信息传递给小乌龟，让小乌龟可以旋转和移动。信息是通过一个 topic 实现传递的。交互节点向这个 topic 发布（publish）信息，小乌龟节点则订阅（subscribe）这个 topic 的信息，从而可以接收交互节点发布的信息。

一个节点发布与订阅的对象可以在前文提到的 `rosnode info` 中看到。此外，也可以通过 `rqt_graph` 工具可视化。

```bash
# installation
sudo apt-get install ros-<distro>-rqt
sudo apt-get install ros-<distro>-rqt-common-plugins
# run
rosrun rqt_graph rqt_graph
```

运行该工具将弹出一个窗口，显示当前活跃的节点及话题。如果两个节点正在通过一个话题通信，那么就会有一条有向边从发布者指向订阅者，边上带有话题本身的名字。

使用 `rqt_plot` 工具可以将话题中的数据可视化。

```bash
# run
rosrun rqt_plot rqt_plot
```

运行该工具将弹出一个窗口，包含了一个波形显示用的坐标系。在上方的 Topic 输入框中输入话题名（例如 `/turtle1/pose/x` 发布小乌龟的 x 坐标信息），点击 + 号，其值就会在波形图中实时显示。

使用 rostopic 工具可以管理话题。

```bash
rostopic -h # 显示使用指南

rostopic bw     display bandwidth used by topic
rostopic echo   print messages to screen
rostopic hz     display publishing rate of topic    
rostopic list   print information about active topics
rostopic pub    publish data to topic
rostopic type   print topic type

# 部分示例
rostopic echo [topic_name] # 打印话题中发布的信息
rostopic echo /turtle1/cmd_vel # 将在用户按下方向键时打印作用于小乌龟的命令信息
# echo 命令会创建该话题的新的临时订阅者，这可以通过 rqt_graph 看到。

rostopic list -v 打印当前的所有话题

rostopic type [topic_name] # 打印一个话题中数据的类型
rostopic type /turtle1/cmd_vel # geometry_msgs/Twist
# 使用 rosmsg 工具可以查看这一类型的定义
rosmsg show geometry_msgs/Twist
# 以下是其输出
geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z
# 可以看到它包含了对切向和法向运动的描述信息。

rostopic pub [topic_name] [msg_type] [args] # 向话题发布信息
rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist \
    -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
# 这一命令创建了一个同时包含切向和法向运动的 Twist 类型数据，并发送给 cmd_vel 话题。
# -1 参数代表 rostopic 发布这一条信息后便退出。
# -- 的作用是提示其后的部分不能解析为 option。(ref: [1])
# 这里的参数值采用了 YAML 格式。大体上类似于 Python 里的值表示。
# 希望 rostopic 循环执行，可以使用 -r 参数。
# 下面的命令以 1Hz 发布 Twist，使得小乌龟可以持续做圆周运动。
rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 1 \
    -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]'
# pub 会创建该话题的新的临时发布者，这可以通过 rqt_graph 看到。

rostopic hz [topic_name] # 实时测量话题中数据产生的速率
```

## Services

服务（service）是另一种节点间通信方式。它是基于请求（ request）和响应（response）工作的。实际使用时类似函数调用。

使用 rosservice 工具可以对服务进行管理。

```bash
# common usage
rosservice list         print information about active services
rosservice call         call the service with the provided args
rosservice type         print service type
rosservice find         find services by service type
rosservice uri          print service ROSRPC uri

rosservice list # 列举所有

rosservice type [service] # 查询一个服务的类型（类似于函数签名）
# 小乌龟节点提供了 /spawn 服务
rosservice type /spawn # turtlesim/Spawn
# 使用 rossrv 工具可以查看这一服务类型（需要的参数类型和返回值类型）
rossrv show turtlesim/Spawn

rosservice call [service] [args] # 调用一个服务
# 在小乌龟节点运行时，调用其 /clear 服务会清空当前画板
rosservice call /clear 
# 调用 /spawn 创建一个新的小乌龟，各服务参数含义可对照 rossrv show 结果查看
rosservice call /spawn 2 2 0.2 "" # 名字由节点自己设置为默认值
# 服务的响应会作为这一命令的结果打印出来

```

## Parameter Server

一种更直接地读写节点中参数（parameter）配置的机制。使用 rosparam 工具可以管理参数。和前面的各种传参命令一样，它的参数值表示都是基于 YAML 格式的。

```bash
rosparam set            set parameter
rosparam get            get parameter
rosparam load           load parameters from file
rosparam dump           dump parameters to file
rosparam delete         delete parameter
rosparam list           list parameter names

# 查询所有 parameter name
rosparam list

# set & get
rosparam set [param_name]
rosparam get [param_name]
# 在小乌龟例程中，修改参数后需要调用 /clear 使之生效

# dump & load，namespace 省略时默认为全局 namespace
rosparam dump [file_name] [namespace]
rosparam load [file_name] [namespace]
```

## Reference

\[1\] 关于命令行参数中 -- 的作用：

> -- A -- signals the end of options and disables further option processing. Any arguments after the -- are treated as filenames and arguments. An argument of - is equivalent to --.
>
> ref: [https://www.man7.org/linux/man-pages/man1/bash.1.html](https://www.man7.org/linux/man-pages/man1/bash.1.html)

\[2\] [http://wiki.ros.org/ROS/Tutorials/UnderstandingNodes](http://wiki.ros.org/ROS/Tutorials/UnderstandingNodes)

\[3\] [http://wiki.ros.org/ROS/Tutorials/UnderstandingTopics](http://wiki.ros.org/ROS/Tutorials/UnderstandingTopics)

\[4\] [http://wiki.ros.org/ROS/Tutorials/UnderstandingServicesParams](http://wiki.ros.org/ROS/Tutorials/UnderstandingServicesParams)

\[5\] [https://answers.ros.org/question/339462/what-does-rosrun-do-internally/](https://answers.ros.org/question/339462/what-does-rosrun-do-internally/)

