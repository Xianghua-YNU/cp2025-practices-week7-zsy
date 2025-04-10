# 实验报告 - Pandas 数据操作练习

## 一、实验目的
阐述本次实验的主要目的，可参考任务目的部分。
通过实际操作，掌握 Pandas 的基本和高级功能，如数据读取、清洗、转换、分析和可视化
## 二、实验步骤
详细描述你完成每个任务的步骤和方法，可结合代码进行说明。

### 任务 1: 读取数据
说明你使用的读取数据的函数和过程。
def load_data():
    """任务1: 读取数据文件"""
    df = pd.read_csv('data/data.csv')
    return df
### 任务 2: 查看数据基本信息
描述如何查看数据的基本信息。
def show_basic_info(data):
    """任务2: 显示数据基本信息"""
    print("数据的基本信息：")
    print(data.info())
    print("\n数据的描述性统计：")
    print(data.describe())
### 任务 3: 处理缺失值
说明你找出缺失值列和填充缺失值的方法。
def handle_missing_values(data):
    """任务3: 处理缺失值"""
    data['年龄'].fillna(data['年龄'].mean(), inplace=True)
    return data
### 任务 4: 数据统计分析
说明你计算数值列均值、中位数和标准差的方法。

### 任务 5: 数据可视化
描述你选择的数值列和绘制直方图的过程。
def analyze_statistics(data):
    """任务4: 统计分析数值列"""
    numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
    statistics = data[numerical_columns].describe()
    print("\n数值列的统计分析：")
    print(statistics)
    print("\n成绩 列的均值: {:.2f}".format(statistics.loc['mean', '成绩']))
    print("年龄 列的均值: {:.2f}".format(statistics.loc['mean', '年龄']))
    return statistics
### 任务 6: 数据保存
说明你保存处理后数据的方法。
def visualize_data(data, column_name='成绩'):
    """任务6: 数据可视化"""
    plt.figure(figsize=(10, 6))
    plt.bar(data['姓名'], data[column_name])
    plt.xlabel('name')
    plt.ylabel(column_name)
    plt.title(f'{column_name}分布')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'visualizations/{column_name}_distribution.png')
    plt.show()

## 三、实验结果
展示每个任务的结果，可使用表格或图表进行呈现。

### 任务 1: 读取数据
展示读取的数据的基本信息（如列名、行数等）。
数据的基本信息：
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   姓名    5 non-null      object 
 1   年龄    4 non-null      float64
 2   成绩    5 non-null      float64
 3   城市    5 non-null      object 
dtypes: float64(2), object(2)
memory usage: 200.0+ bytes

### 任务 2: 查看数据基本信息
粘贴数据的基本信息输出。
数据的基本信息：
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   姓名    5 non-null      object 
 1   年龄    4 non-null      float64
 2   成绩    5 non-null      float64
 3   城市    5 non-null      object 
dtypes: float64(2), object(2)
memory usage: 200.0+ bytes
### 任务 3: 处理缺失值
说明处理后缺失值的情况。
数值列的统计分析：
               年龄        成绩
count  5.000000  5.000000
mean  26.200000 88.875000
std    3.288462  5.507528
min   22.000000 78.500000
25%   24.000000 85.500000
50%   26.200000 88.000000
75%   28.500000 90.000000
max   30.000000 92.000000
### 任务 4: 数据统计分析
列出数值列的均值、中位数和标准差。
Mean of the 'Score' column: 86.80
Mean of the 'Age' column: 26.25
### 任务 5: 数据可视化
插入绘制的直方图。
![image](https://github.com/user-attachments/assets/6f9d0551-5507-468b-8ec3-078f9b6705ee)

### 任务 6: 数据保存
说明保存的文件路径和文件名。
processed_data.csv
## 四、总结
总结本次实验的收获和体会，分析遇到的问题及解决方法，对 Pandas 数据操作的理解和认识。
A:收获和体会:掌握了如何使用 pd.read_csv 读取 CSV 文件，并将其转换为 Pandas DataFrame。学会了如何处理缺失值，包括删除包含缺失值的行或用均值填充缺失值。会了如何将数据处理流程模块化，通过定义函数来组织代码。
  问题及解决方法:1、在保存处理后的数据时，文件路径不正确，导致文件未被成功创建。解决方法：确保文件保存路径正确，并在必要时创建所需的目录。2、在测试中，由于处理后的数据行数不符合预期，导致断言失败。解决方法：调整数据处理逻辑，确保处理后的数据行数与预期一致，在此次作业中，用均值填充缺失值而不是删除包含缺失值的行。
   理解和认识：Pandas 支持多种数据操作，包括数据读取、清洗、转换、分析和可视化，能够满足不同的数据分析需求。此外，其提供了高效的数据结构和操作工具，能够快速处理大规模数据集。
