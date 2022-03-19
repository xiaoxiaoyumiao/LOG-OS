# Physics

## 帧与时间

Time.deltaTime获取上一帧历时秒数，应当在Update中调用。在 FixedUpdate 中调用时，它总是返回一个（和fixed 帧率相关的）常量，这方便进行一些物理计算（事实上 FixedUpdate 就是在 Update cycle 的物理计算子循环中）。但是 FixedUpdate 本身并不是严格按一定时间间隔执行，而是通过反复执行（或不执行）子循环来维持帧率恒定。

## 时间尺度TimeScale

`Time.TimeScale`可以用来设置时间流逝的快慢。对于有物理运算的场合，可能会导致物理模拟的不连续。

## 碰撞检测

UNITY的碰撞检测实际分为碰撞检测和触发检测两种。触发检测不会附带物理碰撞效果，通过trigger触发。

一个游戏对象的碰撞事件可以通过回调函数处理。例如 `OnCollisionEnter(Collision)` 。

ref: [https://docs.unity3d.com/ScriptReference/Collider.OnCollisionEnter.html](https://docs.unity3d.com/ScriptReference/Collider.OnCollisionEnter.html)

### **Ray**

使用Raycast可以方便地绘制射线、完成线和碰撞体的碰撞检测。

ref: [https://docs.unity3d.com/ScriptReference/Physics.Raycast.html](https://docs.unity3d.com/ScriptReference/Physics.Raycast.html)

ref: [https://blog.csdn.net/u010718707/article/details/42111567](https://blog.csdn.net/u010718707/article/details/42111567)

## Rigidbody

刚体组件使得其附着的游戏对象参与 Unity 物理引擎的模拟。其赋予游戏对象常见的位置、速度、角度等物理属性，并支持重力、阻力等常见物理参数的配置。若该组件被设置为运动学的（kinematic），那么其不再参与动力学计算，所有外力、碰撞、约束等不再影响其运动，其运动完全由开发者脚本控制。动力学（dynamic）刚体则受到力、碰撞、约束的作用。对刚体物理量的操作（无论是动力学的还是运动学的）都在 FixedUpdate 中计算为宜。静态（static）刚体适用于始终保持静止的游戏对象。

TODO 刚体的类型

直接修改 velocity 似乎并不是被官方推荐的做法，代替方案是使用 `AddForce` 并通过其参数设置相应的模式。

```csharp
 rigidbody.AddForce(new Vector3(xSpeed, 0, 0), ForceMode.VelocityChange);
```

ref: [https://docs.unity3d.com/ScriptReference/Rigidbody-velocity.html](https://docs.unity3d.com/ScriptReference/Rigidbody-velocity.html)

ref: [https://docs.unity3d.com/ScriptReference/Rigidbody.html](https://docs.unity3d.com/ScriptReference/Rigidbody.html)

ref: [https://answers.unity.com/questions/653793/cant-move-player-with-rigidbodyvelocity.html](https://answers.unity.com/questions/653793/cant-move-player-with-rigidbodyvelocity.html)

## Collider

碰撞体组件使得一个游戏对象可以触发碰撞事件。如果一个刚体需要发生碰撞，那么它应当具有碰撞体组件；但碰撞体却并不一定要是刚体，例如一些静态的地形。（按照 ref\[1\]，它会与一个全局的静态刚体关联。）常用的碰撞体有 BoxCollider\(2D\)，SphereCollider，PolygonCollider2D，CircleCollider2D 等。

ref\[1\]: [https://docs.unity3d.com/ScriptReference/Collider2D-attachedRigidbody.html](https://docs.unity3d.com/ScriptReference/Collider2D-attachedRigidbody.html)

## 获取模型碰撞点的 UV 坐标

```csharp
// example 1
public void OnCollisionEnter( Collision collision )
{
    RaycastHit hit = new RaycastHit();
    Ray ray = new Ray( collision.contacts[ 0 ].point -collision.contacts[ 0 ].normal, collision.contacts[ 0 ].normal );
    if( Physics.Raycast( ray, out hit ) ){
        Print( hit.textureCoord );
    }
}

// example 2
void Update ()
{
    if (!Input.Get$$anonymous$$ouseButton (0))
        return;

    RaycastHit hit;
    if (!Physics.Raycast (Camera.main.ScreenPointToRay (Input.mousePosition), out hit))
         return;

    Renderer renderer = hit.collider.renderer;
    MeshCollider meshCollider = hit.collider as MeshCollider;
    if (renderer == null || renderer.sharedMaterial == null || 
        renderer.sharedMaterial.mainTexture == null || meshCollider == null)
        return;

    Texture2D tex = (Texture2D)renderer.material.mainTexture;
    Vector2 pixelUV = hit.textureCoord;
    print ((int)(pixelUV.x * renderer.material.mainTexture.width) + "--" + 
        (int)(pixelUV.y * renderer.material.mainTexture.height));
}
```

ref: [https://forum.unity.com/threads/get-uv-coordinate-from-collision.12720/](https://forum.unity.com/threads/get-uv-coordinate-from-collision.12720/)

ref: [https://docs.unity3d.com/ScriptReference/RaycastHit-textureCoord.html](https://docs.unity3d.com/ScriptReference/RaycastHit-textureCoord.html)

ref: [https://answers.unity.com/questions/623135/how-to-get-pixel-position-when-clicking-an-object-.html](https://answers.unity.com/questions/623135/how-to-get-pixel-position-when-clicking-an-object-.html)

## Gravity

模型不服从重力的种种可能原因：

ref: [https://forum.unity.com/threads/gravity-not-working-on-rigidbody.48036/](https://forum.unity.com/threads/gravity-not-working-on-rigidbody.48036/)

