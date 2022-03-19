# Miscellaneous

* 不知道为什么使用 texture control 时 texture 的坐标系和实际 UV 的坐标系是垂直镜像的（height 维度方向相反），记得做上下翻转。
  * [https://docs.nvidia.com/gameworks/content/artisttools/hairworks/1\_0/Using\_HairWorks.html](https://docs.nvidia.com/gameworks/content/artisttools/hairworks/1_0/Using_HairWorks.html)
* 官方教程中在使用 3ds max 时用 Hair and fur modifier 创建 hair guide，但记得在创建完成后就把这个 modifier 删掉，否则导出时会发生奇怪的事情。hairworks 需要的只有作为 hair guide 的 line 对象。

