# Miscellaneous

* 一个带有member的class被绑定到一个游戏中的实体（拖动放置到实体）时，实体会多出一个与class名字一致的属性组（在unity里似乎叫做component），且具有与member一致的子属性。如果script更新，unity中的属性也会随之更新。
* 碰撞盒是一类常用的component，包括box collider 2d和rigidbody 2d等
* 若需要为 Unity 项目添加 reference，在 VS 的项目浏览面板中选择 csharp project 中的 references，展开，点击 Analyzers，在 Project 菜单中选择 Add Reference.(ref: \[2])
* 关于自定义 Inspector：(ref: \[1])
  * 设置字符串输入框的大小：使用 \[TextArea(x, y)] 修饰。
    * [https://docs.unity3d.com/ScriptReference/TextAreaAttribute.html](https://docs.unity3d.com/ScriptReference/TextAreaAttribute.html)
    * [https://answers.unity.com/questions/1007952/how-do-i-make-text-boxes-in-the-inspector-bigger.html](https://answers.unity.com/questions/1007952/how-do-i-make-text-boxes-in-the-inspector-bigger.html)
* 如何在 VS 中查看项目的 properties：

> You have to enable the "Access to project properties" option in the Tools>Options>Tools for Unity>General" section.   (ref: \[3])

* 使用 transform.parent 获取父对象。
* 如果想在查看场景时让场景视角绕一个物体旋转，可选定该物体后按 Alt + 鼠标左键拖动即可。(ref: \[5])

## References

\[1] [https://blog.csdn.net/qq\_33337811/article/details/62042218](https://blog.csdn.net/qq\_33337811/article/details/62042218)

\[2] [https://stackoverflow.com/questions/48875798/add-reference-is-missing-in-visual-studio-when-using-with-unity-3d-need-npgsql](https://stackoverflow.com/questions/48875798/add-reference-is-missing-in-visual-studio-when-using-with-unity-3d-need-npgsql)

\[3] [https://developercommunity.visualstudio.com/t/project-properties-cant-be-opened-for-unity-projec/13766](https://developercommunity.visualstudio.com/t/project-properties-cant-be-opened-for-unity-projec/13766)

\[4] [https://answers.unity.com/questions/33552/gameobjectparent.html](https://answers.unity.com/questions/33552/gameobjectparent.html)

\[5] [https://forum.unity.com/threads/how-do-i-make-unity-rotate-a-scene-around-selection.77209/](https://forum.unity.com/threads/how-do-i-make-unity-rotate-a-scene-around-selection.77209/)
