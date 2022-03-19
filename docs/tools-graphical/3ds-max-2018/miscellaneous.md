# Miscellaneous

* Basic Concepts
  * 6 个基本面板
    * Create
      * icon 是一个加号。用于创建各种建模所需的基本元素。
    * Modify
      * icon 是一个自由变换框。用于展示和修改一个对象的各种性质。
    * Hierarchy
      * icon 是一个二叉树。用于设置对象的 Pivot、对象之间的关系（如 alignment 和 IK）。
    * Motion
      * icon 是一个移动的球。用于管理对象的运动。
    * Display
    * Utilities
  * Primitive
    * 在 Create 面板里可以创建的各种 Object
  * Editable Poly / 可编辑多边形
    * 类似于打散，把创建的 primitive 转换为一个可编辑多边形（有点像向上类型转换，可编辑多边形是各种 primitive 的基类），转换后可以自由编辑其顶点和边，但是作为 primitive 时的各种属性（例如圆柱才有的高和半径的属性）会失效
    * 可编辑多边形包含五种类型的元素集合（它们之间有重合）：
      * Vertex：就是顶点。
      * Edge：就是边。
      * Polygon：边围成的、内部不包含边的多边形。就是基本多边形。
      * Border：所有不作为两个多边形交界的边。就是边界。
      * Element：应当是单个连通的整体。
    * 在 Modify - Selection 中可以选择当前仅可选择哪一类型的元素。这可以避免错误。
    * 在 Modify - selection 中的 Ring 和 Loop 可以批量地选择元素。例如当元素为边时， Ring 可以选择与当前选中的边处在同一环面上的所有边，Loop 则会选择与当前选中的边处在同一环线上的所有边。（但需要保证邻近没有怪异的多边形，一般在临近面都是四边形时用）
      * 某些形状（例如圆柱）的底面上的环线因为和底面这个多边形相邻而无法被识别为环线，而如果这个底面多边形被移除，环线就可以被识别了。
    * 选中的元素可以被自由修改，此时其他的元素会相应发生变化来适应对选中元素的修改。例如拖动边或者顶点，会导致其关联的多边形也随之变形。增加边一般也会带来多边形的增加。
  * 以下对各个元素的操作都可以通过右键或 Modify 面板选择。
  * Vertex
    * Collapse：将顶点合成为单个顶点。
    * Weld：将两个顶点合成为一个。
    * Target Weld：将一个顶点焊接到另一个顶点。
  * Edge
    * Connect：连接。将选中的（多条）边按一定的分比从中间取点后连接为环线。可以在连接时设置每条边取点的数量（也就是将会增加的环线的数量）
    * Chamfer：将边沿环面拆为多条边。
    * Bridge：在两条边之间添加一个新的多边形。
  * Geometry
    * Attach：将一个对象和另一个对象组合，从而可以作为一个对象同时编辑。
    * Cut：在边上取点并自由切割多边形。
* Modifiers
  * TurboSmooth 把 lowpoly mesh 平滑为一个 highpoly mesh
* Tranforms
  * Select and Move\(Moving\) - W
  * Select and Rotate\(Rotating\) - E
  * Select and Uniform Scale\(Scaling\) - R
* VIewport switching - second \[...\] at top-left of the view, click it to view options:
  * Perspective - P
  * Orthographic - U
  * Top - T
  * Bottom - B
  * Front - F
  * Left - L
* alt+X - see through \(select object - right click object - object properties - toggle or untoggle see-through \)
* Selection Set: 
  * This function can help create a set of objects to help re-selection become easier.
  * select objects - Toolbar - Create Selection Set - enter new name
* UV mapping
  * Use Unwrap UVW modifier for complex mesh and UVW map for simple primitives.
  * Rough steps: add modifier - select edges and convert to seams - UV editor - peel the meshes split by seams - reshape peeled meshes to fit into the square grid - use the colored texture to ensure meshes are peeled properly - export UV mapping for composing custom textures
  * [https://www.youtube.com/watch?v=SQak9sQh8uw](https://www.youtube.com/watch?v=SQak9sQh8uw)
  * [https://www.youtube.com/watch?v=aMCWmnml0o0](https://www.youtube.com/watch?v=aMCWmnml0o0)

## Reference

\[1\] 人体建模入门教程：[https://www.youtube.com/watch?v=R8VDrIg1BXU](https://www.youtube.com/watch?v=R8VDrIg1BXU)

