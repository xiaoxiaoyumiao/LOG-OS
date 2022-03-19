# Miscellaneous

* 在 Properties 中，使用 $\(ENV\_VAR\) 可以取环境变量的值。如果在 VS 运行时更改了环境变量，需要重启 VS 使之生效。
* 项目依赖的 lib 文件需要在 Properties - Linker - Input - Additional Dependencies 中设置。
* 项目依赖的 dll 文件需要在 PATH 环境变量包含的路径下或构建的输出目录（例如 Debug 或 Release 文件夹），才能被链接器自动查找到；或者可以使用 WINAPI 在代码中手动加载 dll。
  * ref：[https://stackoverflow.com/questions/7845886/linking-dll-in-visual-studio](https://stackoverflow.com/questions/7845886/linking-dll-in-visual-studio)

