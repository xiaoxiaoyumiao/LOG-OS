# Environment & Platform

Unity 会在 C# 项目中定义一些 #define 预处理指令，这些指令定义的符号可以用于判断当前程序所处的环境。例如在编辑器中，Unity 将定义 `UNITY_EDITOR` ；但在针对 UWP 平台构建时，则会定义 `UNITY_WSA` 。假设有一段代码依赖最终部署的 UWP 平台的功能，但无法在编辑器中运行，便可以通过 `#ifdef UNITY_EDITOR` 来判断当前构建的目标环境是 UWP 还是编辑器，从而避免 Unity 尝试在编辑器环境中编译这一段代码而无法正常运行。

在某些情况下，我们希望检查这些 platform specific 代码的正确性。但如果采用上面的写法，在 VS 中这部分代码会由于预处理指令的存在被语法解析器忽略。如果希望切换到基于 platform specific 的预处理指令，可以在 Edit - Preferences - External Tools 中勾选 Player projects，而后点击 Regenerate project files 使得配置生效。如此设置后，在 VS 的解决方案中将出现两个项目，其中一个是针对编辑器环境的 project，另一个则是针对最终部署环境的 player project。它们的内容一致，指向的也是相同的文件，不同只在于环境，因此编辑 player project 中的文件时，代码会基于最终部署环境的预处理指令被解析。

## csc.rsp File

通过在项目的 Assets 文件夹中添加 csc.rsp 文件，可以设置自定义的预处理指令，以及引用一些第三方库。(ref: \[4])

## References

\[1] Unity platform dependent compilation & preprocessors: [https://docs.unity3d.com/Manual/PlatformDependentCompilation.html](https://docs.unity3d.com/Manual/PlatformDependentCompilation.html)

\[2] player project related: [https://forum.unity.com/threads/everything-under-if-windows\_uwp-greyed-out-in-visual-studio-even-though-build-settings-targets-uwp.957251/](https://forum.unity.com/threads/everything-under-if-windows\_uwp-greyed-out-in-visual-studio-even-though-build-settings-targets-uwp.957251/)

\[3] also player project related: [https://forum.unity.com/threads/whats-the-difference-between-playing-in-editor-and-building.922373/](https://forum.unity.com/threads/whats-the-difference-between-playing-in-editor-and-building.922373/)

\[4] Unity csc.rsp: [https://docs.unity3d.com/Manual/dotnetProfileAssemblies.html](https://docs.unity3d.com/Manual/dotnetProfileAssemblies.html)

\[5] csc.rsp related: [https://answers.unity.com/questions/1645154/what-is-cscrsp-file-and-how-can-i-add-it-to-unity.html](https://answers.unity.com/questions/1645154/what-is-cscrsp-file-and-how-can-i-add-it-to-unity.html)

\[6] UWP / WINRT API related: [https://docs.unity3d.com/Manual/windowsstore-scripts.html](https://docs.unity3d.com/Manual/windowsstore-scripts.html)

\[7] global define: [https://forum.unity.com/threads/global-define.93901/](https://forum.unity.com/threads/global-define.93901/)

\[8] also global define: [https://forum.unity.com/threads/how-to-set-project-wide-pragma-directives-with-javascript.71445/](https://forum.unity.com/threads/how-to-set-project-wide-pragma-directives-with-javascript.71445/)





