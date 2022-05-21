## Solver

- 可以快速实现物体的各种运动和跟随策略。
- ref: https://docs.microsoft.com/en-us/windows/mixed-reality/mrtk-unity/features/ux-building-blocks/solvers/solver?view=mrtkunity-2021-05

## head gaze 的判定和使用

- 其实就是把主摄像机的位置和朝向作为 gaze 状态使用。

```c#
void Update()
{
       RaycastHit hitInfo;
       if (Physics.Raycast(
               Camera.main.transform.position,
               Camera.main.transform.forward,
               out hitInfo,
               20.0f,
               Physics.DefaultRaycastLayers))
       {
           // If the Raycast has succeeded and hit a hologram
           // hitInfo's point represents the position being gazed at
           // hitInfo's collider GameObject represents the hologram being gazed at
       }
}
```   

- ref: https://docs.microsoft.com/en-us/windows/mixed-reality/develop/unity/gaze-in-unity

## body locked & tag along

- 这是 HL 中的一种虚拟物体的软跟随方式，例如菜单界面会始终跟随以落在用户的视野内，但在视野内时不会再移动。使用 Radial View Solver 可以快速实现这一效果。
    - 然而亲测使用 fixed height 时的渲染效果较差，建议尽量在 HL 中使用软的物理约束（也可能是因为配置原因）。
    - ref: https://docs.microsoft.com/en-us/windows/mixed-reality/design/billboarding-and-tag-along

## 按钮

- HL 中现成的按钮是通过（使用手势等）碰撞按下一定深度来模拟的，可以说是很仿真的按钮了。
- 创建一个 3D 物体，注意给它添加碰撞盒，然后添加 MRTK 的 `PressableButton` 和 `NearInteractionTouchable` 脚本。
- ref：
    - button: https://microsoft.github.io/MixedRealityToolkit-Unity/Documentation/README_Button.html#how-to-make-a-button-from-scratch
    - example scene: https://docs.microsoft.com/en-us/windows/mixed-reality/develop/unity/hand-eye-in-unity

## Nuget for Unity

- 直接在 VS 项目中用 Nuget Manager 安装 Nuget 包是无法被 Unity 识别的。Nuget for Unity 是一个可以从 Unity 内管理 Nuget 包的 package。
- repo: https://github.com/GlitchEnzo/NuGetForUnity

## QR code

- 复现成功，简要记录遇到过的所有issue
- 复现成功的例程：https://github.com/rderbier/Hololens-QRcodeSample
    - 实际用了 2.7 版本的 MRTK，Mixed Reality Feature Tool 似乎没法给 2019.2 这么旧的 Unity 提供安装，因此按照官方 release 的说明下载了 foundation 和 tools 两个 unitypackage 文件并导入了。
    - ref: https://github.com/microsoft/MixedRealityToolkit-Unity/releases
- 开始侥幸使用 2020 版本的 Unity 跑，但发现还是受到 API 变动的影响。有一篇迁移到 2020 的博客，但尚未尝试：
    - blog: https://localjoost.github.io/Upgrading-reading-and-positioning-QR-codes-with-HoloLens-2-to-Unity-2020-+-OpenXR-plugin/
    - repo: https://github.com/LocalJoost/QRCodeService/tree/main
- 无法通过 Nuget for Unity 安装 MixedReality.QR 依赖的 VCRT Forwarders 包
    - 解决（或许）：用 VS 的 Nuget package manager 安装后找到包的安装目录（位置：https://docs.microsoft.com/en-us/nuget/consume-packages/managing-the-global-packages-and-cache-folders），将其中名为 Unity 的子文件夹下的内容移入 Unity 项目，其中一个 C# 脚本子文件夹和其他自己的脚本放一块（大概放哪都行），另一个包含一堆 dll 的子文件夹放到 Plugins 下。这样做之后构建没有报错，但实际最后没有跑起来，所以不清楚是不是正确的解决方式。
    - ref: https://stackoverflow.com/questions/53447595/nuget-packages-in-unity
- ref：
    - https://docs.microsoft.com/en-us/windows/mixed-reality/develop/advanced-concepts/qr-code-tracking-overview
    - https://docs.microsoft.com/en-us/windows/mixed-reality/develop/unity/qr-code-tracking-unity
    - https://github.com/chgatla-microsoft/QRTracking
    - https://github.com/microsoft/MixedReality-QRCode-Sample
    - https://www.nuget.org/packages/Microsoft.MixedReality.QR
    - https://codeholo.com/2021/03/27/qrcode-tracking-with-hololens-2-xr-sdk-and-mrtk-v2-5/

## Manipulation

- 使用 ObjectManipulator 组件。
    - ref: https://docs.microsoft.com/en-us/windows/mixed-reality/mrtk-unity/features/ux-building-blocks/object-manipulator?view=mrtkunity-2021-05
    - 测试时 near interaction 不是很 work，最后只保留了 far + two hands + move 的配置以保证精确性。

## Input & Control

- 鼠标输入：https://docs.microsoft.com/en-us/windows/mixed-reality/mrtk-unity/features/input/pointers?view=mrtkunity-2021-05#mousepointer

## Unity Browser
  
- 暂未提上日程，存档
    - Browser Impl:
        - https://firefox-source-docs.mozilla.org/mobile/android/geckoview/consumer/index.html
        - https://mozilla.github.io/geckoview/javadoc/mozilla-central/org/mozilla/geckoview/package-summary.html
        - https://github.com/IanPhilips/UnityOculusAndroidVRBrowser
        - https://forum.unity.com/threads/beta-in-game-3d-web-browser-for-android.594058/
    - Android + Unity:
        - https://github.com/Unity-Technologies/uaal-example/blob/master/docs/android.md
        - https://stackoverflow.com/questions/24564470/unity3d-and-android-studio-integration
        - https://docs.unity3d.com/Manual/UnityasaLibrary-Android.html
        - https://docs.unity3d.com/Manual/android-gradle-overview.html
