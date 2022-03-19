# Stream

```cpp
#include <sstream>
#include <string>
#include <fstream>

std::ifstream infile("thefile.txt");
std::string line;
while (std::getline(infile, line))
{
    std::istringstream iss(line);
    int a, b;
    if (!(iss >> a >> b)) { break; } // error

    // process pair (a,b)
}
```

## Reference

\[1\] [https://stackoverflow.com/questions/7868936/read-file-line-by-line-using-ifstream-in-c](https://stackoverflow.com/questions/7868936/read-file-line-by-line-using-ifstream-in-c)

\[2\] [https://www.cplusplus.com/doc/tutorial/files/](https://www.cplusplus.com/doc/tutorial/files/)

