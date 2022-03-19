# Classes & Data Structures

## Classes & Objects

```text
Objects.equals(a,b) //检验A和B的相等性
//equals方法要求具有自反性、对称性、传递性、一致性（反复调用结果应当一致），以及非空!=null
getclass().getName()//可以获得类名字符串
A instanceof B运算可以判定一个实例是否是给定类的实例
```

### 泛型

```text
//用以下方式定义一个泛型类：
public class ClassName<T,U>{
    private T field;
    ...
}
//用以下方式定义一个泛型方法：
class ClassName {
    public <T> T getString(T a){
        ...
    }
}
//用以下方式对T的方法进行限定（良心啊）：
class ClassName {
    public <T extends SomeInterfaceOrClass & SomeOtherInterface> T getString(T a){//限定使用&分隔，而类型变量用逗号分隔；限定中至多有一个是类
        ...
    }
}
//泛型类/接口可以普通地继承：
public class Something<E> implements Parent<E>
```

## 集合接口Collection

集合框架collection：接口和实现分离 Collection是一个接口，Collections是一个类

```text
import java.util.Collections;
//Collection 接口的基本方法：
boolean add(E ele); // add element
Iterator<E> iterator();//return iterator
int size(); //return size
boolean isEmpty()
boolean contains(Object obj)
boolean addAll(Collection c)
boolean remove(Ojbect obj)
void clear()
​
​
//Iterator<E>'s basic method:
boolean hasNext();
E hasNext();
//so you can iterate over the collection like this:
while (iter.hasNext()){
    ClassName ele = iter.next();
    ...
}
//to make it easier, try for each:
for (ClassName ele : c) {
    //do something
}//this works for all classes that impl Collection
//can reduce words with lambda expression:
iterator.forEachRemaining(ele -> System.out.println(ele));
​
​
```

#### 列表接口List

```text
//List is sequential and can be accessed by index
​
```

#### 集合接口Set

```text
//Set can store no duplicate elements judged by equals()
​
```

#### 映射接口Map

使用put添加，get访问，用Map.entry&lt;typeA,typeB&gt;作为变量可以for each遍历

#### 实用数据结构

```text
/** 动态数组(向量)ArrayList */
ArrayList<ClassName> arr = new ArrayList<>(int);//可以提供一个可选参数作为初始容量，但注意此时数组列表内并没有元素（甚至空元素）
arr.add(ClassName obj); //添加元素
arr.size()；//获取数组大小
arr.get(index);//获取index位置元素
arr.set(index,content);//对index位置的元素赋值content。只能操作已有元素
arr.toArray(a);//把数组列表内容移到静态的数组a中
//可以使用for each遍历
​
/** 可寻址的映射表HashMap */
HashMap<ClassName> hm;
​
/** 链表LINKEDLIST LinkedList */
LinkedList<E> ll;
​
/** 双端队列 ArrayDeque */
ArrayDeque<E> ad;
​
/** 散列映射 HashMap */
import java.util.HashMap;
Map<S,T> someMap = new HashMap<>();
someMap.put(key,value);
someMap.get(key) -> value(or null);
someMap.getOrDefault(key,0) -> value(or 0);
    //application: word counting
    someMap.put(word,someMap.getOrDefault(word,0)+1);
    //or merge() instead(not that general)
    someMap.merge(word,1,Integer::sum);
someMap.remove(key);
//return view:
keySet()
values()
entrySet()
for (Map.Entry<S,T> entry:someMap.entrySet()){
   ...
}
​
```

#### 子范围/视图

如subList\(a,b\)取一个List的部分区间，subMap\(K1,K2\)取SortedMap范围内的的子集合 不可修改视图：试图修改集合时抛出异常 Collections.unmodifiable\[somecollectiontype\]

#### SortedSet&lt;E&gt;

建立有序集合

