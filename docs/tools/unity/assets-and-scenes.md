# Assets and Scenes

## Prefabs

把一个游戏场景中的对象从hierarchy列表中拖回assets栏即可获得一个Prefab。为了动态spawn出游戏对象，可以在Monobehavior的子类中定义一个GameObject的field，并在编辑器中将其赋值为assets中的prefab（这个field的取值只能是prefab或gameobject），然后在update函数中使用Instantiate\(gameobject\)将其实例化：

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

**注意对Prefab的嵌套可能出现子Prefab的关联丢失的问题：**

{% embed url="https://blog.csdn.net/zhenghongzhi6/article/details/84068691" caption="" %}

似乎能解决这个问题的轮子：

{% embed url="http://www.xuanyusong.com/archives/3042" caption="" %}

## **资源加载**

{% embed url="https://www.cnblogs.com/zhepama/p/4362312.html" caption="" %}

加载的资源必须在Assets/Resources路径下，查询（Load）时使用项目中该目录下的相对路径。例如Resources/Time.png会被项目加载成Resources目录下的一个资源Time，于是load时传一个”Time“就能索引到这个资源。

```text
foreach (string ele in names)
{
    Object pref = Resources.Load(string.Format(directory, ele), typeof(Sprite));
    Sprite tmp = GameObject.Instantiate(pref) as Sprite;
    sprites.Add(ele, tmp);
}
```

正规大型游戏更倾向采用在Runtime加载AssetBundle的方式，目前还没有试验过，待补完。

## **活跃场景及名字**

```text
 Scene scene = SceneManager.GetActiveScene ();
        GUILayout.Label ("当前场景: " + scene.name);
```

## **场景加载和进度条**

{% embed url="https://blog.csdn.net/huang9012/article/details/38659011" caption="" %}

{% embed url="https://blog.csdn.net/weixin\_42552233/article/details/81017332" caption="" %}

{% embed url="https://www.cnblogs.com/hutuzhu/p/9804348.html" caption="" %}

* 需要引用`UnityEngine.SceneManagement`
* 同步加载用`SceneManager.LoadScene(sceneName)`
* 异步加载用`SceneManager.LoadSceneAsync(sceneName)`，和协程结合使用可以实现进度条
* 场景可以附加式加载，好像很牛逼，有空研究一下
* 进度条加载页面实现：
  * 这里涉及三个场景：原场景A，加载页面B，目标场景C
  * 大体思路：场景A指定好目标场景（例如通过一个全局变量），加载场景B；场景B异步加载目标场景C，同时根据加载进度更新进度条UI；加载完成后进入场景C。有一些麻烦的细节：
  * 异步加载会返回一个`AsyncOperation`对象operation，这个对象提供所有加载相关信息，如`operation.progress`获取0~1浮点数表示加载进度。为了保证进度条UI显示友好，需要在加载一开始关掉`operation.allowSceneActivation`，等进度条UI更新到100%再打开。由于关掉这个选项的缘故，场景的加载进度只会到0.9f，这一点在更新进度条UI进度时要注意。
  * 最简单的进度条UI使用localScale实现一个矩形的长度变化即可。

## **数值文件的加载**

一般文件的加载可以使用`string filePath = Application.streamingAssetsPath + "/CSVDemo.csv";`这个`streamingAssetsPath`是一个Unity会根据具体运行平台确定的路径，相应地文件要放在Unity的 Assets/StreamingAssets 目录中。

CSV 加载的轮子列表：

{% embed url="https://www.cnblogs.com/lyh916/p/8588218.html" caption="亲测基本可用" %}

{% embed url="https://www.cnblogs.com/wuzhang/p/wuzhang20150511.html" caption="" %}

{% embed url="https://blog.csdn.net/musicvs/article/details/73135681" caption="" %}

## **数据存储方式**

{% embed url="https://blog.csdn.net/billcyj/article/details/79888614" caption="" %}

## **运行时数据可持久化**

推荐使用单例模式实现（不继承 MonoBehavior）。

{% embed url="https://blog.csdn.net/ycl295644/article/details/42458477?utm\_source=blogxgwz8" caption="" %}

## **存档实现**

{% embed url="https://www.cnblogs.com/yoyocool/p/8527612.html" caption="" %}

