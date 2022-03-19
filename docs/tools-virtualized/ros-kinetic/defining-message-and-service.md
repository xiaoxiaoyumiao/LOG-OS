# Defining Message & Service

## Message Definition

每个 message 被一个 msg 文件描述。 msg 文件是字符串文本文件，每行描述一个域，一个域的描述包含其类型和名字。类型可取的值如下：

```
int8, int16, int32, int64 (plus uint*)
float32, float64
string
time, duration
other msg files # 也就是其他 msg 文件的名字
variable-length array[] and fixed-length array[C]
```

习惯上自定义消息类型似乎都是大写开头。

例如，定义一个`Point.msg` 文件以描述 2D 坐标类型的 Message：

```
float64 x
float64 y
```

它包含了类型为 64 位浮点数的 x, y 坐标。进而可以定义一个 `Waypoints.msg` 文件以描述一条路径包含的多个点：

```
Point[] points
```

它定义了一个 Point 类型的数组。

如先前章节所述，查询消息类型可通过 `rosmsg show` 命令实现。

```
rosmsg show [[package_name/]message_type_name]
# 例如前文使用过的：
rosmsg show geometry_msgs/Twist
```

包名可以省略。

```
rosmsg show Twist

# output:

[geometry_msgs/Twist]:
geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z

```

## Service Definition

每个 service 被一个 srv 文件定义。srv 文件是字符串文本文件，描述请求和响应的格式，之间用划线分隔。看例子更快：

```
int64 A
int64 B
---
int64 Sum
```

这个服务的请求包含两个 64 位整型，响应则为一个 64 位整型。

如先前章节所述，查询服务类型可通过 `rossrv show` 命令实现。

```bash
rossrv show turtlesim/Spawn
```

## Configurations

为了从 msg 或 srv 文件中编译出可执行程序，需要在 package.xml 中添加如下引用：

```
 <build_depend>message_generation</build_depend>
  <exec_depend>message_runtime</exec_depend>
```

同时，需要在其 CMakeLists.txt 文件中做如下修改。

1. 添加对 `message_generation` 的构建依赖：

```
find_package(catkin REQUIRED COMPONENTS
   roscpp
   rospy
   std_msgs
   message_generation
)
```

2\. 添加对 `message_runtime` 的运行时依赖：

```
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES planner
  CATKIN_DEPENDS message_runtime
#  DEPENDS system_lib
)
```

3\. 对于自定义消息，添加对自定义的 msg 文件的依赖（这一部分可以在自动生成的 CMakeLists.txt 的注释中找到）：

```
add_message_files(
  FILES
  Message1.msg
  Message2.msg
)
```

对于自定义服务，添加对自定义的 srv 文件的依赖，同样可以在注释中找到：

```
add_service_files(
  FILES
  Service1.srv
  Service2.srv
)
```

4\. 最后，写明对 `generate_messages` 的调用。这一函数同样可以在注释中找到，将其取消注释即可：

```
generate_messages(
  DEPENDENCIES
  std_msgs
)
```

完成以上配置后，在 workspace 根目录做一次 catkin make 即可完成编译。编译器将从描述文件生成可供不同语言引用的 header 或 package。

> The C++ message header file will be generated in \~/catkin\_ws/devel/include/beginner\_tutorials/. The Python script will be created in \~/catkin\_ws/devel/lib/python2.7/dist-packages/beginner\_tutorials/msg. The lisp file appears in \~/catkin\_ws/devel/share/common-lisp/ros/beginner\_tutorials/msg/.
