# Unity on Android

## Environment Setup

Minimum API level is the default SDK version that Unity would target when building project. (ref: \[3])

The output package name can be set in Edit -> Project Settings -> Player. (ref: \[4])

\[1] official routine: [https://docs.unity3d.com/2019.1/Documentation/Manual/android-sdksetup.html](https://docs.unity3d.com/2019.1/Documentation/Manual/android-sdksetup.html)

\[2] about specifying external SDK path: [https://gamedev.stackexchange.com/questions/174728/set-up-android-sdk-path-to-make-android-remote-work-in-unity](https://gamedev.stackexchange.com/questions/174728/set-up-android-sdk-path-to-make-android-remote-work-in-unity)

\[3] [https://forum.unity.com/threads/how-to-change-android-compile-sdk-target.443894/](https://forum.unity.com/threads/how-to-change-android-compile-sdk-target.443894/)

\[4] [https://forum.unity.com/threads/where-is-package-name-setting.318839/](https://forum.unity.com/threads/where-is-package-name-setting.318839/)



## Debug

Just make sure the target device is ADB-connected to the Unity Editor machine (can be via USB or WiFi).

You can also use Unity **logcat** package (can be found & installed in Unity buit-in package manager). Also make sure to connect the device.

\[1] official guide: [https://docs.unity3d.com/Manual/ManagedCodeDebugging.html](https://docs.unity3d.com/Manual/ManagedCodeDebugging.html)

\[2] a debug routine (not fully tested): [https://blogs.siliconorchid.com/post/newbie-coder/unity-intro-for-business-developer/pt4-debugger-logging/](https://blogs.siliconorchid.com/post/newbie-coder/unity-intro-for-business-developer/pt4-debugger-logging/)

\[3] logcat package reference: [https://docs.unity3d.com/Packages/com.unity.mobile.android-logcat@1.2/manual/index.html](https://docs.unity3d.com/Packages/com.unity.mobile.android-logcat@1.2/manual/index.html)

