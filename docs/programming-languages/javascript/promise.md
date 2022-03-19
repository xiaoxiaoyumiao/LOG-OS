# Promise

## Introduction

* Promise 代表了一个尚未发生的事件或尚未得到的值，通过使用 Promise 可以方便地设定对未来事件的结果或者得到的值应该如何处理。异步函数可以像普通的同步函数返回值那样返回一个 Promise，承诺未来将返回的值。
* 使用 then、catch 方法和 Promise 链的书写方式可以使嵌套的异步回调函数形成更易读的链状表达式。

## Promise

* Promise 总是处于三种状态中的某一种：
  * pending：初始状态，表明结果尚未得到
  * fulfilled / resolved：表明 Promise 正常地取得了结果
  * rejected：表明并没有如期取得结果，而是发生了某些错误
* Promise 的构造器接受一个函数对象。这个函数对象的参数包含 resolve 和 reject 两个回调函数，调用前者可以使 Promise 进入 fulfilled 状态，调用后者则使 Promise 进入 rejected 状态。Promise 会在被构造后立即执行这个函数。resolve 和 reject 回调函数都可以接受参数作为 Promise 的最终返回值。
  * 从某种角度来说 Promise 也可以看作是对一个异步函数的封装。
* Promise 对象的 then 方法接收 onFulfillment 和 onRejection 两个回调函数作为参数，分别处理 Promise fulfilled 和 Promise rejected 的情况。catch 方法则只接收 onRejection 一个参数。finally 方法则接收 onFinally 回调函数，它在无论 fulfilled 还是 rejected 的情况下都会被执行。
  * 所有回调函数都会接受 Promise 的最终返回值（也就是 resolve 或 reject 接受的参数）作为参数。
  * 这三个方法都会返回一个新的 Promise 对象。因此可以通过调用返回的 Promise 的 then 等方法，将 Promise 组织为链状的形式，也就是 Promise 链。
  * 如果传入的回调函数返回了新的 Promise 对象，那么这三个方法返回的 Promise 状态将会延续这个新的 Promise 对象的状态，返回值也会继承。
  * 虽然使用时 Promise 链基本上由一连串回调函数构成，但注意 then 等方法其实并不要求回调函数是异步的，或者必须返回一个新的 Promise。回调函数会按照在链中的定义顺序执行。
  * 即使通过 then 等方法添加回调函数时 Promise 已经进入 fulfilled 或 rejected 状态，回调函数仍然会被执行，因此不必担心异步函数执行和回调的竞争冒险问题。
  * 如果觉得 `promise.then(()=>{ return new Promise((resolve, reject)=>{ ... } ); })` 这种写法看起来很庞杂（特别是在实际执行函数体并不长或者 Promise 一定会进入某个确定状态的时候），可以考虑使用 Promise 的静态函数 reject 和 resolve，它们会直接返回一个解决到对应状态的 Promise 对象。
    * 当然对于 resolve 方法，如果它接受的返回值是一个带有 then 方法的对象（比如一个 Promise 对象），那么它返回的 Promise 对象会像 then 返回的 Promise 那样跟随这个对象的状态和结果。
* Promise 另外提供了 any、allSettled、race 等静态方法，从而可以对多个 Promise 结果进行逻辑运算。

```text
promise1
.then(value => { return value + ' and bar'; })
.then(value => { return value + ' and bar again'; })
.then(value => { return value + ' and again'; })
.then(value => { return value + ' and again'; })
.then(value => { console.log(value) })
.catch(err => { console.log(err) });
```

## Reference

\[1\] [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

\[2\] [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Promise/then](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then)

