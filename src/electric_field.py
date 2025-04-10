"""
电偶极子电势与电场计算与可视化模板

本模板用于计算和可视化电偶极子的电势分布和电场线。
学生需要完成标有TODO的三个函数实现。
"""

import numpy as np
import matplotlib.pyplot as plt

# 物理常数
k = 8.99e9  # 库仑常数 (N·m²/C²)
q_pos = 1e-9  # 正点电荷量 (C)
q_neg = -1e-9  # 负点电荷量 (C)

# 电荷位置 [x, y] 坐标 (m)
pos_charge_pos = np.array([0.05, 0])  # 正电荷位置
neg_charge_pos = np.array([-0.05, 0])  # 负电荷位置

def calculate_potential(X, Y):
    """
    计算二维空间电势分布
    
    参数:
        X, Y: 二维网格坐标矩阵 (numpy.ndarray)
        
    返回:
        V: 电势值矩阵 (numpy.ndarray)
    """
    # TODO 1: 实现电势计算
    # 提示: 计算每个点到正负电荷的距离，应用电势公式
    r_pos = np.sqrt((X - pos_charge_pos[0])**2 + (Y - pos_charge_pos[1])**2)
    r_neg = np.sqrt((X - neg_charge_pos[0])**2 + (Y - neg_charge_pos[1])**2)
    
    r_pos = np.where(r_pos == 0, 1e-10, r_pos)
    r_neg = np.where(r_neg == 0, 1e-10, r_neg)
    
    V = k * (q_pos / r_pos + q_neg / r_neg)
    return V

def calculate_electric_field(V, spacing):
    """
    通过电势梯度计算电场强度
    
    参数:
        V: 电势值矩阵 (numpy.ndarray)
        spacing: 网格间距 (float)
        
    返回:
        Ex, Ey: 电场在x和y方向的分量 (numpy.ndarray, numpy.ndarray)
    """
    # TODO 2: 实现电场计算
    # 提示: 使用np.gradient计算电势梯度，注意负号和参数顺序
    dV_dx, dV_dy = np.gradient(V, spacing)
    Ex = -dV_dx
    Ey = -dV_dy
    return Ex, Ey

def main():
    """
    主函数: 计算并可视化电势和电场
    """
    # 创建计算网格
    x = np.linspace(-0.2, 0.2, 100)
    y = np.linspace(-0.2, 0.2, 100)
    X, Y = np.meshgrid(x, y)

    # TODO 3: 调用计算函数并绘制结果
    # 提示: 
    # 1. 先调用calculate_potential计算电势
    V = calculate_potential(X, Y)
    # 2. 用calculate_electric_field计算电场
    spacing = x[1] - x[0]
    Ex, Ey = calculate_electric_field(V, spacing)
    
    # 3. 使用plt.contourf绘制电势图
    
    plt.figure(figsize=(8, 6))
    contour = plt.contourf(X, Y, V, levels=50, cmap='viridis')
    plt.colorbar(contour, label='电势 (V)')
    # 4. 使用plt.streamplot绘制电场线
    plt.streamplot(X, Y, Ex, Ey, color='white', linewidth=1, density=1)
    # 5. 添加必要的标签、图例和标题
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('电偶极子电势分布与电场线')
    plt.savefig('electric_field.png')  # 保存为 PNG 图片
    plt.show()
    
    
    # ... 绘图代码 ...
    plt.show()

if __name__ == "__main__":
    main()
