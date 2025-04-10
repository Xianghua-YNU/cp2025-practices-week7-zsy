import pandas as pd
import matplotlib.pyplot as plt

def creat_frame():
    """
    创建一个包含学生信息的DataFrame并保存为CSV文件。
    
    该函数创建一个包含学生姓名、年龄、成绩和所在城市的数据框架，
    并将其保存为UTF-8编码的CSV文件。
    
    Returns:
        None
    """
    # 创建一个字典来模拟数据
    data = {
    '姓名': ['张三', '李四', '王五', '赵六', '陈七'],
    '年龄': [25, 30, None, 22, 28],
    '成绩': [85.5, 90.0, 78.5, 88.0, 92.0],
    '城市': ['北京', '上海', '广州', '深圳', '上海']
    }

    # 将字典转换为 DataFrame
    df = pd.DataFrame(data)

    # 将 DataFrame 保存为 CSV 文件
    df.to_csv('data/data.csv', index=False, encoding='utf-8')

def load_data():
    """任务1: 读取数据文件"""
    # 学生需要在此处实现代码
    df = pd.read_csv('data/data.csv')
    return df

def show_basic_info(data):
    """任务2: 显示数据基本信息"""
    # 学生需要在此处实现代码
    print("数据的基本信息：")
    print(data.info())
    print("\n数据的描述性统计：")
    print(data.describe())

def handle_missing_values(data):
    """任务3: 处理缺失值"""
    # 学生需要在此处实现代码
    data['年龄'].fillna(data['年龄'].mean(), inplace=True)
    return data

def analyze_statistics(data):
    """任务4: 统计分析数值列"""
    # 学生需要在此处实现代码
    numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
    statistics = data[numerical_columns].describe()
    print("\n数值列的统计分析：")
    print(statistics)
    print("\n成绩 列的均值: {:.2f}".format(statistics.loc['mean', '成绩']))
    print("年龄 列的均值: {:.2f}".format(statistics.loc['mean', '年龄']))
    
    return statistics

def visualize_data(data, column_name='成绩'):
    """任务6: 数据可视化"""
    # 学生需要在此处实现代码
    plt.figure(figsize=(10, 6))
    plt.bar(data['姓名'], data[column_name])
    plt.xlabel('name')
    plt.ylabel(column_name)
    plt.title(f'{column_name}分布')
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(f'visualizations/{column_name}_distribution.png')
    plt.show()

def save_processed_data(data):
    """任务7: 保存处理后的数据"""
    # 学生需要在此处实现代码
    data.to_csv('processed_data.csv', index=False, encoding='utf-8')


def main():
    """主函数，执行所有数据处理流程"""
    # 生成data.csv文件
    creat_frame() 
    
    # 学生需要在此处组织代码流程
    df = load_data()
    show_basic_info(df)
    cleaned_df = handle_missing_values(df)
    analyze_statistics(cleaned_df)
    visualize_data(cleaned_df, '成绩')
    save_processed_data(cleaned_df)

if __name__ == "__main__":
    main()
