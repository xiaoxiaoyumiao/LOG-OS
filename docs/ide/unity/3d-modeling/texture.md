# Texture

* 使用 `SetPixels` 和 `Apply` 可以在代码中动态修改一个 texture 对象并应用。texture 需要被启用读写，且只有特定格式的 texture 可以被修改。这些都可以在 texture 对象的 import settings 中配置。请将 Format 设置为受支持的格式（例如 ARGB32, RGBA32, RGB24 和 Alpha8）。
* ref：[https://forum.unity.com/threads/setpixels-unsupported-texture-format.150028/](https://forum.unity.com/threads/setpixels-unsupported-texture-format.150028/)
* api ref: [https://docs.unity3d.com/ScriptReference/Texture2D.SetPixels.html](https://docs.unity3d.com/ScriptReference/Texture2D.SetPixels.html)

