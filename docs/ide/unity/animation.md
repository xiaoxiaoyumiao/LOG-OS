# Animation

## Animator

* Animator 是 unity 提供的一种 component，负责为一个对象提供动画效果。事实上，Animator 可以控制其附着的对象拥有的（任何？）组件的属性，而 SpriteRenderer 和 Transform 是其可控的组件中常用的两种。通过控制 SpriteRenderer 的 sprite 属性，就可以制造出逐帧动画；而通过修改 Transform 组件中的位置、角度或缩放则可以在 unity 中制造光滑的动画。
* Animator 拥有一个 Controller 属性，它指示这个 Animator 使用的 Animator Controller。Animator Controller 是一种资源文件，包含了关于动画状态机的所有信息，它可以用 Animator 窗口来查看。
  * 作为演示范例，可以如下为逐帧动画创建 Animator Controller：将一堆连续编号的帧素材（比如 png 文件）拖拽到 Hierarchy 窗口，unity 会提示选择一个地方存储由这些动画帧创建的 .anim 文件。这样的文件描述了一个 Motion（或叫 Animation Clip 或 Animation；我们在下面会进一步解释 Motion\)。确定之后，在与这个 Motion 文件相同的目录下还会出现一个 .controller 文件，这就是 Animator Controller。双击就可以打开 Animator 窗口来浏览它。此外，在 Hierarchy 窗口中还出现了一个新的游戏对象，它自动带上了 Animator 组件，并且这个组件的 controller 就是新创建的 controller。
  * 正常的创建方式似乎是选中对象后在 Animation 窗口中选择 Create New Clip。
* 通过 Animator 窗口可以看到，controller 包含了一个 Layer tab、一个 Parameter tab、一个绘出了由箭头连接的若干矩形。每个矩形代表了一个 AnimatorState，并带有一个名字。每个箭头代表一个 Transition。AnimatorState（以下简称 state）和 transition 是状态机的基本元素。
  * 有一些 state 具有特殊的颜色和名字，它们有别于普通的灰色的 state。如 AnyState 表示状态机中的任何状态，这有助于更容易地绘制涉及所有状态的转移规律。
* 先简要介绍 state 和 transition 的意义。
  * state 描述了动画状态机的一个状态，当被 controller 控制着的游戏对象处于一个状态时，它会做这个状态定义的运动，可能是贴图的连续变化（那样就成为了逐帧动画），也可能是其子对象的物理运动，或者其他。
  * transition 描述了 state 到 state 的一个转移，它总是带有条件。当条件满足，游戏对象就可以从 transition 的源状态通过 transition 到达目标状态。当游戏对象处于一个转移时，它会表现出转移所定义的中间过渡状态。
* 点击一个 state（矩形）可以在 Inspector 中查看它的各种属性。最重要的是 Motion 和 Transitions。
  * Motion 属性指向一个 .anim 文件，它刻画了当游戏对象处在这个 state 时应该按照什么方式“运动”。
  * Transitions 包含了由当前 state 指向其他 state 的所有 Transition。这是一个列表。这个列表中可能同时有多个 transition 的条件被满足，如果这种情况发生，最靠前的 transition 会被执行。可以拖动改变 transition 的顺序。列表中每个 transition 有 Solo 和 Mute 两个布尔属性，如果有 transition 是 Solo 的，那么其余那些没有勾选 Solo 的会被禁用（不论有没有勾选 Mute）；而勾选 Mute 的 transition 也会被禁用。一个 transition 的 Mute 优先于 Solo 判定。
* 点击一个 transition（箭头）可以在 Inspector 中查看它的各种属性。在这里也可以设置 transition 的 solo 和mute 属性。下面给出了 transition 的条件设置。Conditions 为条件的列表（我们会在下面给出对条件的解释）；还有一个特殊的条件在上方给出，即 Has Exit Time。若勾选 Has Exit Time，就相当于附加了一个条件：Motion 必须运行到结尾。当且仅当这些条件都成立的时候，transition 才会发动。
* 在解释条件之前，需要先解释 Parameters tab。Parameters 维护了状态机的所有状态变量，可在 Animator 窗口中任意增减。一共可创建四类状态变量：Int, Float, Bool 和 Trigger。而一个条件就是关于某个 Parameters 中的变量的表达式。
  * 前三个变量类型是平凡的，最后一个为触发器，它和 Bool 仅有一点不同：可以认为它默认为假且只能被用户置为真，并且在触发了一次转移之后，会被置为假。
  * 在 Parameters 中可以设置变量的默认值；在代码里可以通过 Animator 组件提供的 Set 和 Get 接口实现变量的查和改（具体来说，接口名称取决于要查或改的变量类型，如一个 Bool 类型的变量的 Set 函数为 `SetBool`）。
* 通过 Layers 可以实现状态机嵌套等操作，因未尝试（且不适宜建造过于复杂的状态机）故不做记录。
* 下面介绍 Animation 窗口，通过它可以编辑 Animation Clip / Motion。双击状态或 .anim 文件都可以打开这个窗口。它表现为一个时间轴，轴的每行维护一个组件属性（Property）的关键帧。为了修改 animation，必须选中一个具体的游戏对象，因为 animation 可控制哪些组件和子对象的组件显然是依赖于具体对象的。选中后，Add Property 按钮就会亮起。
  * 通过 Property 列表上方的下拉菜单可以方便地在这个游戏对象拥有的各个 animation 之间切换。
  * 如果添加了一个 SpriteRenderer 的 sprite 属性，把图片序列直接拖进时间轴的相应行可以快速创建逐帧动画。
  * 时间轴上的白色竖线（可称为指针）指向当前对象所处的帧。如果该 animation 对应的游戏对象被选中了，那么拖动指针就可以看到游戏对象的样子按照时间轴中的设置在连续变化。Property 列表中以文本框显示 各个 property 在指针所指的时刻的取值，可以通过编辑这些文本框来编辑指针所指的帧。可以通过顶部的文本框让指针指向相应序号的帧。
* 进阶、代码和坑：
  * 每个 state 有一个 Speed 属性，可以设置该状态运行时的速度。当速度为负数时，state 会倒放。勾选其 Multiplier 可以使用一个 float 状态变量作为速度的因子，控制加减速乃至倒放。
  * 每个 .anim 有一个 Loop Time 属性，当勾选时 state 能够循环播放这个 animation，不选时则只会播放一次。**注意：无法 loop 的 animation 在一个倒放的状态中可能会发生状态机卡死的问题。**
  * 通过 `Animator.Play` 函数可以强制播放一个状态。
  * loop pose：[https://forum.unity.com/threads/loop-pose-is-misnamed-and-should-be-make-seamless-and-a-proper-looping-should-be-added.393182/](https://forum.unity.com/threads/loop-pose-is-misnamed-and-should-be-make-seamless-and-a-proper-looping-should-be-added.393182/)
  * Behavior：行为类可以监测动画状态机的运行状态。这需要继承 `StateMachineBehavior`。通过重写 `OnStateEnter`、`OnStateExit` 等方法可以在状态切换时干各种事情。点击 Layers 中的某一个 layer 或 Animator 界面的空白处可以看到 Inspector 中 layer 的属性下可以 Add Behavior，在这里把脚本挂上去就可以对整个 layer 里的状态进行检测（实际应该会为每个状态创造一个 Behavior 的实例），当然也可以挂在单个状态上，点击状态就可以看到。
  * 似乎没有太好的方法获取当前的状态名，而是只能获取到其 hash 值；但可以通过先计算所有状态名的 hash 值来构造映射。
  * ```text
    Animator animator = main.GetComponent<Animator>();
    AnimatorStateMachine stateMachine = ((AnimatorController)animator.runtimeAnimatorController).layers[0].stateMachine;
    List<string> names = stateMachine.states.Select(item => item.state.name).ToList();
    foreach (var name in names)
    {
        // hashTranslator.Add(Animator.StringToHash(name), name);
        hashTranslator[Animator.StringToHash(name)] = name;
    }
    ```
  * 暂时不知道如何修改一个 Motion 的 FPS。通过拖拽创建的第一个 Motion 是 12 FPS，但之后创建的都是 60 FPS，原因未知。
  * Mirror 可以镜像翻转一段动画。
  * 时间轴添加事件 [http://www.xuanyusong.com/archives/2246](http://www.xuanyusong.com/archives/2246)
  * 可以在 Inspector 预览一段 Motion 的效果，不过需要把游戏对象拖到预览窗口里作为模型。

## Reference

\[1\] [https://www.jianshu.com/p/252c18016b3f](https://www.jianshu.com/p/252c18016b3f)

\[2\] [http://dotween.demigiant.com/download.php](http://dotween.demigiant.com/download.php)

