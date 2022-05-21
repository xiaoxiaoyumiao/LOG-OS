# Assets and Scenes

## Prefabs

把一个游戏场景中的对象从 hierarchy 列表中拖回 assets 栏即可获得一个Prefab。为了动态生成游戏对象，可以在 `Monobehavior` 的子类中定义一个类型为 `GameObject` 的 property，并在编辑器中将其赋值为 assets 中的 prefab（这个 property 的取值只能是 prefab 或 gameobject ），然后在 `Update` 函数中使用 `Instantiate(gameobject)` 将其实例化：

```csharp
//pseudo code
public class test : MonoBehavior {
    public GameObject gameobject;
    void Update() {
        destroy();//remember to destroy objects that you generated
        if (spawn_condition) {
            GameObject instance = Instantiate(gameobject) as GameObject;
            //do something to instance
        }
    }    
    void destroy() {
        foreach (GameObject ele in list_to_destroy) {
            Destroy(ele);
        }
        list_to_destroy.clear();
    }
}
```

Instantiate prefab while keeping the prefab link (used in an editor script)
  - Use `PrefabUtility.InstantiatePrefab` .
  - ref: https://docs.unity3d.com/ScriptReference/PrefabUtility.InstantiatePrefab.html
  - ref: https://answers.unity.com/questions/21731/editor-script-instantiating-prefab-and-maintaining.html

### Nested prefabs
  - Unity supports nested prefabs.
  - A blue box icon represents a prefab. A blue box with a plus sign represents an override on the parent prefab.
  - ref: https://docs.unity3d.com/2020.3/Documentation/Manual/NestedPrefabs.html

====start of old content====

注意对Prefab的嵌套可能出现子Prefab的关联丢失的问题：

[https://blog.csdn.net/zhenghongzhi6/article/details/84068691](https://blog.csdn.net/zhenghongzhi6/article/details/84068691)

似乎能解决这个问题的轮子：

[http://www.xuanyusong.com/archives/3042](http://www.xuanyusong.com/archives/3042)

====end of old content====

### Change prefab instances via script

When prefab instances are modified from script (especially via editor script when it's not play mode), Unity cannot track the changes as an override, and thus will lose these changes when the scene is reloaded.

To tell Unity that this is an override, call `PrefabUtility.RecordPrefabInstancePropertyModifications` after property change. Its parameter is the component whose properties are modified.

ref: https://docs.unity3d.com/ScriptReference/PrefabUtility.RecordPrefabInstancePropertyModifications.html


## 资源加载

[https://www.cnblogs.com/zhepama/p/4362312.html](https://www.cnblogs.com/zhepama/p/4362312.html)

加载的资源必须在Assets/Resources路径下，查询（Load）时使用项目中该目录下的相对路径。例如Resources/Time.png会被项目加载成Resources目录下的一个资源Time，于是load时传一个”Time“就能索引到这个资源。

```
foreach (string ele in names)
{
    Object pref = Resources.Load(string.Format(directory, ele), typeof(Sprite));
    Sprite tmp = GameObject.Instantiate(pref) as Sprite;
    sprites.Add(ele, tmp);
}
```

正规大型游戏更倾向采用在Runtime加载AssetBundle的方式，目前还没有试验过，待补完。

## 活跃场景及名字

```
 Scene scene = SceneManager.GetActiveScene ();
        GUILayout.Label ("当前场景: " + scene.name);
```

## 场景加载和进度条

[https://blog.csdn.net/huang9012/article/details/38659011](https://blog.csdn.net/huang9012/article/details/38659011)

[https://blog.csdn.net/weixin_42552233/article/details/81017332](https://blog.csdn.net/weixin_42552233/article/details/81017332)

[https://www.cnblogs.com/hutuzhu/p/9804348.html](https://www.cnblogs.com/hutuzhu/p/9804348.html)

* 需要引用`UnityEngine.SceneManagement`
* 同步加载用`SceneManager.LoadScene(sceneName)`
* 异步加载用`SceneManager.LoadSceneAsync(sceneName)`，和协程结合使用可以实现进度条
* 场景可以增量地加载到另一个场景
* 进度条加载页面实现：
  * 这里涉及三个场景：原场景A，加载页面B，目标场景C
  * 大体思路：场景A指定好目标场景（例如通过一个全局变量），加载场景B；场景B异步加载目标场景C，同时根据加载进度更新进度条UI；加载完成后进入场景C。有一些麻烦的细节：
  * 异步加载会返回一个`AsyncOperation`对象operation，这个对象提供所有加载相关信息，如`operation.progress`获取0\~1浮点数表示加载进度。为了保证进度条UI显示友好，需要在加载一开始关掉`operation.allowSceneActivation`，等进度条UI更新到100%再打开。由于关掉这个选项的缘故，场景的加载进度只会到0.9f，这一点在更新进度条UI进度时要注意。
  * 最简单的进度条UI使用localScale实现一个矩形的长度变化即可。

## 数值文件的加载

一般文件的加载可以使用`string filePath = Application.streamingAssetsPath + "/CSVDemo.csv";`这个`streamingAssetsPath`是一个Unity会根据具体运行平台确定的路径，相应地文件要放在Unity的 Assets/StreamingAssets 目录中。

CSV 加载的轮子列表：

[https://www.cnblogs.com/lyh916/p/8588218.html](https://www.cnblogs.com/lyh916/p/8588218.html)
亲测基本可用

[https://www.cnblogs.com/wuzhang/p/wuzhang20150511.html](https://www.cnblogs.com/wuzhang/p/wuzhang20150511.html)

[https://blog.csdn.net/musicvs/article/details/73135681](https://blog.csdn.net/musicvs/article/details/73135681)

## 数据存储方式

[https://blog.csdn.net/billcyj/article/details/79888614](https://blog.csdn.net/billcyj/article/details/79888614)

## 运行时数据可持久化

推荐使用单例模式实现（不继承 MonoBehavior）。

[https://blog.csdn.net/ycl295644/article/details/42458477?utm_source=blogxgwz8](https://blog.csdn.net/ycl295644/article/details/42458477?utm_source=blogxgwz8)

## 存档实现

[https://www.cnblogs.com/yoyocool/p/8527612.html](https://www.cnblogs.com/yoyocool/p/8527612.html)

## 资源的导出复用

使用 export package 功能。

[https://blog.theknightsofunity.com/use-unitypackage-files-share-part-project](https://blog.theknightsofunity.com/use-unitypackage-files-share-part-project)
