import numpy as np
import scipy.ndimage as sim
import matplotlib.pyplot as plt

def create_small_filter():
    """
    创建3×3平均滤波器
    
    返回:
        numpy.ndarray: 3×3的滤波器矩阵，每个元素值为1/9
    """
    # 学生需要在此实现代码
    small_filter = np.ones((3, 3)) / 9
    return small_filter

def create_large_filter():
    """
    创建15×15平均滤波器
    
    返回:
        numpy.ndarray: 15×15的滤波器矩阵，每个元素值为1/225
    """
    # 学生需要在此实现代码
    large_filter = np.ones((15, 15)) / 225
    return large_filter

def process_image(input_file):
    """
    处理图像并显示原始图像和滤波后的结果
    
    参数:
        input_file (str): 输入图像文件路径
        
    功能:
        1. 读取输入图像
        2. 创建3×3和15×15平均滤波器
        3. 对图像应用两种滤波器
        4. 显示原始图像和两种滤波结果对比
        
    学生任务:
        完成以下步骤的实现代码
    """
    # 1. 读取图像 - 使用plt.imread()函数
    img = img = plt.imread(input_file)
    
    # 2. 创建滤波器 - 调用已实现的函数
    small_filter = create_small_filter()
    large_filter = create_large_filter()
    
    # 3. 应用卷积 - 使用sim.convolve()函数
    small_result = sim.convolve(img, small_filter)
    large_result = sim.convolve(img, large_filter)
    
    # 4. 显示结果 - 使用matplotlib绘制对比图
    # 创建画布
    plt.figure(figsize=(15, 5))
    
    # 显示原始图像
    plt.subplot(1, 3, 1)

    # 学生需要添加显示原始图像的代码
    plt.title('Original Image')
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    # 显示3×3滤波结果
    plt.subplot(1, 3, 2)
    
    # 学生需要添加显示小滤波器结果的代码
    plt.title('3×3 Filter Result')
    plt.imshow(small_result, cmap='gray')
    plt.axis('off')
    # 显示15×15滤波结果
    plt.subplot(1, 3, 3)
    # 学生需要添加显示大滤波器结果的代码
    plt.title('15×15 Filter Result')
    plt.imshow(large_result, cmap='gray')
    plt.axis('off')
    # 调整布局并显示
    plt.tight_layout()
    plt.show()
    
    plt.savefig('processed_image.png', dpi=300)
if __name__ == "__main__":
    # 主程序入口 - 学生需要确保data/bwCat.tif文件存在
    process_image('data/bwCat.tif')
