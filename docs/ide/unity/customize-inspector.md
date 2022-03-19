# Customize Inspector

## 自定义Inspector

{% embed url="https://blog.csdn.net/qq_33337811/article/details/62042218" %}

## 在Inspector中添加按钮

```csharp
using UnityEngine;
using System.Collections;
using UnityEditor;

[CustomEditor(typeof(ObjectBuilderScript))]
public class ObjectBuilderEditor : Editor
{
    public override void OnInspectorGUI()
    {
        DrawDefaultInspector();

        ObjectBuilderScript myScript = (ObjectBuilderScript)target;
        if(GUILayout.Button("Build Object"))
        {
            myScript.BuildObject();
        }
    }
}
```

## 文件系统交互

例如调出文件保存对话框，其标题为 `Save texture as PNG` ，默认文件名为贴图名，后缀为 .png ：

```
var path = EditorUtility.SaveFilePanel(
            "Save texture as PNG",
            "",
            texture.name + ".png",
            "png");
```

类似地还有调出保存路径、警告对话框等接口。详见 ref: \[2]。

## 序列化

为了让component的field能够在inspector中便捷地被访问和修改，需要在类前标注这是一个可序列化的类，并对不需要序列化的值标注非序列化。

```
[System.Serializable]
public class BlockTypeParameter
{
    public int someProperty;
    [System.NonSerialized]
    private static BlockTypeParameter mFactory;
    ...
}
```

## References

\[1] [https://learn.unity.com/tutorial/editor-scripting#5c7f8528edbc2a002053b5f9](https://learn.unity.com/tutorial/editor-scripting#5c7f8528edbc2a002053b5f9)

\[2] [https://docs.unity3d.com/2019.4/Documentation/ScriptReference/EditorUtility.SaveFilePanel.html](https://docs.unity3d.com/2019.4/Documentation/ScriptReference/EditorUtility.SaveFilePanel.html)
