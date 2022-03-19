# Write Server/Client

## Server Template

```python
#!/usr/bin/env python

from __future__ import print_function

# 导入所需的 service 和 response 类型
from beginner_tutorials.srv import AddTwoInts,AddTwoIntsResponse
import rospy

def handle_add_two_ints(req):
    '''
    request 到达时的回调函数
    构造了一个 response 对象并返回
    '''
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    # Node 初始化
    rospy.init_node('add_two_ints_server')
    # 构造 Service
    # 这里将其命名为 add_two_ints，服务类型为 AddTwoInts
    # 同时设定了 request 到达时的回调函数
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")
    
    # 就是 spin
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
```

## Client Template

```python
#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import AddTwoInts,AddTwoIntsResponse

def add_two_ints_client(x, y):
    # 阻塞等待名为 add_two_ints 的 server 出现
    rospy.wait_for_service('add_two_ints')
    try:
        # 构造服务的一个 proxy，从而可以像普通函数一样调用
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        # 调用 proxy，得到 response
        resp1 = add_two_ints(x, y)
        # 取结果（sum 为 response 结构中储存计算结果的属性名）
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s+%s"%(x, y))
    print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))
```

## Build & Run

编译和往常一样在 workspace 执行 catkin make 即可。运行：

```text

rosrun [package_name] [python_file_name] [args]
# example:
rosrun beginner_tutorials add_two_ints_server.py
rosrun beginner_tutorials add_two_ints_client.py 1 3
```

