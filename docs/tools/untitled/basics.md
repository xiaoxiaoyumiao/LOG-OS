# Basics

## USB Connection

* 将待调试的手机通过 USB 数据线连接开发计算机
* 在手机上打开开发者选项 - USB 调试
* 在开发计算机上 adb 所在目录下运行 `adb devices -l` ，此时 adb client 启动，并检测是否有 adb server 在运行，若没有则会自动启动，并将 client 连接至 server。
* 上面的命令会显示包含当前连接的所有模拟器和硬件设备的列表。

## Wireless Connection

Here we use connection with an Nreal smart glass device as an example. The smart glass uses Android kernel and has WiFi networking. In our setting, the smart glass and the machine running adb (that is, my laptop) are connected to the same local network.

* `adb devices` command lists all connected devices. Output looks like this:

```
List of devices attached
8eda6f94        device
```

* `8eda6f94` is the device serial id. Now restart adb in `tcpip` mode for this device. Run:

```
adb -s 8eda6f94 tcpip 5555
```

* Here `-s` stands for 'serial' and it's followed by the device id. 5555 is the port. This don't have to be 5555 actually; I guess all **odd** ports between 5555 and 5585 works. (ref: \[2])
  * `-s` and the id can be omitted if the connected device is unique.
* Now find the IP address of the android device for setting up wireless connection. `adb shell` execute shell commands directly on the target android device.(ref: \[4]) There are several shell commands that can be used to get device's ip address (ref: \[5]), for example `ip route`. So run:

```
adb -s 8eda6f94 shell ip route
```

* Here we use `-s` to name the device, and let `shell` to execute `ip route` on the device. Output looks like this:

```
192.168.1.0/24 dev wlan0  proto kernel  scope link  src [ip address]
```

* The address we want will appear at the `[ip address]` position.
* Finally, use this address to connect to the device wirelessly:

```
adb connect [ip address]:[port]
```

* Remember to replace the `[ip address]` with the address we get, and `[port]` with the port number we choose above (5555).
* Now run `adb devices` , a new device would appear in the list. Notice that its serial id is exactly the `[ip address]:[port]`. The USB cable can be unplugged now and the first device would just disappear.

## File Transfer

> 如需从设备中复制某个文件或目录（及其子目录），请使用以下命令：

```
adb pull remote local
```

> 如需将某个文件或目录（及其子目录）复制到设备，请使用以下命令：

```
adb push local remote
```

> 将 `local` 和 `remote` 替换为开发机器（本地）和设备（远程）上的目标文件/目录的路径。

## Kill Server

> 如需停止 adb 服务器，请使用 `adb kill-server` 命令。然后，您可以通过发出其他任何 adb 命令来重启服务器。

## Reference

\[1] [https://developer.android.com/studio/command-line/adb#wireless](https://developer.android.com/studio/command-line/adb#wireless)

\[2] [https://developer.android.com/studio/command-line/adb#howadbworks](https://developer.android.com/studio/command-line/adb#howadbworks)

\[3] [https://medium.com/@amanshuraikwar.in/connecting-to-android-device-with-adb-over-wifi-made-a-little-easy-39439d69b86b](https://medium.com/@amanshuraikwar.in/connecting-to-android-device-with-adb-over-wifi-made-a-little-easy-39439d69b86b)

\[4] [https://technastic.com/adb-shell-commands-list/](https://technastic.com/adb-shell-commands-list/)

\[5] [http://rapidprogrammer.com/how-to-get-android-ip-address-from-adb-commandline-shell](http://rapidprogrammer.com/how-to-get-android-ip-address-from-adb-commandline-shell)

\[6] [https://developer.android.google.cn/studio/command-line/adb](https://developer.android.google.cn/studio/command-line/adb)

