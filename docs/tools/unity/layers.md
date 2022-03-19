# Layers

可以用来对碰撞体分组。

[https://docs.unity3d.com/Manual/LayerBasedCollision.html](https://docs.unity3d.com/Manual/LayerBasedCollision.html)

[https://blog.csdn.net/lishangke/article/details/100320921](https://blog.csdn.net/lishangke/article/details/100320921)

关于渲染先后时的Layer：通过Sorting Layer和Order in Layer可以设置渲染层级。这两个量可以在Inspector查到。前一个优先级高，相同Layer时order更小的更先被渲染（可以是负数），于是会在画面的底部；后渲染的覆盖先渲染的。在代码中设置sprite renderer的SortingOrder成员变量就相当于修改Order in layer。

理论上z轴越小离摄像机越近，越后渲染；但实际测试似乎不太对劲，可能会产生竞争（可能是因为物体没有开z轴比较？）。目前知道sorting layer和order in layer的优先级是高于z轴的。

关于不同layer的介绍：

[https://blog.csdn.net/leansmall/article/details/66478412](https://blog.csdn.net/leansmall/article/details/66478412)

[https://blog.csdn.net/qq\_40306845/article/details/104147384](https://blog.csdn.net/qq\_40306845/article/details/104147384)

