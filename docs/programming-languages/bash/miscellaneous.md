# Miscellaneous

* 如何在 bash 终端显示里缩短当前路径的显示？
  * 旧版本可以通过修改 `PS1` 变量实现
  * 较新的版本可以使用 `PROMPT_DIRTRIM` 变量实现，它定义在终端中展示几层目录
  * 可以在 bash startup file 中修改上述变量来达到定制路径显示的效果
    * ref: [https://unix.stackexchange.com/questions/381113/how-do-i-shorten-the-current-directory-path-shown-on-terminal](https://unix.stackexchange.com/questions/381113/how-do-i-shorten-the-current-directory-path-shown-on-terminal)
* 进程的挂起和恢复
  * ctrl + Z 可以挂起一个正在执行的进程
  * fg 命令可以把被挂起的进程重新调到前台执行
  * bg 命令可以把被挂起的进程调到后台执行
    * ref：[https://blog.csdn.net/qq\_42914528/article/details/81913482](https://blog.csdn.net/qq_42914528/article/details/81913482)
* 在函数中使用 local 修饰符可以定义一个函数中的局部变量
  * ref： [https://blog.csdn.net/robertsong2004/article/details/41555245](https://blog.csdn.net/robertsong2004/article/details/41555245)

