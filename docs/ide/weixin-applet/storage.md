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

## Cloud

* 在微信公众平台中可以为小程序免费开启云开发功能，获得一个自命名的云开发环境，它包含了一定的存储空间。
* 点击开发者工具工具栏中的云开发，可以打开云开发控制台，在这里可以管理云存储空间中的文件。
* 在 `App` 的 `OnLaunch` 中初始化云环境：

```javascript
onLaunch: function () { 
    wx.cloud.init({
      env: "environment-id" // 这里填写公众平台上创建的云环境的 ID
    })
  },
```

从云空间下载文件，使用 `wx.cloud.downloadFile` 接口：

```javascript
function downloadFromCloud(url) {
  return wx.cloud.downloadFile({ fileID: url })
    .then( ... )
}
```

文件的 URL 在上传文件时就可以看到。

## Reference

\[1\] [https://developers.weixin.qq.com/miniprogram/dev/framework/ability/storage.html](https://developers.weixin.qq.com/miniprogram/dev/framework/ability/storage.html)

\[2\] [https://developers.weixin.qq.com/miniprogram/dev/wxcloud/guide/storage/api.html](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/guide/storage/api.html)

\[3\] [https://developers.weixin.qq.com/miniprogram/dev/wxcloud/reference-sdk-api/storage/Cloud.uploadFile.html](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/reference-sdk-api/storage/Cloud.uploadFile.html)

\[4\] [https://blog.csdn.net/Panda325/article/details/108111212](https://blog.csdn.net/Panda325/article/details/108111212)

