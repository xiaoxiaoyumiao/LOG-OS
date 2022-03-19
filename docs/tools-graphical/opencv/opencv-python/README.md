# OpenCV-Python

Python 版本的 OpenCV 和 C++ 版本的接口大体相同，但有一些比较重要的区别。

* Python 版本中没有 C++ 中的 Mat 类型的概念，所有的矩阵为 NumPy 矩阵，其数据类型也完全采用 NumPy 的数据类型体系。Channel 采用矩阵的维度来区分，例如三通道的图片将用一个最后一维长度为 3 的矩阵表示。
  * 因此 Python 中图片对象的接口直接参考 NumPy 的文档即可。C++ 中用于类型转换的 `convertTo`  等方法也不再存在，采用 NumPy 的 `astype` 方法即可。此外，C++ 中需要借助 Rect 等类型对 Mat 对象进行切片索引，而在 Python 中则可以灵活采用 NumPy 的切片索引，使用 slice 对象或 slice 构成的元组来对图片对象进行切片。
  * 如果希望创建一个新的图片对象，无需调用特殊的构造方法，直接构造一个 NumPy 的矩阵即可。例如，可以用 `zeros_like` 来构造一个与已有图片形状、类型相同的空白图片对象。
  * 更多矩阵操作相关可参考 ref \[2\]。

如下是一个简短的 python OpenCV 程序，可以看到它和 C++ 版本有很多相似之处。大多接口的使用都可以以此类推。OpenCV 的接口 Doc 中同时包含了 C++ 和 Python 的接口，如可以参考 ref \[3\] 中的 Function Documentation。

运行需要有 OpenCV 的 Python 动态链接库，如果已安装了 OpenCV，动态链接库（.pyd 文件）可以在其安装目录下找到（例如 `opencv\build\python\cv2\python-3.9` ）。

```python
# Python program to explain cv2.cvtColor() method 
   
# importing cv2 
import cv2 
   
# some path
path = r'C:\Users\Administrator\Desktop\geeks.png' 
   
# Reading an image in default mode
src = cv2.imread(path)
   
# Window name in which image is displayed
window_name = 'Image'
  
# Using cv2.cvtColor() method
# Using cv2.COLOR_BGR2HSV color space
# conversion code
image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV )
  
# Displaying the image 
cv2.imshow(window_name, image)
```

## Reference

\[1\] [https://www.geeksforgeeks.org/python-opencv-cv2-cvtcolor-method/](https://www.geeksforgeeks.org/python-opencv-cv2-cvtcolor-method/)

\[2\] [https://docs.opencv.org/master/d3/df2/tutorial\_py\_basic\_ops.html](https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html)

\[3\] [https://docs.opencv.org/master/d2/de8/group\_\_core\_\_array.html](https://docs.opencv.org/master/d2/de8/group__core__array.html)



