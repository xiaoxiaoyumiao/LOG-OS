# Statistics

## 统计运算函数

### 统计量

```text
[n,y] = hist(x,k) # 直方图/频数表，x原始数据向量，k等分区间数；n为频数行向量，y为分割的各区间中点构成的行向量
mean(x) # 求均值
median(x) # 求中位数
range(x) # 求极差
std(x) # 求标准差
var(x) # 求方差
skewness(x) # 偏度skewness
kurtosis(x) # 峰度kurtosis
```

### 分布与密度函数

```text
# 分布的前缀：
unif # 均匀分布
exp # 指数分布
norm # 正态分布，参数mean std（不是var）不传参时为N(0,1)
chi2 # 卡方分布
T # t分布
f # F分布，参数n1 n2
bino # 二项分布
poiss # 泊松分布
cov(x,y) # 协方差，x,y为同长度数组，输出[sx^2 sxy^2; sxy^2 sy^2]
corrcoef(x,y) # 相关系数，输出[1,rxy;rxy,1]

# 具体功能的后缀：
pdf # 概率密度函数，返回p(x)
cdf # 分布函数（PDF的积分）,返回F(x)
Inv # 逆概率分布/求分位数，返回F^-1(x)
stat # 均值与方差，返回[mean, var]
rnd # 随机数生成

# 使用例：
y = normpdf(1.5, 1,2) % P(X=1.5), X~N(1,2)
y = binopdf(5:8, 20, 0.2) % P(X=5), P(X=6), P(X=7), P(X=8), X~B(20,0.2)
[m,v] = fstat(3,5) % [E(X), D(x)], X~F(3,5)
unifrnd(a,b,m,n) % m行n列[a,b]区间上的随机数
rand(m,n) % m行n列[0,1]区间上的随机数
```

### 回归

```text
b = regress(y, X) % X由1和自变量构成，如X = [ ones(n,1), x]
[b,bint,r,rint,s]=regress(y,X);
rcoplot(r,rint) % 残差作图
```

