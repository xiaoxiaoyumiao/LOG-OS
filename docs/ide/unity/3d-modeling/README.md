# 3D Modeling

欢迎进入 3D 世界！

## Mesh, Materials & Textures

这三种对象的概念与 3D 建模中的相应概念基本一致。Mesh 如同字面含义，储存了一个 3D 对象的结构和渲染信息。图形处理器在渲染一个 3D 模型时，会获取到它所有顶点的位置、颜色等信息以及各个顶点如何构成一个个三角面，然后从顶点开始一步步渲染成一个立体的图样。Mesh 储存了这个过程所需的大部分信息，当然它所应具备的最基本的数据就是一个指示所有顶点的列表和一个指示所有三角面的列表。

Material 决定如何由 Mesh 数据渲染一个模型。模型能呈现出或陶瓷或金属的质感，即是由 Material 实现的。事实上 Material 包含了 shader，也就是定义了处理器渲染策略的函数。Material 是与 Mesh 相解离的概念，一个 material 可以被各种不同的 mesh 使用，一个 mesh 也可以持有多个 material。有的模型表面是更复杂的图片，其相应的 Material 就需要携带这一图片信息（也就是常说的贴图）。Texture 代表一类具有特殊用途的图片数据，当使用它而非 Sprite 时，往往意味着场景与渲染紧密相关。如果需要为 mesh 赋予一个贴图，首先需要创建相应的 texture，然后将这个 texture 赋予一个 material，最后将 material 赋予 mesh（准确来说，是 mesh 的 renderer 组件）。这一过程的逻辑和 3D 建模中赋予贴图的逻辑一致。

在项目中，一个模型的数据可以被组织为 Materials, Mesh, Textures 三个子目录。

Unity 支持 fbx 格式的模型文件。直接将其拖入项目目录，Unity 即可完成对模型信息的解析。在 Project 面板中可以查看模型信息，其包含的各个对象及其链接关系都会被保留下来。对其解析结果类似一个 Prefab，它包含了 mesh、material（如果导出的模型包含了材质和贴图）以及起辅助作用的骨骼、样条等对象。简而言之，导出的东西在解析后都能看到。（注意不要放在 StreamingAssets 目录下。）

## Reference

\[1\] [https://docs.unity3d.com/Manual/3D-formats.html](https://docs.unity3d.com/Manual/3D-formats.html)

\[2\] tips for importing fbx: [https://blog.csdn.net/lly20000/article/details/45508347](https://blog.csdn.net/lly20000/article/details/45508347)

\[3\] tips for working with 3ds max: [https://blog.csdn.net/chenghai37/article/details/49999449?locationNum=15&fps=1](https://blog.csdn.net/chenghai37/article/details/49999449?locationNum=15&fps=1)

