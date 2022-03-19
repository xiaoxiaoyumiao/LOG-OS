# Storage

## API

```javascript
/* store data in provided key */
wx.setStorage
/* field of parameter object
* key: string
* data: any
*/
wx.setStorageSync(string key, any data)

/* load data of provided key */
wx.getStorage
/* field of parameter object
* key: string
* parameter of callback on success:
* data: any
*/
wx.getStorageSync(string key) -> any

/* get information of all stored data */
wx.getStorageInfo
/* parameter of callback on success:
* keys: Array.<string> - all keys of stored data
* currentSize: number - current size of all data(KB)
* limitSize: number - bound of size of storage(KB)
*/
wx.getStorageInfoSync -> Object

/* remove data of provided key */
wx.removeStorage
/* field of parameter object
* key: string
*/
wx.removeStorageSync(string key)

/* clear all stored data */
wx.clearStorage
wx.clearStorageSync()
```

* 以 sync 结尾的函数是同步版本，否则为异步版本
* 异步版本的参数都是单个对象。除了拥有上面列出的 field 之外，它还可以拥有名为 success、fail、complete 的field，它们的取值为对应情形下的回调函数。
* data  只支持原生类型、Date、及能够通过`JSON.stringify`序列化的对象。

## Reference

\[1\] [https://developers.weixin.qq.com/miniprogram/dev/framework/ability/storage.html](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/storage.html)



