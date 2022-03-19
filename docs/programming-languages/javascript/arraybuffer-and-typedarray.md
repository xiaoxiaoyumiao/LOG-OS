# ArrayBuffer & TypedArray

## ArrayBuffer

`ArrayBuffer` 对象是一个存储二进制数据的 buffer，无法直接操作，需要借助 DataView 或 TypedArray 对象来读写其值。

```javascript
// create an ArrayBuffer of length 8
const buffer = new ArrayBuffer(8);
// use byteLength property to get the length 8
const len = buffer.byteLength;
```

## DataView

`DataView` 对象拥有一系列 set 和 get 方法，可以读写其拥有的 `ArrayBuffer` 特定位置的值，且可以控制读写时的大小端。如果希望灵活操作一块缓存数据，可以使用 `DataView`。

* 它本身并不具备类型信息，类型是在每一次读写时随所调用的方法动态确定的。
* 注意它不能使用中括号索引。

```javascript
var buffer = new ArrayBuffer(16);
var view = new DataView(buffer, 0);

// read buffer property to get the original buffer.
var alsoBuffer = view.buffer;  // ArrayBuffer(16) {}

// read byteLength property to get the length of this view
const len = view.byteLength; // 16

view.setInt16(1, 42);
view.getInt16(1); // 42
```

## TypedArray

`TypedArray` 是与普通列表不同，可针对二进制数据读写的一系列数组类型的基类。这一类数组可以使用中括号索引读写。如果希望批量地维护一列特定位宽和长度的数据，并且能方便地使用中括号语法，可以使用 `TypedArray`。

* 它的元素类型在构造时就确定了。
* 它可以使用中括号索引读写。

```javascript
let buffer = new ArrayBuffer(16);
// create a 
let int32View = new Int32Array(buffer);
for (let i = 0; i < int32View.length; i++) {
  int32View[i] = i * 2;
}
```

## Offset & Length

`DataView` 和 `TypedArray` 都可以在从 `ArrayBuffer` 构造时指定 offset 和 length，即从原 buffer 相对起始位置偏移多少（字节）开始，覆盖多少（字节）的长度。这样就可以只针对 buffer 的特定数据段操作。但注意这种情况下 view 对象返回的 `byteLength` 和其 buffer 属性的 `byteLength` 并不会一致，其 buffer 属性保持着先前的 `ArrayBuffer` 的属性。

## Methods

大多数 Array 的方法 Typed Array 都有。此处列举一些 Typed Array 独有的方法。

```javascript
// set values of the current array starting from offset
// to the values provided by array.
// 默认使用 array 的所有值，且会在越界时报错。
// 如果只想使用 array 的一部分值，可以考虑使用 slice 方法。
typedarray.set(array[, offset])

// create an ArrayBuffer with a size in bytes
const buffer = new ArrayBuffer(8);
const uint8 = new Uint8Array(buffer);
// Copy the values into the array starting at index 3
uint8.set([1, 2, 3], 3);
console.log(uint8);
// expected output: Uint8Array [0, 0, 0, 1, 2, 3, 0, 0]
```

## Reference

\[1\] [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/ArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)

\[2\] [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/DataView](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView)

\[3\] [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed\_arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)

\[4\] [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/TypedArray](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)

\[5\] [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/TypedArray/set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray/set)

