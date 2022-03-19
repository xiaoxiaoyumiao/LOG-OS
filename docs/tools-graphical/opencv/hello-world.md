# Hello World

* 在 Visual Studio 中创建一个 VS C++ 控制台项目，使用安装时设置的环境变量配置头文件路径和 library 路径，添加 lib 依赖（注意 Debug 和 Release 使用不同的库文件）
* 测试代码：

```cpp
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
using namespace cv;
using namespace std;
int main(int argc, char** argv)
{
    if (argc != 2)
    {
        cout << " Usage: " << argv[0] << " ImageToLoadAndDisplay" << endl;
        return -1;
    }
    Mat image;
    image = imread(argv[1], IMREAD_COLOR); // Read the file
    if (image.empty()) // Check for invalid input
    {
        cout << "Could not open or find the image" << std::endl;
        return -1;
    }
    namedWindow("Display window", WINDOW_AUTOSIZE); // Create a window for display.
    imshow("Display window", image); // Show our image inside it.
    waitKey(0); // Wait for a keystroke in the window
    return 0;
}
```

注意：`imshow` 后面必须跟随一个 `waitKey` 或者 `pollKey` 函数，否则无法达到显示效果。传入一个正的参数可以设置显示一帧的延时。

## Reference

\[1\] [https://docs.opencv.org/4.5.2/dd/d6e/tutorial\_windows\_visual\_studio\_opencv.html](https://docs.opencv.org/4.5.2/dd/d6e/tutorial_windows_visual_studio_opencv.html)

\[2\] [https://docs.opencv.org/master/d7/dfc/group\_\_highgui.html\#ga453d42fe4cb60e5723281a89973ee563](https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563)

