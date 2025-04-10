# SymPy 绘图实验报告

## 一、实验信息

- 小组名称：zhusiyu
- 成员：朱思宇
- 实验日期：2025.4.10

---

## 二、实验目的

- 熟悉SymPy的plot、plot_implicit、和plot3d_parametric_surface函数；
- 掌握曲线、隐函数和参数曲面的绘制方法。

---

## 三、实验内容与方法

分别说明三个问题的具体绘图方法和使用的函数接口。
---
A：1、基本函数绘图
    绘图方法： 使用 SymPy 的 plot 函数。定义符号变量 x。构造表达式 cos(tan(πx))。设置绘图区间为 [−1,1]。添加坐标轴标签（xlabel 和 ylabel）和标题。
    函数接口：plot(expr, (x, -1, 1), xlabel='x', ylabel='y', title='cos(tan(pi*x))', show=False)
   2、 隐函数绘图
   绘图方法： 使用 SymPy 的 plot_implicit 函数。定义符号变量 x 和 y。构造隐函数表达式。设置绘图区间为 x∈[−10,10] 和 y∈[−10,10]，避免除零错误。添加坐标轴标签和标题。设置 points=500 以获得平滑曲线。
    函数接口：plot_implicit(expr, (x, -10, 10), (y, -10, 10), xlabel='x', ylabel='y', title='e^y + cos(x)/x + y = 0', points=500, show=False)
    3、 参数曲面绘图    绘图方法： 使用 SymPy 的 plot3d_parametric_surface 函数。定义符号变量 s 和 t。构造参数方程 x=e^(−s) cost，y=e^(−s) sint，z=t。设置参数范围 s∈[0,8] 和 t∈[0,5π]。添加三维坐标轴标签和标题。
    函数接口：plot3d_parametric_surface(x, y, z, (s, 0, 8), (t, 0, 5*sp.pi), xlabel='x', ylabel='y', zlabel='z', title='3D Parametric Surface', show=False)
    
## 四、实验结果与分析

### 问题1: 函数曲线 $\cos(\tan(\pi x))$ 绘制结果

![image](https://github.com/user-attachments/assets/1442f78f-c426-49a6-9d23-c4b0468c4e97)


### 问题2: 隐函数曲线 $e^y + \frac{\cos x}{x} + y = 0$ 绘制结果

![image](https://github.com/user-attachments/assets/9cb7f527-dad4-4794-8b24-ca344fa2d75c)


### 问题3: 参数曲面绘制结果

![image](https://github.com/user-attachments/assets/4d65b3ff-0205-44dd-a8c3-5dce3da7fb80)


---

## 五、实验总结与讨论

- 通过本实验你掌握了哪些绘图技巧？
- A:1、基本函数绘图：熟悉了如何使用 sympy.plot 函数绘制一元函数的图像。掌握了设置绘图区间、坐标轴标签和标题的方法。
    2、隐函数绘图：学会了使用 sympy.plot_implicit 函数绘制隐函数图像。了解了如何避免除零错误并设置合适的绘图区间。
    3、参数曲面绘图：掌握了使用 sympy.plot3d_parametric_surface 函数绘制三维参数曲面的方法。学会了定义参数方程和设置参数范围。
- 实验中你遇到了哪些问题？如何解决？
- A:问题：在 problem2 中，绘图区间设置不当，导致图像不完整或出现错误。
    解决方法：调整了绘图区间，避免了除零错误，并确保图像完整。
- 你对SymPy的绘图功能有什么建议或意见？
- A:希望能够提供更明确的错误提示，帮助用户快速定位问题。建议默认绘图区间和采样点数量能够根据函数特性自动调整。

---

## 六、参考文献

- SymPy官方文档：https://docs.sympy.org/latest/modules/plotting.html
