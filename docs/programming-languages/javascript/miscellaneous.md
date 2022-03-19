# Miscellaneous

* JS 没有常量的概念
  * 订正：ES2015 有了。
* JS 没有权限（公有和私有）的概念
* JS 没有枚举的概念。不追求安全的情形下用结构体实现即可，否则：
  * [https://stackoverflow.com/questions/287903/what-is-the-preferred-syntax-for-defining-enums-in-javascript](https://stackoverflow.com/questions/287903/what-is-the-preferred-syntax-for-defining-enums-in-javascript)
* 关于在构造器中使用访问器
  * 使用 Object.defineProperties 方法
    * [https://stackoverflow.com/questions/5222209/getter-setter-in-constructor](https://stackoverflow.com/questions/5222209/getter-setter-in-constructor)
* 关于文件命名规范
  * 字母全部小写
  * 不要带空格
  * 用破折号（-）连接单词
  * 库文件可用逗点（.），用于体现版本或从属关系
  * ```text
    vue.min.js
    vue-router.js
    jquery.form.js
    jquery-1.4.2.min.js
    ```
  * ref: [https://developer.aliyun.com/article/202570](https://developer.aliyun.com/article/202570)
* 关于整数
  * JS 中表示数字的只有 Numbers 这个类，表示法统一为 64 位的浮点数。整数绝对值的上界为 2^53. \[ TODO 整数的单独章节 \]
* 关于无符号整数
  * JS 没有无符号类型的说法，如果一定要把某个数强转为无符号整数，可以使用 &gt;&gt;&gt; 算符。它在右移时使用 0 填充高位，且一定返回无符号整数。
  * ref: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned\_right\_shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Unsigned_right_shift)
* 关于数组
  * new Array\(x\) 似乎并不是被鼓励的语法。推荐直接使用 \[\] 初始化一个数组（或许更接近列表）。
  * 拷贝 ArrayBuffer 内容的比较舒适的写法：
  * ```text
    function copy(src)  {
        var dst = new ArrayBuffer(src.byteLength);
        new Uint8Array(dst).set(new Uint8Array(src));
        return dst;
    }
    ```
* console.assert 打印的异常并不会被 try - catch 捕捉到。
* 检查一个对象是否是一个函数
  * ```text
    if (typeof v === 'function') {
        // do something
    }
    ```
* 除了 TextEncoder / TextDecoder，Buffer 也可以方便地起到字符串和 ArrayBuffer 转换的效果。
  * ```text
    const arrayBuffer = new ArrayBuffer(16);
    const buffer = Buffer.from(arrayBuffer);
    // buffer to string
    buffer.toString(encoding, start, end);
    ```

    * [https://nodejs.org/api/buffer.html\#buffer\_buf\_buffer](https://nodejs.org/api/buffer.html#buffer_buf_buffer)
* Array 的 forEach 方法可以方便地顺序遍历元素。
  * [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Array/forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
* 关于随机数：使用`Math.random()` 生成
* ```text
  function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
  }
  ```

  * [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Math/random](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random)

