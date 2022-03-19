# Numerical Analysis

```text
sum(x) % 矩形积分
cumsum(x) % 前缀和数组
trapz(x) % 均匀步长梯形公式
trapz(x,y) % 梯形公式，步长可能不均匀
quad('fun',a,b,tol=1e-6) % 辛普森公式，a,b为区间
quadl('fun',a,b,tol) % 高斯公式
dblquad('fun',xlo,xhi,ylo,yhi) % quad计算二重积分
```

