# Data Retrieval

## Configure and Open

在打开设备时需要指定获取到的图片数据的格式等信息。这通过结构体 `k4a_device_configuration_t` 实现。

k4a 中主要有两类对象，一类是 handle，通常代表一个现实对象，而且引用被 k4a 维护，需要通过 k4a 方法解除引用；另一类是 data structure，只代表一份（配置等）数据，不需要由开发者维护生命周期。

通过设置 configuration 中各个 field 的值就可以对设备进行配置。

* `color_format` 色彩摄像头的图片格式，为枚举变量类型，可配置为 MJPG、BGRA 等
* `color_resolution` 色彩摄像头分辨率，为枚举变量类型，不设置时色彩摄像头将默认不开启
* `depth_mode` 设置深度摄像头的模式，不设置时深度摄像头将默认不开启
* `camera_fps` 两个摄像头的期望帧率，为枚举变量类型
* `synchronized_images_only` 是否同步摄像头的数据，默认为否，设置为真后设备只在色彩和深度帧数据都准备好后才返回数据，若只需要色彩或深度数据的其中一种可以将此选项复位

```cpp
// Configure a stream of 4096x3072 BRGA color data at 15 frames per second
k4a_device_configuration_t config = K4A_DEVICE_CONFIG_INIT_DISABLE_ALL;
config.camera_fps = K4A_FRAMES_PER_SECOND_15;
config.color_format = K4A_IMAGE_FORMAT_COLOR_BGRA32;
// config.color_resolution = K4A_COLOR_RESOLUTION_3072P;
config.color_resolution = K4A_COLOR_RESOLUTION_720P;
config.depth_mode = K4A_DEPTH_MODE_NFOV_UNBINNED;
config.synchronized_images_only = true;
```

准备好后可以开启设备：

```cpp
if (K4A_RESULT_SUCCEEDED != k4a_device_start_cameras(device, &config))
{
    // do some failure handling
}
```

## Get Capture Data

设备产生的每一份数据被封装在类型为 `k4a_capture_t` 的 capture handle 里。创建一个 capture 对象，然后调用方法将设备产生的新数据填充到 capture 对象中。

```cpp
// Capture a depth frame
k4a_capture_t capture;
switch (k4a_device_get_capture(device, &capture, TIMEOUT_IN_MS))
{
case K4A_WAIT_RESULT_SUCCEEDED:
    printf("Got capture.\n");
    break;
case K4A_WAIT_RESULT_TIMEOUT:
    printf("Timed out waiting for a capture\n");
    continue;
    break;
case K4A_WAIT_RESULT_FAILED:
    printf("Failed to read a capture\n");
    goto Exit;
}

// Use data stored in the capture
...

// Release the capture
k4a_capture_release(capture);
```

## Fetch & Use Image Intro

从 capture 对象中可以得到色彩或深度数据。如果在 config 中两个摄像头都启用且开启了数据同步，那么两种数据都可以得到。数据可以使用类型为 `k4a_image_t` 的 image handle 操作。

```cpp
k4a_image_t colorImage = k4a_capture_get_color_image(capture);
// Access the depth16 image
k4a_image_t depthImage = k4a_capture_get_depth_image(capture);
```

使用完 image 后应当释放。

```text
k4a_image_release(colorImage);
```

## Reference

\[1\] [https://docs.microsoft.com/en-us/azure/kinect-dk/retrieve-images](https://docs.microsoft.com/en-us/azure/kinect-dk/retrieve-images)

\[2\] [https://microsoft.github.io/Azure-Kinect-Sensor-SDK/master/structk4a\_\_device\_\_configuration\_\_t.html\#details](https://microsoft.github.io/Azure-Kinect-Sensor-SDK/master/structk4a__device__configuration__t.html#details)

\[3\] [https://microsoft.github.io/Azure-Kinect-Sensor-SDK/master/structk4a\_\_capture\_\_t.html](https://microsoft.github.io/Azure-Kinect-Sensor-SDK/master/structk4a__capture__t.html)

