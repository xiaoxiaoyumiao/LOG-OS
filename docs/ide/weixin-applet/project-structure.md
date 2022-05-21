# Project Structure

## 小程序架构

一个典型的小程序项目结构为：

```text
|- app.js
|- app.json
|- app.wxss
|- sitemap.json
|- project.config.json
|- pages
  |- [page_name]
    |- [page_name].js
    |- [page_name].wxml
    |- [page_name].json
    |- [page_name].wxss
```

_\[ TODO - 请在这里添加到 JSON 语法介绍的链接 \]_

JSON 配置文件包含了键值对的列表。关于值的类型：

* 数字，包含浮点数和整数
* 字符串，需要包裹在双引号中
* Bool值，true 或者 false
* 数组，需要包裹在方括号中 \[\]
* 对象，需要包裹在大括号中 {} 
* Null

各个 JSON 文件的作用：

* project.config.json - 项目个性化配置 
* app.json - 适用于整个小程序的配置
  * pages 字段：小程序的所有页面路径，其第一个页面为启动小程序时首先看到的页面，即首页
* page.json - 单个页面配置 

WXML: 基本元素为组件。组件类似 HTML中的元素，用 `<type key=value><\type>` 格式构成。

> JS 可以通过DOM（ML文件的生成树）来控制界面（ML）元素。

更高级的开发模式是 MVVM，将渲染和逻辑分离：

```text
一个数据绑定案例；
ML:(view template)
<text>{{msg}}</text>
JS:(model)
this.setData({msg:"Hello World"})
```

WXSS: 类比 CSS，可以在 WXSS 文件中方便地创建样式的定义，供 WXML 的组件使用。

JS: 定义所有页面逻辑。例如，在组件属性中设置其回调函数（触发器），在JS代码中定义回调函数，即可以响应用户的点击等操作。

app.js - 定义APP实例，程序启动时首先触发 onLaunch

多数API的回调是异步回调。

