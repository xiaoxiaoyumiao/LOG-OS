# Customize Inspector

## Introduction

[https://blog.csdn.net/qq_33337811/article/details/62042218](https://blog.csdn.net/qq_33337811/article/details/62042218)

## Serialization

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

## Text Input Style Control
设置字符串输入框的大小：使用 `[TextArea(x, y)]` 修饰。

ref:
* [https://docs.unity3d.com/ScriptReference/TextAreaAttribute.html](https://docs.unity3d.com/ScriptReference/TextAreaAttribute.html)
* [https://answers.unity.com/questions/1007952/how-do-i-make-text-boxes-in-the-inspector-bigger.html](https://answers.unity.com/questions/1007952/how-do-i-make-text-boxes-in-the-inspector-bigger.html)

## Add a Button in Inspector

```csharp
// Here I add a button to the inspector of a component called GlobalSet
[CustomEditor(typeof(GlobalSet))]
public class GlobalSetEditor : Editor {

    public override void OnInspectorGUI()
    {
        // Draw default inspector layouts. Otherwise it's overwritten
        // Also check: DrawDefaultInspector()
        base.OnInspectorGUI(); 
        var globalSet = (GlobalSet)target;
        if (GUILayout.Button("Update Desk Numbers"))
        {
            // Do something
        }
```

- ref: https://answers.unity.com/questions/126048/create-a-button-in-the-inspector.html

## File System Access

例如调出文件保存对话框，其标题为 `Save texture as PNG` ，默认文件名为贴图名，后缀为 .png ：

```
var path = EditorUtility.SaveFilePanel(
            "Save texture as PNG",
            "",
            texture.name + ".png",
            "png");
```

类似地还有调出保存路径、警告对话框等接口。详见 ref: \[2]。

## References

\[1] [https://learn.unity.com/tutorial/editor-scripting#5c7f8528edbc2a002053b5f9](https://learn.unity.com/tutorial/editor-scripting#5c7f8528edbc2a002053b5f9)

\[2] [https://docs.unity3d.com/2019.4/Documentation/ScriptReference/EditorUtility.SaveFilePanel.html](https://docs.unity3d.com/2019.4/Documentation/ScriptReference/EditorUtility.SaveFilePanel.html)
