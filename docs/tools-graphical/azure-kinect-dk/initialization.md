# Initialization

## Initialization

首先获取当前连接的 Azure Kinect 设备数量，然后通过索引打开相应的设备。打开设备需要提供一个类型为 `k4a_device_t` 的 device handle。

```cpp
// get connected device count
uint32_t count = k4a_device_get_installed_count();
if (count == 0)
{
    printf("No k4a devices attached!\n");
    return 1;
}

k4a_device_t device = NULL;

for (uint32_t deviceIndex = 0; deviceIndex < count; deviceIndex++)
{
    // open the device
    if (K4A_RESULT_SUCCEEDED != k4a_device_open(deviceIndex, &device))
    {
        printf("%d: Failed to open device\n", deviceIndex);
        continue;
    }

    ...
}
```

如果只有一个设备连接，也可以通过预定义的 DEFAULT 标识符来连接：

```cpp
// Open the first plugged in Kinect device
k4a_device_t device = NULL;
// K4A_FAILED is a MACRO determining if the result represents failure
if (K4A_FAILED(k4a_device_open(K4A_DEVICE_DEFAULT, &device)))
{
    printf("Failed to open k4a device!\n");
    return 1;
}
```

不同连接时机下同一台设备的索引可能不同，如果希望连接到固定的某一台设备，可以查询设备的序列号。

```cpp
// Get the size of the serial number
size_t serial_size = 0;
// device: k4a_device_t Device handle.
// NULL: char* Serial number.
// &serial_size: size_t* Serial number size.
// This returns K4A_BUFFER_RESULT_TOO_SMALL when provided buffer is too small.
// In other unsuccessful situations it just returns failure.
// We can pass NULL to the buffer argument without generating errors.
k4a_device_get_serialnum(device, NULL, &serial_size);

// Allocate memory for the serial, then acquire it
char *serial = (char*)(malloc(serial_size));
k4a_device_get_serialnum(device, serial, &serial_size);
printf("Opened device: %s\n", serial);
free(serial);
```

任何设备使用完毕后，都需要关闭。

```cpp
// close the device
k4a_device_close(device);
```

## Reference

\[1\] [https://docs.microsoft.com/en-us/azure/kinect-dk/find-then-open-device](https://docs.microsoft.com/en-us/azure/kinect-dk/find-then-open-device)

