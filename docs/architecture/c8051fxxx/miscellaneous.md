# Miscellaneous

* 关于变量初始化和看门狗
  * 如果需要初始化的变量过多，由于系统重启默认开启看门狗，故可能被狗咬。解决办法可以是在启动代码中添加关闭看门狗的命令或者 refresh（不过实验时 refresh 的方法没有起效）
  * [http://m.blog.chinaunix.net/uid-22695386-id-3036498.html](http://m.blog.chinaunix.net/uid-22695386-id-3036498.html)

