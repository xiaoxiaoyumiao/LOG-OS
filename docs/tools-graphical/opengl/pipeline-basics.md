# Pipeline Basics

## Introduction

* 图形显示也就是将希望绘制的 2D 或 3D 对象经过一系列变换而投影到像素构成的 2D 屏幕上。这一系列操作是由一个 pipeline 完成的。
* Graphics pipeline 大体上有两个步骤：第一步将对象投影到二维，第二步将对象映射到有色的像素。
* 具体而言，在 pipeline 的每一个阶段，显卡都（常常是高度并行地）对图形数据（的每个基本元素）执行一个特定的程序，这个程序称作 shader。
* 开发者可以使用 **OpenGL Shading Language / GLSL** 重新编写其中一些阶段的 shader，这为图形渲染实现提供了极高的灵活性。
* pipeline 一般而言（按阶段的执行顺序）如下构成：
  * **Vertex Data** - _\*\*_输入，顶点数据集合（其实并不是一个阶段）
  * **Vertex Shader** - 接受一个 vertex 的数据，执行坐标变换和其他对顶点数据的基本操作
  * **Primitive Assembly** - 接受所有 vertex 的数据，将顶点组织为 primitive，例如三角形。
  * **Geometry Shader** - 接受构成一个 primitive 的顶点数据，能够重构 primitive 的几何形状。
  * **Rasterization** - 接受所有 primitive 的数据，映射到屏幕上的像素点。用来渲染一个像素的数据被称为 fragment。Rasterization 从 primitives 生成 fragments，并执行 clipping。clipping 指的是把屏幕之外的 fragments 丢弃。
  * **Fragment Shader** - 接受一个 fragment 的数据，决定一个像素最终的颜色。
  * **Alpha Test & Blending** - 接受所有 fragment 的数据，计算 fragment 之间的重叠关系以及颜色的融合。
* Vertex shader 和 fragment shader 是开发者必须实现的。

## Pipeline

假设我们要渲染一个三角形。

### Vertex Data

#### Initialize

顶点数据应当组织为一个字节序列的形式（例如 C 数组），但顶点的各个属性在序列中如何排布是可以由开发者指定的，之后会介绍如何指定顶点数据的解析方法。

基本的顶点数据包含每个顶点的坐标信息。例如使用以下结构依次定义三角形的三个顶点：

```cpp
float vertices[] = {
     -0.5f, -0.5f, 0.0f, // first vertex
     0.5f, -0.5f, 0.0f,  // second vertex
     0.0f,  0.5f, 0.0f   // third vertex
}
```

* **normalized device coordinates / NDC** 注意到每个坐标分量都设定成了 \(-1, 1\) 之间的浮点数。这里的坐标采用的是 normalized device coordinates / NDC，坐标系的原点在屏幕正中央，向右为 x 轴正方向，向上为 y 轴正方向，坐标轴与屏幕边界的交点到原点的距离取为相应坐标轴的单位 1。因此在对顶点做坐标变换后，坐标分量 \(-1, 1\) 范围以外的坐标都会被丢弃。
  * 接下来我们不会对坐标做实质性的变换，所以在这里直接将坐标设置为 NDC 下三角形的期望位置。
  * 我们已经使用过 `glViewport` 来设置显示区域的大小。NDC 下的坐标会根据这一信息，经过 viewport transform 变换到实际的屏幕坐标系。fragments 使用的就是屏幕坐标系。

#### Bind to an Object

为了让 OpenGL 能够使用这个字节序列，需要把字节序列填充到一个 OpenGL 对象里。

buffer object 是可以维护缓存的对象，通过 `glGenBuffers` 可以获取到一个 buffer object。准确来说，获取到的是对象的一个 unique ID，因此是 unsigned int 类型的。

OpenGL 是一个巨大的状态机，为了能够执行操作，需要先设定好 context。为了操作一个 buffer object，也需要在 context 中指定这个 object。

context 包含了多种类型的 buffer 标识符，不同类型代表一个 buffer 的不同使用方式。通过 `glBindBuffer` 可以将一个 buffer object 绑定到一个特定类型的 buffer 标识符上，之后就可以通过引用这个标识符来操作这个 buffer object 了。

通过 `glBufferData` ，可以把字节序列填充到给定的 buffer 标识符绑定的对象里。

```cpp
// generate a buffer object and get unique id
unsigned int VBO; 
// 1: number, number of buffer object to generate
// &VBO: pointer to an uint array to store the generated id(s)
glGenBuffers(1, &VBO);   
// bind created object to context
glBindBuffer(GL_ARRAY_BUFFER, VBO);   
// copy buffer data into the object 
// GL_ARRAY_BUFFER: the buffer identifier
// sizeof(vertices): size of data
// vertices: data
// GL_STATIC_DRAW: indicating how we want the data to be managed
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
```

> The fourth parameter specifies how we want the graphics card to manage the given data. This can take 3 forms:
>
> * GL\_STREAM\_DRAW: the data is set only once and used by the GPU at most a few times.
> * GL\_STATIC\_DRAW: the data is set only once and used many times.
> * GL\_DYNAMIC\_DRAW: the data is changed a lot and used many times.

### Vertex Shader

定义一个 shader 分为两步：使用 GLSL 编写一个 shader；使用 OpenGL 接口编译这个 shader。这里暂时不展开 GLSL 的编写，而只给出样例和简单的解释：

```cpp
#version 330 core
layout (location = 0) in vec3 aPos;

void main()
{
    gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
}
```

* 第一行指定 GLSL 的版本。OpenGL 3.3 开始 GLSL 和 OpenGL 的版本号是同步的。
* 第二行定义了 shader 的一个输入变量 aPos。
  * `layout (location = 0)` 指定变量的位置。在 OpenGL 主过程中，要操作一个 shader 中定义的变量需要预先知道这个变量的位置。这个位置可以通过 layout location 手动指定，也可以不指定而通过特定接口取得。在 GLSL 编写中会介绍关于 location 的细节。
  * `in` 指示了这个变量用来接收 shader 的输入数据。对于这个 shader 而言，是 vertex 的位置。
  * `vec3` 指示了这个变量的类型。`vec3` 是浮点 3D 向量。OpenGL 中 `vec` 加上一个数字 n 表示 n 维的向量类型。n 可以是 1 到 4。
  * `aPos` 是这个变量的名字。
* 下面定义了一个 main 函数表示 shader 处理数据的主过程。
  * `gl_Position` 是 GLSL 的预定义变量，它是 vertex shader 将输出的顶点位置信息，并且是一个 4D 向量。
  * 随后的语句构建了一个 4D 向量。可以使用 `x` ,`y`, `z` ,`w` 来引用一个 `vec` 的各个维度。
  * 可以看到这个 shader 并没有实质性地改变坐标。

#### Compiling Shader

配置 shader 的过程比配置 buffer 要稍微方便一些。

```cpp
const char *vertexShaderSource = "#version 330 core\n"
    "layout (location = 0) in vec3 aPos;\n"
    "void main()\n"
    "{\n"
    "   gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n"
    "}\0";

// get a shader
unsigned int vertexShader;
vertexShader = glCreateShader(GL_VERTEX_SHADER);

// bind (an array of) shader source code to the shader
// vertexShader : shader， the shader to which source code is given
// 1: count, element count of the code array
// &vertexShaderSource: pointer to the code array
// NULL: length, an array of string length, omitted here
glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
glCompileShader(vertexShader);

// some code to check if the compiling process succeeded
int  success;
char infoLog[512];
glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &success);
if(!success)
{
    glGetShaderInfoLog(vertexShader, 512, NULL, infoLog);
    std::cout << "ERROR::SHADER::VERTEX::COMPILATION_FAILED\n" << infoLog << std::endl;
}
```

### Fragment Shader

类似地构建一个 fragment shader，它赋予这个三角形中所有的像素同一种颜色。

```cpp
#version 330 core
out vec4 FragColor;

void main()
{
    FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);
}
```

* 注意这里我们使用 out 关键字定义了一个输出变量。

编译：

```cpp
unsigned int fragmentShader;
fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
glCompileShader(fragmentShader);
```

### Shader Program

OpenGL 需要知道 shader 的连接关系。通过 program 对象可以做到这一点：

```cpp
// create a program
unsigned int shaderProgram;
shaderProgram = glCreateProgram();

// attach shader to the program
glAttachShader(shaderProgram, vertexShader);
glAttachShader(shaderProgram, fragmentShader);

// link the program
glLinkProgram(shaderProgram);

// some code to check if the linking process succeeded
glGetProgramiv(shaderProgram, GL_LINK_STATUS, &success);
if(!success) {
    glGetProgramInfoLog(shaderProgram, 512, NULL, infoLog);
    ...
}

// register program to context
glUseProgram(shaderProgram);

// we can delete the shader objects now
glDeleteShader(vertexShader);
glDeleteShader(fragmentShader);
```

### Linking Vertex Attributes

现在我们需要告知 OpenGL 如何从我们定义的 vertex data 中解析 vertex shader 所需的输入数据。对于 vertex shader 而言，输入变量也叫 **vertex attribute**。

注意到我们定义的数据是一个 float 数组，每个元素宽度为 4 字节，因此每个顶点的位置数据占据 12 字节宽度。把 buffer object 绑定到 context 之后，就可以通过 `glVertexAttribPointer` 为指定某个的 shader 变量提供解析这个 buffer object 的方法：

```cpp
// 0: index, the location of shader variable 
//     (we set location of aPos to be 0 in shader, so this function will
//     configure the pointer for aPos)
// 3: size, the number of components of this vertex attribute
//     (aPos is a vec3, so it has 3 components)
// GL_FLOAT: data type of the attribute
// GL_FALSE: normalized, indicating whether to normalize the vector
// 3 * sizeof(float): stride, indicating stride of vertex data in the array
//     (stride, or distance between adjacent pos vectors, is 3 * 4 bytes)
// (void*)0: pointer, indicating start of the array
//     (because we are using a buffer, it's 0 indicating that 
//     data of first vertex just lies at the start of the array 
//     but we need to convert it to a pointer type.
//     and there are times when we do not bind a buffer)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);

// enable attribute array for a provided index
// when enabled, the data in the bound buffer will be used for rendering
// 0 indicating location of the variable, so it's aPos here
glEnableVertexAttribArray(0);
```

创建和绑定 vertex attribute 的整个过程显得较为繁琐。使用 Vertex Array Object 可以帮助保存相关的上下文配置，节省绑定需要的代码量。

### Vertex Array

Vertex Array Object 会保存如下信息：

> * Calls to glEnableVertexAttribArray or glDisableVertexAttribArray.
> * Vertex attribute configurations via glVertexAttribPointer.
> * Vertex buffer objects associated with vertex attributes by calls to glVertexAttribPointer.

```cpp
// generate a vertex array
unsigned int VAO;
// 1: number
// &VAO: pointer to an array of uint
glGenVertexArrays(1, &VAO);  
// bind Vertex Array Object
glBindVertexArray(VAO);

// operations binding attributes

// copy our vertices array in a buffer for OpenGL to use
glBindBuffer(GL_ARRAY_BUFFER, VBO);
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
// then set our vertex attributes pointers
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
glEnableVertexAttribArray(0); 

// ...

// start rendering

// use shader program 
glUseProgram(shaderProgram);
// bind the vertex array to apply the configuration
glBindVertexArray(VAO);
// and then draw things
```

### Draw Arrays

以下调用将使用 vertex array 中的 3 个点绘制三角形。

```cpp
// draw using defined shaders and vertex attribute configurations
// GL_TRIANGLES: mode, indicate the primitive to use
//     The primitive can also be lines, quads and polygons
// 0: first, the starting index of the vertex array
// 3: count, the number of vertices to render
glDrawArrays(GL_TRIANGLES, 0, 3);
```

### Element Buffer

当绘制更复杂的图形时，我们需要指定如何连接给定的各个顶点来构造 primitive。这时可以使用上下文中的 element array buffer 类型。假设要绘制一个四边形。

```cpp
float vertices[] = {
     0.5f,  0.5f, 0.0f,  // top right
     0.5f, -0.5f, 0.0f,  // bottom right
    -0.5f, -0.5f, 0.0f,  // bottom left
    -0.5f,  0.5f, 0.0f   // top left 
};
unsigned int indices[] = {  // note that we start from 0!
    0, 1, 3,   // first triangle
    1, 2, 3    // second triangle
};  

// generate a buffer object
unsigned int EBO;
glGenBuffers(1, &EBO);
// bind the object to element array buffer in context
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
// copy data to buffer object
glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW); 

// when drawing with elements:
// bind the object
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
// draw elements based on indexing on vertices
// GL_TRIANGLES: mode, indicating the primitive type
// 6:count, number of vertices to draw
// GL_UNSIGNED_INT:type, type of indices
// 0: indices, a pointer indicating start of the element array
glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
```

### Complete Code

```cpp
// ..:: Initialization code :: ..
// 1. bind Vertex Array Object
glBindVertexArray(VAO);
// 2. copy our vertices array in a vertex buffer for OpenGL to use
glBindBuffer(GL_ARRAY_BUFFER, VBO);
glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
// 3. copy our index array in a element buffer for OpenGL to use
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);
// 4. then set the vertex attributes pointers
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
glEnableVertexAttribArray(0);  

[...]

// ..:: Drawing code (in render loop) :: ..
glUseProgram(shaderProgram);
glBindVertexArray(VAO);
glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0)
glBindVertexArray(0);
```

## Reference

\[1\] [https://learnopengl.com/Getting-started/Hello-Triangle](https://learnopengl.com/Getting-started/Hello-Triangle)

\[2\] [https://www.khronos.org/registry/OpenGL-Refpages/es2.0/xhtml/glEnableVertexAttribArray.xml](https://www.khronos.org/registry/OpenGL-Refpages/es2.0/xhtml/glEnableVertexAttribArray.xml)

