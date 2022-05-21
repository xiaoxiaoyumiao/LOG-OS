# Layers

Layer 是 Unity 中用于 Camera 组件选择性渲染、Light 选择性光照、Raycast 选择性碰撞的层概念，通过 Edit -> Project Settings -> Tags and Layers 可以管理所有的 layer。

GameObject 的 layer 可以在其 Inspector 中配置。

## Layer for Rendering

关于渲染先后时的Layer：通过Sorting Layer和Order in Layer可以设置渲染层级。这两个量可以在Inspector查到。前一个优先级高，相同Layer时order更小的更先被渲染（可以是负数），于是会在画面的底部；后渲染的覆盖先渲染的。在代码中设置sprite renderer的SortingOrder成员变量就相当于修改Order in layer。

理论上z轴越小离摄像机越近，越后渲染；但实际测试似乎不太对劲，可能会产生竞争（可能是因为物体没有开z轴比较？）。目前知道sorting layer和order in layer的优先级是高于z轴的。

## Layer for Collision

- Layer 与选择性 Raycast 碰撞检测

    - Raycast 可以接收一个 layer mask 参数，它是一个整型，其二进制表示中为 1 的位对应的 layer 将被选择参与碰撞检测。例如 `1<<4` 代表与 layer 4 的物体做碰撞检测，`~(1<<4)`则表示不与该层的物体做碰撞检测。

Collision layer check:

```c#
    public LayerMask mask;
         
    void OnCollisionEnter(Collision c){
        if((mask.value & (1<<c.gameObject.layer))!= 0){
            // Do something
        }    
```

- ref: https://answers.unity.com/questions/454494/how-do-i-use-layermask-to-check-collision.html

## References

https://docs.unity3d.com/Manual/Layers.html

https://docs.unity3d.com/ScriptReference/Physics.Raycast.html
        
[https://docs.unity3d.com/Manual/LayerBasedCollision.html](https://docs.unity3d.com/Manual/LayerBasedCollision.html)

[https://blog.csdn.net/lishangke/article/details/100320921](https://blog.csdn.net/lishangke/article/details/100320921)

[https://blog.csdn.net/leansmall/article/details/66478412](https://blog.csdn.net/leansmall/article/details/66478412)

[https://blog.csdn.net/qq\_40306845/article/details/104147384](https://blog.csdn.net/qq\_40306845/article/details/104147384)



