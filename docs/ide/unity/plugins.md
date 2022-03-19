# Plugins

## Import

直接将 dll 文件放入 Unity 工程目录下，Unity 就会识别并加载它。Unity 按照 dll 文件名来区分各个 dll，因此项目中不能有重名的 dll。此外 dll 一旦加载就不会被 unload，只能通过重启编辑器来更新。

导入 dll 中的函数代码如下：

```csharp
using UnityEngine;
    using System.Runtime.InteropServices;

    class SomeScript : MonoBehaviour {

       #if UNITY_IPHONE
   
       // On iOS plugins are statically linked into
       // the executable, so we have to use __Internal as the
       // library name.
       [DllImport ("__Internal")]

       #else

       // Other platforms load plugins dynamically, so pass the name
       // of the plugin's dynamic library.
       [DllImport ("PluginName")]
    
       #endif

       private static extern float FooPluginFunction ();

       void Awake () {
          // Calls the FooPluginFunction inside the plugin
          // And prints 5 to the console
          print (FooPluginFunction ());
       }
    }
```

## Debugging

通过以下方法可以在 Unity Visual Studio 工程中调试一个 Native Plugin。前提是在 dll 的所在目录下存在其调试文件（pdb，可以在构建 dll 时 VS 的输出目录下找到）：

> VS -&gt; "Attach to Process" -&gt; select "unity.exe" process 
>
> To troubleshoot: in VS use the "Modules" pane to verify that your dll is loaded and has symbols. I also set code type to "Native" in the attach dialog.

## Reference

\[1\] [https://docs.unity3d.com/Manual/NativePlugins.html](https://docs.unity3d.com/Manual/NativePlugins.html)

\[2\] [https://forum.unity.com/threads/how-to-debug-a-native-c-plugin.428681/](https://forum.unity.com/threads/how-to-debug-a-native-c-plugin.428681/)

