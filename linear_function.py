import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, widgets

def plot_linear_function(k, b):
    """
    绘制一次函数图像
    
    参数:
    k (float): 函数斜率
    b (float): 函数截距
    """
    # 生成x轴数据
    x = np.linspace(-10, 10, 100)
    
    # 计算y轴数据
    y = k * x + b
    
    # 绘制函数图像
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, color='blue', label=f'y = {k:.2f}x + {b:.2f}')
    
    # 设置坐标轴标签和标题
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('一次函数图像')
    ax.legend()
    
    # 显示图像
    plt.show()

# 创建交互式小组件
k_slider = widgets.FloatText(value=1, description='k:')
b_slider = widgets.FloatText(value=0, description='b:')

interactive_plot = interactive(plot_linear_function, 
                              k=k_slider,
                              b=b_slider)

# 显示小组件
interactive_plot
