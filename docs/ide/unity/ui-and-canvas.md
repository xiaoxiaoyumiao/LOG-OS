# UI & Canvas

脚本中需要`using UnityEngine.UI`

可以通过 gameObject - UI 对游戏对象添加UI组件，添加以后会自动在该对象下建立一个canvas类型的子对象，然后在这个canvas对象下建一个UI对象。canvas子对象可以有多个。

## 不同的Canvas模式

这里要记录一下Canvas的三种渲染方式：

1. Screen Space - Overlay
   1. 这种渲染模式表示 Canvas 下的所有的 UI 控件永远位于屏幕的前面 , 不管有没有相机 , UI元素永远在屏幕最前面 ，主要是2D效果。
2. Screen Space - Camera
   1. 这种渲染模式 Canvas 和 摄像机之间有一定的距离 , 可以在摄像机和 Canvas 之间播放一些粒子特效，主要是3D效果。
3. World Space
   1. 这种模式下 Canvas 就和普通的 3D 物体一样了 , 可以控制它的大小,旋转,缩放等 , 一般用来做血条。
   2. 注意！Canvas做Prefab子物体的情况下千万不要动Canvas的位置和大小，否则场景中UI子物体的位置并不会和Prefab编辑时看到的同步；此外如果显示不正常或者直接消失，先注意修改一下Canvas的Pixels per unit，这个太大可能会导致UI物体过于模糊或者溢出屏幕

Image：遮罩可以使用 Mask 组件。具有 Mask 组件的 Image 会成为其子 Image 的遮罩，即只显示子 Image 落在 Mask Image 的非透明区域内的部分。遮罩的策略可以设置，如没有子 Image 的位置是否显示 Mask Image 的内容。

```csharp
 // Label 定制字体
 GUIStyle titleStyle2 = new GUIStyle();
            titleStyle2.fontSize = 20;
            titleStyle2.normal.textColor = new Color(46f/256f, 163f/256f, 256f/256f, 256f/256f);
            GUI.Label(new Rect(Screen.width / 2 - 70, Screen.height / 2 -30, 100, 30), "是否覆盖已有关卡？", titleStyle2);
```

```csharp
Toolbar
​
  toolbarInt = GUI.Toolbar(new Rect(30, 250, 250, 30), toolbarInt, new string[] { "功能一", "功能二", "功能 三" });
        if (lastValue != toolbarInt)
        {
            if (toolbarInt == 0)
                Debug.Log(1111);
            if (toolbarInt == 1)
                Debug.Log(2222);
            if (toolbarInt == 2)
                Debug.Log(3333);
            lastValue = toolbarInt;
        }
————————————————
版权声明：本文为CSDN博主「电达」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u011480667/article/details/77542226
```

## 对话框实现

其实还是比较简单和灵活的，可以参考的思路：

[http://blog.sina.com.cn/s/blog\_149e762dc0102w308.html](http://blog.sina.com.cn/s/blog_149e762dc0102w308.html)

[https://blog.csdn.net/u010989951/article/details/75096153?locationNum=2&fps=1](https://blog.csdn.net/u010989951/article/details/75096153?locationNum=2&fps=1)

[https://www.cnblogs.com/2Yous/p/5079965.html](https://www.cnblogs.com/2Yous/p/5079965.html)（异常时的系统对话框，应该属于C\#库？）

## Panel

很有用的UI组件容器。其depth在决定层级时优先级很高。可以添加GridLayoutGroup之类的Component来layout内部的元素。

## Canvas的分辨率

图片资源有一个 pixel per unit 属性表示图片的多少像素等于一个 unity 单位。

同时， Canvas 中的 Scale mode 为 stant pixel size 时，scale factor 和 reference pixels per unit 可以控制绘制的尺寸（后一个属性作用尚不明确）

