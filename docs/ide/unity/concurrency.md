# Concurrency

## Coroutine

* 阻塞等待协程完成
  * 使用 `yield return StartCoroutine(SomeMethod())` 。
  * ref: [https://forum.unity.com/threads/wait-until-coroutine-finish-like-thread-join.479629/](https://forum.unity.com/threads/wait-until-coroutine-finish-like-thread-join.479629/)
* 关于 yield return null
  * 基于 C# 的线程调度，Unity 在遇到诸如 null 这样对 Unity 的 coroutine 系统无意义的值时，会简单地 re-schedule 该协程到下一个 frame 继续执行。作为参照，Unity 会解析 WaitForSeconds 这样的 yield return 对象并作相应调度（等待若干时间）。
  * ref: [https://answers.unity.com/questions/1582166/yield-return-null.html](https://answers.unity.com/questions/1582166/yield-return-null.html)

## Promise

A 3rd-party Promise implementation: [https://github.com/Real-Serious-Games/C-Sharp-Promise#chaining-async-operations](https://github.com/Real-Serious-Games/C-Sharp-Promise#chaining-async-operations)

