# Example Practice

## Transform K4A Image into OpenCV Mat

```cpp
// Configuration

k4a_device_configuration_t config = K4A_DEVICE_CONFIG_INIT_DISABLE_ALL;
config.camera_fps = K4A_FRAMES_PER_SECOND_30;
config.color_format = K4A_IMAGE_FORMAT_COLOR_BGRA32; // <==== For Color image
config.color_resolution = K4A_COLOR_RESOLUTION_2160P;
config.depth_mode = K4A_DEPTH_MODE_NFOV_UNBINNED; // <==== For Depth image 

// Color data

k4a_image_t colorImage = k4a_capture_get_color_image(capture); // get image metadata
if (colorImage != NULL)
{
    // you can check the format with this function
    k4a_image_format_t format = k4a_image_get_format(colorImage); // K4A_IMAGE_FORMAT_COLOR_BGRA32 

    // get raw buffer
    uint8_t* buffer = k4a_image_get_buffer(colorImage);

    // convert the raw buffer to cv::Mat
    int rows = k4a_image_get_height_pixels(colorImage);
    int cols = k4a_image_get_width_pixels(colorImage);
    cv::Mat colorMat(rows , cols, CV_8UC4, (void*)buffer, cv::Mat::AUTO_STEP);

    // ...

    k4a_image_release(colorImage);
}

// Depth data

k4a_image_t depthImage = k4a_capture_get_depth_image(capture); // get image metadata
if (depthImage != NULL)
{
    // you can check the format with this function
    k4a_image_format_t format = k4a_image_get_format(depthImage); // K4A_IMAGE_FORMAT_DEPTH16 

    // get raw buffer
    uint8_t* buffer = k4a_image_get_buffer(depthImage);

    // convert the raw buffer to cv::Mat
    int rows = k4a_image_get_height_pixels(depthImage);
    int cols = k4a_image_get_width_pixels(depthImage);
    cv::Mat depthMat(rows, cols, CV_16U, (void*)buffer, cv::Mat::AUTO_STEP);

    // ...

    k4a_image_release(depthImage);
}
```

## Reference

\[1\] [https://stackoverflow.com/questions/57222190/how-to-convert-k4a-image-t-to-opencv-matrix-azure-kinect-sensor-sdk](https://stackoverflow.com/questions/57222190/how-to-convert-k4a-image-t-to-opencv-matrix-azure-kinect-sensor-sdk)

\[2\] [https://github.com/microsoft/Azure-Kinect-Sensor-SDK/issues/968](https://github.com/microsoft/Azure-Kinect-Sensor-SDK/issues/968)

