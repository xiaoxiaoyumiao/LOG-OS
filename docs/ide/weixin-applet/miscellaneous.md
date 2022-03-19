# Miscellaneous

* 可以对 JS 代码做格式化。路径：编辑 - 格式化代码 \[ shift + alt + F \]
* 在开启 ES6 转 ES5 的选项时，使用生成器语法（`function*`）并不能被成功识别， 因此要么关闭选项，要么还是使用传统的返回闭包的 iterator 实现方案。
* 小程序的断点调试
  * [https://blog.csdn.net/zxy9602/article/details/79603547](https://blog.csdn.net/zxy9602/article/details/79603547)
* wxss 渲染中无法使用本地路径访问资源，需要通过网络接口或者 base64 嵌入，否则会提示渲染层网络层 `-do-not-use-local-path-` 错误。
  * [https://www.ijiaoyu.org/info/6.html](https://www.ijiaoyu.org/info/6.html)
* 自定义 tabbar
  * 按照官方实现走就行，大体流程是在 app.json 中配置作为 tab 的页面路径，在根目录建立 custom-tab-bar 目录，在目录中建立组件，然后按照组件编写。
  * 比较头疼的是每个页面拥有自己的 tab bar 实例，导致要由每个 tab 来设置自己的 tabbar 的选中状态，切换 tab 的时候 tab bar 就会有短暂的闪烁。
  * [https://developers.weixin.qq.com/miniprogram/dev/framework/ability/custom-tabbar.html?search-key=%E8%87%AA%E5%AE%9A%E4%B9%89tabbar](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/custom-tabbar.html?search-key=%E8%87%AA%E5%AE%9A%E4%B9%89tabbar)
* 基础库各版本用户数量分布
  * [https://developers.weixin.qq.com/miniprogram/dev/framework/client-lib/version.html](https://developers.weixin.qq.com/miniprogram/dev/framework/client-lib/version.html)

