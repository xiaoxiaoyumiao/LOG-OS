# Camera

* 场景中有一个唯一的主摄像机，可以通过`Camera.main`来获取。是第一个具有main Camera的tag的相机。
* 摄像机的transform的位置也是世界坐标系的位置。
* 摄像机按照深度depth决定先后顺序，depth较大的摄像机的画面会渲染在depth较小的上面。
* Clear Flags决定当摄像机如何填充没有物体影像的部分。默认一般是天空盒或者纯色，但是可以替换成Depth only（从而把这部分画面留给小depth的摄像机）。
* culling mask决定摄像机捕捉哪些内容。所有物体都有一个Layer的属性，默认一般是Default。设置这个mask可以让摄像机只捕捉一部分Layer中的物体的影像。
* Projection决定视角，有透视和正交两种，透视时就是3D，正交时就是2D。
* Viewport Rect决定摄像机渲染出的画面（视口Viewport）相对整个屏幕的位置和尺寸，采用视口坐标系。
* Camera可以通过设置Target texture来把结果渲染到材质上，利用这一点可以实现小地图、画中画等等。新建一个Texture，然后把它赋值给target texture即可。计算和做坐标转换时（大概）可以把这个texture类比成屏幕screen。
* 小地图的制作：[https://blog.csdn.net/wuming22222/article/details/37526659](https://blog.csdn.net/wuming22222/article/details/37526659)
* 关于size和尺寸换算的问题：[https://blog.csdn.net/lezhi\_/article/details/78827549](https://blog.csdn.net/lezhi_/article/details/78827549)

