# Event Handling

## Mouse Events

最直接的轮询方法：

`Input.mousePosition` 获取鼠标位置，`Screen` 获取屏幕信息

```text
鼠标事件，都是当鼠标和gui或者碰撞体（Collider）交互时候触发。
需要说明的是drag其实就是鼠标down后up之前持续每帧都会发送此消息。
​
OnMouseDown：当鼠标上的按钮被按下时触发的事件；
OnMouseDrag：当用户鼠标拖拽GUI元素或碰撞体时调用；
OnMouseEnter：当鼠标进入物体范围时被调用；
OnMouseExit：当鼠标退出时被调用；
OnMouseOver：当鼠标移动到某对象的上方时触发的事件；
OnMouseUp：当鼠标按键被松开时触发的事件
```

也可以注册触发器：

```csharp
public class StartGame : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        GetComponent<Button>().onClick.AddListener(onClick);
    }
​
    void onClick()
    {
        SceneManager.LoadScene("SelectLevel");
    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
```

[https://blog.csdn.net/tom\_221x/article/details/78457615](https://blog.csdn.net/tom_221x/article/details/78457615)

[https://docs.unity3d.com/Manual/ExecutionOrder.html](https://docs.unity3d.com/Manual/ExecutionOrder.html)

## Keyboard Events

```csharp
// key pressed down
if (Input.GetKey(KeyCode.W))
{
    // ...
}

// any key down
if (Input.anyKey){
    // ...
}

```

关于同时使用WASD和arrow控制的方案：

Edit -> roject Settings -> Input，Horizontal 和 Vertical 规定一套按键输入属性

ref: [https://www.jianshu.com/p/962e91c6e56c](https://www.jianshu.com/p/962e91c6e56c)

代码里用

```csharp
horizontal_axis_name = Horizontal;
h = Input.GetAxisRaw(horizontal_axis_name);
```

## UI Events

UI 的鼠标判断则需要借助事件系统：

```csharp
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;
 
public class ZhiShiKuUIChange : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler
{
    private Image image;
    public Sprite[] sprites;
 
    void Start()
    {
        image = GetComponent<Image>();
    }
 
    public void OnPointerEnter(PointerEventData eventData)
    {
        image.sprite = sprites[0];
    }
 
    public void OnPointerExit(PointerEventData eventData)
    {
        image.sprite = sprites[1];
    }
}
```

Button 组件的 onClick: 在该组件上按下鼠标后，仍在该组件上松开鼠标时触发。(ref: \[1])


## Input Action

Abstraction over a source of input.

```
    var action = new InputAction(binding: "<Gamepad>/buttonSouth");
    
    // Additional bindings can be added using `AddBinding`.
    action.AddBinding("<Mouse>/leftButton");
```

ref: https://docs.unity3d.com/Packages/com.unity.inputsystem@1.0/api/UnityEngine.InputSystem.InputAction.html

## References

\[1] [https://docs.unity3d.com/530/Documentation/ScriptReference/UI.Button-onClick.html](https://docs.unity3d.com/530/Documentation/ScriptReference/UI.Button-onClick.html)

