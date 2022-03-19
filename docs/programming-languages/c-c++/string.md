# String

## Dependency

### Human

* C basic \[EASY\]
* C standard \[EASY\]

## Character Array / 字符数组

字符数组可以用来表示一个字符串。被表示的字符串的各个字符顺次存入字符数组从0索引开始的位置中；最后一个字符紧邻的下一个索引处，用 `\0` （ASCII 值为 `0x00`）标明字符串的终止。在标准中这称为一个 null-terminated string。

### Declaration

用数组声明方法正常地声明一个字符数组即可。可以通过一个常字符串来初始化。

```c
char test1[20]; // define a char array without initialization
char test2[20] = "1234"; // declare a char array with "1234" as content
char test3[] = "abc"; // size of array can be omitted
```

使用 `memset` 可以方便地把（任何类型的）数组清零。

```c
/* header */
#include <string.h>

/* declaration */
void *memset( void *dest, int ch, size_t count );
// (since C11)
errno_t memset_s( void *dest, rsize_t destsz, int ch, rsize_t count );

/* usage */
char test1[20];
memset(test1, 0, sizeof(test1)); // maybe it's safer to clean up before use
```

使用 `strlen` 可以获取字符串的长度。

```c
/* header */
#include <string.h>

/* declaration */
size_t strlen( const char *str );
// (since C11)
size_t strnlen_s( const char *str, size_t strsz );

/* usage */
char dest[20] = "1234";
printf("%d",strlen(dest)); // output: 4
```

除了使用 `printf` 格式化输出，使用 `puts` 也可以打印字符串。`puts` 将一个 null-terminated string 的所有字符（不包含终止符）打印到 `stdout` ，并附加一个`\n` 。

### Assignment & Copy

`strcpy(dest, src)` 把 `src` 指向的 null-terminated string（连同终止符本身）拷贝到 `dest` 指向的位置。以下情况会导致 undefined 的行为：

* `dest` 数组不够大
* `dest` 和`src` 指向的内存区域重叠
* `dest` 不指向一个字符数组
* `src` 不指向一个 null-terminated string

```c
/* header */
#include <string.h>

/* declaration */
// (until C99)
char *strcpy( char *dest, const char *src );
// (since C99)
char *strcpy( char *restrict dest, const char *restrict src ); 
// (since C11)
errno_t strcpy_s(char *restrict dest, rsize_t destsz, const char *restrict src);

/* usage */
char dest[20];
strcpy(dest, "1234"); // dest points to "1234"
char targ[20];
strcpy(targ, dest);   // targ points to "1234"
```

注意：因为采用字符串视角时并不考虑终止符之后的内容，所以“字符数组指向的字符串”和“字符数组的内容”并不总是一致。在移动、复制、打印、修改字符数组时都应该记住这一点。例如：

```c
char dest[20] = "1234";
strcpy(dest, "21");
for (int i=0;i<20;++i) putchar(dest[i]); // output: 21 4
```

### String Format

使用 `sprintf` 可以用来自由地构造复杂的字符串。它的用法和 `printf` 差不多，区别在于它不把内容打印到 `stdout` 而是某个字符数组中。

格式化规则参考 `printf` 使用方法。

```c
/* header */
#include <stdio.h>

/* declaration */
// (until C99)
int sprintf( char *buffer, const char *format, ... );
// (since C99)
int sprintf( char *restrict buffer, const char *restrict format, ... );
// (since C11)
int sprintf_s(char *restrict buffer, rsize_t bufsz,
              const char *restrict format, ...);
// (since C11)
int snprintf_s(char *restrict buffer, rsize_t bufsz,
               const char *restrict format, ...);

/* usage */
char dest[20];
memset(dest, 0, sizeof(dest));
sprintf(dest,"I have %d apple(s)", 2); // dest points to "I have 2 apple(s)"
puts(dest); // output: I have 2 apple(s)
```

### String-Number Conversion

对于数字还有更快捷的字符串化的方式。以下字符串-数字转换函数会舍弃字符串开头的空白字符，并在能转换成数字的前提下尽可能地读取字符（负数也可以处理）。此后的字符会被舍弃。失败情形下返回 0。转换所得数字越界情形下的行为 undefined。

```c
/* header */
#include <stdlib.h>

/* declaration */
int       atoi( const char *str );
long      atol( const char *str );
// (since C99)
long long atoll( const char *str );

/* usage */
char str[] = " \n -1234junk";
int val = atoi(str); // val = -1234
char fail[] = "abc";
val = atoi(fail); // val = 0
```

### String Matching

使用`strstr(str, substr)` 可以在一个给定串`str`中寻找某个子串`substr`。如果找到，返回指向`str` 中首次出现的`substr` 的第一个字符的指针，简单来说就是返回字串首次出现的位置。否则，返回一个空指针。特别地，如果`substr` 是空串，将返回`str` （也就是指向`str`第一个字符的指针）。

据称这个查找函数的时间复杂度是最坏 O\(N^2\) 的，但在非极端情况下效率不比手写 KMP 算法差。

```c
/* header */
#include <string.h>

/* declaration */
char *strstr( const char* str, const char* substr );
```

