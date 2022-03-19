# Coordinate System

* Unity中有多套坐标系，最重要的应注意何时为屏幕坐标、何时为世界坐标，并做转换。所有坐标系之间都有转换函数（网上有些函数已经废弃），直接调用相应的摄像机的方法即可
  * GUI界面绘制坐标系：屏幕左上角为原点\(0,0\)，右下角为\(Screen.width,Screen.height\)。GUI绘制采用此坐标系
  * 屏幕\(screen\)坐标系：屏幕左下角为原点\(0,0\)，右上角为\(Screen.width,Screen.height\)。鼠标或触屏位置采用此坐标系
  * 视口\(viewport\)坐标系：视口（摄像机显示区域）左下角原点\(0,0\)，右上角\(1,1\)，是归一化的坐标系。摄像机视角采用此坐标系，如摄像机的Viewport rect的x,y,w,h等参数采用的就是视口坐标系（严格来说这个视口矩形填的是对整个屏幕建立视口坐标系后摄像机视口显示到屏幕上的位置和尺寸，但摄像机做坐标转换的时候仍然是以视口左下角而不是屏幕左下角作为\(0,0\)点）
  * 世界\(world\)坐标系：游戏空间的实际坐标系，游戏对象transform等采用此坐标系。
* 鼠标（屏幕坐标系）转世界坐标：需要对齐Z平面
  * ```text
    //获取鼠标在相机中（世界中）的位置，转换为屏幕坐标；
    screenPosition = Camera.main.WorldToScreenPoint(transform.position);
    //获取鼠标在场景中坐标
    mousePositionOnScreen = Input.mousePosition;
    //让场景中的Z=鼠标坐标的Z
    mousePositionOnScreen.z = screenPosition.z;
    //将相机中的坐标转化为世界坐标
    mousePositionInWorld = Camera.main.ScreenToWorldPoint(mousePositionOnScreen);
    ```
* 相对坐标和世界坐标的转换：
  * ```text
    localVector = transform.InverseTransformPoint(worldVector)
    // transform是作为local参照的物体的transform
    worldVector = transform.TransformPoint(localVector)
    // transform同上
    ```

