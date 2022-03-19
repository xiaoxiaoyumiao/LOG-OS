# Linear Algebra

## 矩阵运算

```text
#行向量 a = [1 2 3]; b = [4,5,6]
#列向量 d = [1;2;3]
#矩阵 m = [1 2 3; 4 5 6]
res = a + b # 向量加法

%向量矩阵操作：  b(3:5)
b(2) #向量索引，尾
length(b) #获取向量长度
size(A) #获取矩阵大小，返回一个元组
sort(x,DIM) #对矩阵x沿着
a = b' #共轭转置b
a = b.' #转置b

a*b #矩阵乘法
a.*b #矩阵点积
a\b # INV(A) B
a/b # A INV(B)

向量/矩阵生成：
randsample(MAX, num) 从整数1~MAX随机抽num个数做成列向量
rand(r,c) 生成r行c列的随机矩阵
​
diag(x) 若x是行/列向量，返回由该向量构成的对角阵；
否则，（无论矩阵是否为方阵）返回矩阵的对角元素构成的向量
diag(diag(x)) 提取矩阵对角阵
triu(x,1) 返回对角线为0的x的上三角阵
tril(x,-1) 返回对角线为0的x的下三角阵
norm(x) 求二范数
cond(x) 求条件数（判矩阵病态程度）
eig(x) 求所有特征值
rank(A) 求矩阵的秩
[L,U,P] = lu(A)
返回三个矩阵，下三角矩阵L、上三角矩阵U和一个置换矩阵P，满足P*A=L*U。
​
B = reshape(A,m,n) 将矩阵A变形为m*n矩阵B
```

