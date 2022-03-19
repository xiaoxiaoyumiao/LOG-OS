# Weixin Applet

## 小程序架构

app.js app.json app.wxss pages js wxml json wxss

JSON: project.config.json - 项目个性化配置 app.json - 适用于整个小程序的配置 page.json - 单个页面配置 pages:小程序的所有页面路径，其第一个页面为首页 JSON语法：{"key":value,...} 数字，包含浮点数和整数 字符串，需要包裹在双引号中 Bool值，true 或者 false 数组，需要包裹在方括号中 \[\] 对象，需要包裹在大括号中 {} Null

WXML: 组件：类似HTML中的元素，用\格式构成 JS可以通过DOM（ML文件的生成树）来控制界面（ML）元素 更高级的开发模式是MVVM，将渲染和逻辑分离：

```text
一个数据绑定案例；
ML:(view template)
<text>{{msg}}</text>
JS:(model)
this.setData({msg:"Hello World"})
```

WXSS: 就是CSS。

JS: 在组件属性中设置其回调函数（触发器），在JS代码中定义回调函数，从而响应用户操作。 app.js - 定义APP实例，程序启动时首先触发onLaunch 多数API的回调是异步回调。

