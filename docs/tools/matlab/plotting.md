# Plotting

## 作图相关

hold on将使用叠加作图，否则新的图会冲掉旧的图。使用hold off关掉。

```text
figure(1); % 在图1作画
subplot(1,2,1); % 当前图中共有1行2列，在第1格中作图
subplot(1,2,2); % 当前图中共有1行2列，在第2格中作图
% 添加坐标轴名称
xlabel("x");
ylabel("y");
% 利用table函数可以把列向量画成一个表格的栏

% 图像绘制时的文字格式化输出
text(100, 70, [{['f = ', num2str(f_max)]}; {['A = ', num2str(A_max)]}; {['Ph = ', num2str(ph)]}])
title(sprintf('IMF%d的频谱', k))
```

