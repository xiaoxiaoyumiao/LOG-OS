# Better Graphics

## TextMesh Pro

* 基本使用
  * 最基本的当然是设置文字内容。和一般的文本组件一样，只需设置组件的 text 属性为文字内容即可。
  * TextMesh Pro(TMP) 提供了相当丰富的文本元信息，这些信息包含在 `TMP_TextInfo` 对象中。通过组件的 `textInfo` 属性可以获得包含当前文本元信息的 `TMP_TextInfo` 。text info 的常用属性有：
    * `wordInfo` ：是 `TMP_WordInfo` 对象构成的数组，每个 `TMP_WordInfo` 存储一个 word 的元信息（例如起止字符的索引等）。在 TMP 中标点不包含在 word 中。
    * `wordCount` ：词数。注意 `wordInfo` 数组的 Count 并不一定是真实的总行数，下同
    * `lineInfo` ：是 `TMP_LineInfo` 对象构成的数组，每个 `TMP_LineInfo` 存储一个 line 的元信息（例如起止字符的索引等）。
    * `lineCount` ：行数。
    * `pageInfo` ：是 `TMP_PageInfo` 对象构成的数组，每个 `TMP_PageInfo` 存储一个 page 的元信息（例如起止字符的索引等）。将 TMP 组件的 overflow mode 设置为分页模式后就可以得到多个 page。
    * `pageCount` ：页数。
* 关于可见性控制
  * 通过设置组件的 `maxVisibleLines` 可以控制可见的行数。
* 关于字体大小
  * 对于 Unity 的普通 text 组件，font size 的作用以及和 pixels per unit 的关系比较奇怪（尤其是在值比较小的时候）。TMP 的字体大小完全（正比例地）受 font size 的控制，同时也意味着无法通过 pixels per unit 控制“分辨率”（而只能通过操作 scaling 缩放）。
  * ref: \[6] 提到了更详细的字体大小，`lineHeight` ，以及 `ForceMeshUpdate` 的一些性质。
* 关于自定义字体
  * ttf 字体无法直接应用于 TMP。TMP 提供了 font asset creator (Windows -> TextMeshPro -> Font Asset Creator)，可以将 ttf 资源转换为 TMP 字体和材质资源。在转换时若无特殊要求，全部采取其默认配置即可。转换结果包含一个 TMP 字体资源文件和一个材质文件。
* 关于间距设置
  * spacing 控制的是在文本元素之间插入的额外间距的大小，因此设置为 0 时就是通常情况下的默认间距。其单位为 em，即与字体大小的比值。官方解释详见 ref: \[4]。
  * 间距都可以通过脚本设置，例如 `lineSpacing` 属性。(ref: \[8])
* 关于颜色设置
  * 如果颜色效果是相对静态的，可以直接将内容通过富文本的语法标记颜色。(ref: \[7])
  * 但如果需要较为频繁地动态修改颜色，则需要操作 mesh 信息。这里直接贴上一段可用代码（版本：TMP 2.1.1）。也可以参考官方 TMP 包里附带的颜色切换样例（如果只安装了 essential 也可以补装）。

```csharp
// This function assigns color to characters from index start to end.
// display: a TMP component
void UpdateSpanColor(Color32 color, int start, int end)
    {
        // Debug.Log($"start: {start} end: {end}");
        TMP_TextInfo textInfo = display.textInfo;
        start = Mathf.Max(start, 0);
        start = Mathf.Min(start, textInfo.characterCount - 1);
        end = Mathf.Min(end, textInfo.characterCount);
        for (int characterIndex = start; characterIndex < end; ++characterIndex)
        {
            // int characterIndex = startIndex + i;
            if (textInfo.characterInfo[characterIndex].isVisible)
            {
                int meshIndex = textInfo.characterInfo[characterIndex].materialReferenceIndex;
                int vertexIndex = textInfo.characterInfo[characterIndex].vertexIndex;
                // Get a reference to the vertex color
                Color32[] vertexColors = textInfo.meshInfo[meshIndex].colors32;
                vertexColors[vertexIndex + 0] = color;
                vertexColors[vertexIndex + 1] = color;
                vertexColors[vertexIndex + 2] = color;
                vertexColors[vertexIndex + 3] = color;
                display.UpdateVertexData(TMP_VertexDataUpdateFlags.Colors32);
            }
        }
    }
```


## References

\[1] TMP font asset creation: [https://learn.unity.com/tutorial/textmesh-pro-font-asset-creation#5f60578fedbc2a0022b98998](https://learn.unity.com/tutorial/textmesh-pro-font-asset-creation#5f60578fedbc2a0022b98998)

\[2] Also font asset creation: [https://forum.unity.com/threads/use-other-fonts-in-textmesh-pro.527960/](https://forum.unity.com/threads/use-other-fonts-in-textmesh-pro.527960/)

\[3] An explanation on TMP scaling: [https://forum.unity.com/threads/textmeshpro-scale.673867/](https://forum.unity.com/threads/textmeshpro-scale.673867/)

\[4] About spacing: [https://forum.unity.com/threads/units-of-spacing-options-in-inspector.755066/](https://forum.unity.com/threads/units-of-spacing-options-in-inspector.755066/)

\[5] Additional resource on px & em: [https://betterprogramming.pub/must-know-css-length-units-px-em-and-rem-ab4bf2a75907](https://betterprogramming.pub/must-know-css-length-units-px-em-and-rem-ab4bf2a75907)

\[6] [https://forum.unity.com/threads/getting-the-size-of-text-in-unity-scale.652198/](https://forum.unity.com/threads/getting-the-size-of-text-in-unity-scale.652198/)

\[7] Rich text syntax: [http://digitalnativestudios.com/textmeshpro/docs/rich-text/](http://digitalnativestudios.com/textmeshpro/docs/rich-text/)

\[8] [https://docs.unity3d.com/ScriptReference/TextMesh-lineSpacing.html](https://docs.unity3d.com/ScriptReference/TextMesh-lineSpacing.html)

\[9] official doc for font: [http://digitalnativestudios.com/textmeshpro/docs/font/](http://digitalnativestudios.com/textmeshpro/docs/font/)



