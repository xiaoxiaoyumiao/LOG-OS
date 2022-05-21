# Component Oriented Framework

Unity 的开发环境是面向组件的。

游戏的基本组成单位是场景（Scene），它是人物、物品、UI 等所有游戏元素的容器，常常表示游戏中的一块特定的空间，例如一个关卡。一个场景的信息储存在 `.unity` 文件中。

场景中的每个实体都是一个游戏对象（GameObject）。游戏对象可以在 Unity Editor 中拖动摆放，也可以在运行时由代码动态创建。
    * 这些对象或者独立，或者从属于其他对象而成父子关系。许多更加复杂的对象间的关系可以基于这种基本的层级关系来实现，例如维持两个对象的相对距离不变，或将众多的同类型对象分组管理。所有的游戏对象和它们之间的层级关系可以在 Hierarchy 面板中看到。
    * 并不是被渲染出具体形状的才能是游戏对象。事实上，我们常用空游戏对象来实现对其他游戏对象的管理。此外，摄像机本身也是游戏对象。
    * 游戏对象是一个运行时的概念，但游戏对象可以从特定的模板（称为 Prefab）创建，而这种模板是可持久化的。
 
每个游戏对象具有的性质由组件（Component）实现。一个组件实现一种特定的功能或性质，当一个组件被添加到一个游戏对象上时，这个游戏对象就被赋予了这个组件实现的性质。游戏对象就像是组件的容器。例如，一个具有碰撞盒的游戏对象可能拥有 `Collider` 或 `Collider2d` 组件。
    * 当选中一个游戏对象时，它拥有的组件可以在 Inspector 面板中看到。
    * 组件可以通过代码实现。事实上在 Unity 中，组件和脚本文件有相当紧密的联系。一个组件对应了一个继承了 `MonoBehavior` 的子类。当一个脚本中包含了一个 `MonoBehavior` 的子类，它就可以被添加到某个游戏对象上，赋予这个游戏对象某些功能。
    * 自定义组件可以在 Inspector 中暴露属性或方法，使得它们可以在运行时被执行或修改。事实上，对 Inspector 可执行的操作相当灵活。

## Runtime Access

### Access GameObjects

获取当前脚本附着的游戏对象 `this.gameObject` 

通过场景里面的名字或者一个路径（绝对路径以'/'打头，可以是相对路径）直接获取游戏对象：`GameObject go = GameObject.Find(“GameObject”); 　　GameObject go = GameObject.Find(“GameObject/Cube”);` 

通过Tag 获取单个游戏对象：`GameObject.FindWithTag(“tag”)` 

通过Tag 获取多组游戏对象：`GameObject.FindGameObjectsWithTag(“tag”)` 

Use tag to filter out objects:
    - use `CompareTag`: https://docs.unity3d.com/ScriptReference/Component.CompareTag.html
    - For collision detection, the layer mask way is slightly more efficient (sure it depends after all)
    - It's also useful to use `FindGameObjectsWithTag`.

ref: http://unity3d.com/support/documentation/ScriptReference/GameObject.FindGameObjectsWithTag.html

### Access Components

获取组件 `GetComponent`  

`gameObject.GetComponent<ComponentClass>()`可获取任一对象 `gameObject` 的相应组件`ComponentClass` 
    * `gameObject.GetComponentInChildren<ComponentClass>()`DFS 获取子对象（包括自身）的任意该类型组件
    * `gameObject.GetComponentsInChildren<ComponentClass>()`获取子对象（包括自身）的所有该类型组件，返回列表，可以通过查看组件的 `name`  （就是其 `gameObject` 的`name` ）来分辨是否为所需的组件。


