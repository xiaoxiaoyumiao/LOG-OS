# Write Subscriber/Publisher

## Publisher Template

```python
# 必须依赖 rospy
import rospy
# 导入 Publisher 所需的消息类型
from std_msgs.msg import String

def talker():
    # 构造 Publisher 将创建一个 topic
    # 此处 topic name 为 chatter，消息类型为 String
    # queue_size 设置了网络拥塞时的队列大小
    pub = rospy.Publisher('chatter', String, queue_size=10)
    # init_node 方法初始化本进程（节点）
    # 这里定义 node name 为 talker
    # anonymous 参数允许多个 talker 节点存在并自动在名字后添加数字以区分
    # 本语句和 publisher 构造语句可以互换位置
    rospy.init_node('talker', anonymous=True)
    # 构造 Rate 实例以控制 publish 频率
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        # 发布
        pub.publish(hello_str)
        # 控制频率，此处也可以用 rospy.sleep(time)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
```

## Subscriber Template

```python
#!/usr/bin/env python
import rospy
# 导入 Subscriber 需要的消息类型
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    # 构造 Subscriber
    # 这里设置其订阅的 topic 为前面创建的消息类型为 String 的 chatter
    # 同时设定了消息到达时的回调函数
    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
```

## Build & Run

编译和往常一样在 workspace 执行 catkin make 即可。运行：

```text
rosrun [package_name] [python_file_name] [args]

# example:
rosrun beginner_tutorials talker.py
```

## Reference

\[1\] [http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)

