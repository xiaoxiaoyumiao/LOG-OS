# Image Manipulation

可以获取到 image 数据缓冲区来直接操作 image 数据。

通过以下方法可以获取到 image raw data 的缓冲区，从而将 image 数据转换为其他便于处理的图像格式，例如 cv 的 Mat。

```cpp
uint8_t* buffer = k4a_image_get_buffer(colorImage);
```

色彩 buffer 的格式由 config 决定。例如，在 BGRA 模式下，raw data 的每个元素依次由 Blue，Green，Red，Alpha 四个字节构成。

深度 buffer 的格式默认为 Depth 16，它就是一个 uint16\_t 数组（小端序，每个元素占 2 字节），每个元素为目标点到摄像机原点的距离（单位为毫米）。

k4a 也提供了其他一些 image 变换的方法。

## Coordinate Transformation

每个摄像头有一个自己的 2d 和 3d 的坐标系，分辨率和格式也有所不同。k4a 提供了在不同摄像头坐标系下变换数据的方法。

`k4a_calibration_t` 结构体描述设备的 calibration，它包含了色彩和深度摄像头的格式等信息，用于实现坐标系间变换。`k4a_calibration_camera_t` 结构体描述一个摄像头的 calibration。

通过以下代码可以获取到彩色摄像头的长和宽。

```cpp
k4a_calibration_t calibration;
if (K4A_FAILED(k4a_device_get_calibration(device, config.depth_mode, config.color_resolution, &calibration))) {
    printf("Failed to get calibration.\n");
    k4a_device_stop_cameras(device);
    k4a_device_close(device);
    return 1;
}

int colorWidth = calibration.color_camera_calibration.resolution_width;
int colorHeight = calibration.color_camera_calibration.resolution_height;
```

使用 calibration 对象可以构造出 transformation 对象。类型为 `k4a_transformation_t` 的 transformation handle 负责处理特定的图像变换。

```cpp
k4a_transformation_t transformation = k4a_transformation_create(&calibration);
if (transformation == NULL) {
    printf("Failed to get tranformation.\n");
    k4a_device_stop_cameras(device);
    k4a_device_close(device);
    return 1;
}

...

// Tranform the depth image to the color camera coordinate.

k4a_image_t rgbdImage;

// k4a_image_format_t  format
// int width_pixels  width in pixels
// int height_pixels  height in pixels
// int stride_bytes  0 for reasoning from format and width
// k4a_image_t* image_handle 
)    
if (K4A_FAILED(k4a_image_create(K4A_IMAGE_FORMAT_DEPTH16, colorWidth, colorHeight, 0, &rgbdImage))) {
    printf("failed to create rgbd image.\n");
}

k4a_transformation_depth_image_to_color_camera(transformation, depthImage, rgbdImage);

...

k4a_image_release(rgbdImage);

...

// Destroy tranformation handle
k4a_transformation_destroy(transformation);
```

## Reference

\[1\] [https://docs.microsoft.com/en-us/azure/kinect-dk/use-image-transformation](https://docs.microsoft.com/en-us/azure/kinect-dk/use-image-transformation)

\[2\] [https://docs.microsoft.com/en-us/azure/kinect-dk/use-calibration-functions](https://docs.microsoft.com/en-us/azure/kinect-dk/use-calibration-functions)

