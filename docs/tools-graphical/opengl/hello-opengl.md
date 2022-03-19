# Hello OpenGL

## Introduction

* OpenGL 本身是对图像绘制 API 的 specification，定义了各个方法的参数和返回值。其实现由具体硬件环境（尤其是显卡）决定。
* 早版本 OpenGL 设计为 immediate mode，开发者直接调用图像绘制方法。随着 OpenGL 为开发者提供越来越多的定制空间，从 3.3 版本开始 OpenGL 鼓励采用 core-profile mode 开发，这是 OpenGL specification 的一个移除了旧接口的子集。
* OpenGL 向下兼容，核心机制并不随版本更新改变，因此上手时学习 OpenGL 3.3 而非某个最新版本是合理的。
* OpenGL 是一个巨大的状态机，每一刻的状态是一个 context，用户通过操作 context 来改变 OpenGL 的绘制模式。

## Installation on Windows

* GLFW 是常用的跨平台 OpenGL 开发库之一，提供对窗口、OpenGL contexts 和。安装地址：[https://www.glfw.org/download.html](https://www.glfw.org/download.html)
  * 也可以使用 CMake 从源代码编译所需的库文件。
* （以 Visual Studio 为例）新建空白项目，在项目 properties 中配置 GLFW 的头文件路径和库文件路径，以及对 GLFW 库文件的依赖。
* 在 Windows 上，Visual Studio 的 Microsoft SDK 自带 OpenGL 实现的库 opengl32.lib。需要把这一库文件添加到项目依赖。
* 对 OpenGL 接口的具体实现要通过函数指针和特定接口在 runtime 确定，使用每个接口时都这么做会使代码繁琐。GLAD 是一个基于 web 的 code generator，在指定 OpenGL 版本等信息后就可以自动生成一份 loader 代码用于项目中。
  * GLAD：[https://glad.dav1d.de](https://glad.dav1d.de)
  * 生成后下载 zip 文件并解压得到 include 和 src 文件夹。将前者的内容加入项目的 include 范围，将后者包含的 glad.c 文件加入项目。

## Hello OpenGL

* 以下代码能生成一个墨绿色的窗口，并在按下 esc 时关闭窗口。

```cpp
#include <glad\glad.h>
#include <GLFW\glfw3.h>
#include <iostream>

void framebuffer_size_callback(GLFWwindow* window, int width, int height);
void processInput(GLFWwindow *window);

int main() {
    // initialize GLFW
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    //glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);

    // create a window
    GLFWwindow* window = glfwCreateWindow(800, 600, "LearnOpenGL", NULL, NULL);
    if (window == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);

    // load GLAD
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
    {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }
    glViewport(0, 0, 800, 600); // (0, 0) is the lower left corner

    // reister a callback for window resizing
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

    // main loop
    while (!glfwWindowShouldClose(window))
    {
        // input
        processInput(window);

        // set the color to use to clear the color buffer
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        // other bits that can be speficied are GL_DEPTH_BUFFER_BIT and GL_STENCIL_BUFFER_BIT
        glClear(GL_COLOR_BUFFER_BIT);

        // consume events
        glfwPollEvents();        
        // refresh display buffer
        glfwSwapBuffers(window); 
    }

    // end program
    glfwTerminate();
    return 0;
}

void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
    glViewport(0, 0, width, height);
}

void processInput(GLFWwindow *window)
{
    // close the window if ESCAPE is pressed
    // GetKey returns a GLFW_RELEASE when the provided key is not pressed
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
}
```

## Reference

\[1\] [https://learnopengl.com/Getting-started](https://learnopengl.com/Getting-started)

