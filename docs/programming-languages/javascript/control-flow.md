# Control Flow

## If

```javascript
if (cond1) {
    // ...
} else if (cond2) {
    // ...
} else {
    // ...
}
```

## Switch

```javascript
switch (x) {
    case 0: // switch-case uses a === match
        // ...
        break;
    case 1:
    case 2: // in JS, the code block can be shared between cases like C
        // ...
        break;
    // ...
    default:
        // ...
}
```

## For

```javascript
for (i = 0; i < cars.length; i++) { 
    text += cars[i] + "<br>";
}
```

## For-in

For-in loops over properties of an object.

```javascript
// loop over elements of an array
var numbers = [45, 4, 9, 16, 25];

var txt = "";
var x;
for (x in numbers) {
  txt += numbers[x] + "<br>";
}
// or:
for (let i in numbers) {
  txt += numbers[i] + "<br>";
}

// loop over properties of an object
var person = {fname:"Bill", lname:"Gates", age:62}; 

var text = "";
var x;
for (x in person) {
    text += person[x]+" "; 
} // text = "Bill Gates 62"
```

* 事实上 for - in 的迭代次序在应用于数组时并不一定依赖数组本身的索引顺序，所以如果要遍历一个数组，建议采用传统 for 或者 `Array.prototype.forEach` 或者下文的 for - of 。
  * ref: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)

## For-of

For-of loops over values of an iterable object.

```javascript
let cars = ["BMW", "Volvo", "Mini"];
let text = "";

for (let x of cars) {
  text += x + "<br>";
}
```

## Reference

\[1\] [https://www.w3schools.com/js/js\_loop\_forin.asp](https://www.w3schools.com/js/js_loop_forin.asp)

