# Topology

## Fat Tree



每个 switch 有 k 个端口。核心层 switch 为 `(k/2)**2`  个，Pod 有 k 个，每个 Pod 包含 (k/2) 个汇聚层 switch 和 (k/2) 个边缘层 switch，Pod 内每个汇聚层 switch 与每个边缘层 switch 连接（各自消耗 k/2 个端口）。每个汇聚层 switch 剩余 k/2 个端口与 k/2 个核心层 switch 相连，于是每个 Pod 都有 `(k/2)**2` 个端口与核心层 switch 相连，各个端口恰连接各不相同的核心层 switch。每个边缘层的剩余端口都用于连接 host，共能连接 k\*(k/2)\*(k/2) 个 host。

```
# of port per switch = k
# of pod = k
# of switch = k**2 + (k/2)**2 = k**2 * 5/4
# of server = k*(k/2)*(k/2) = k**3 /4
```

REF: [https://www.cnblogs.com/zhuting/p/8880475.html](https://www.cnblogs.com/zhuting/p/8880475.html)
