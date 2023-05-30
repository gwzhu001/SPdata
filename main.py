import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
data = pd.read_excel('data1.xlsx', sheet_name=None)

# 统计每天的步数和距离
walk_data = data['步行']
 daily_steps = walk_data.groupby('日期')['步数'].sum()
daily_distance = walk_data.groupby('日期')['距离'].sum()

# 统计每日消耗卡路里
calories_data = data['健身']
daily_calories = calories_data.groupby('日期')['卡路里'].sum()

# 统计每日心率
heart_rate_data = data['心率']
daily_heart_rate = heart_rate_data.groupby('日期')['心率'].mean()

# 统计每日温度和体温变化
temperature_data = data['基本信息']
daily_temperature = temperature_data.groupby('日期')['温度'].mean()
daily_body_temperature = temperature_data.groupby('日期')['体温'].mean()

# 统计运动情况和运动持续时长
activity_data = data['跑步'].append(data['骑行']).append(data['健身']).append(data['羽毛球'])
daily_activity_duration = activity_data.groupby('日期')['时长'].sum()

# 统计每次运动心率的最大值、最小值和平均值
activity_heart_rate = activity_data.groupby('日期')['心率']
max_heart_rate = activity_heart_rate.max()
min_heart_rate = activity_heart_rate.min()
average_heart_rate = activity_heart_rate.mean()

# 绘制图表
fig, axes = plt.subplots(4, 1, figsize=(10, 12))

# 步数和距离
axes[0].plot(daily_steps, marker='o')
axes[0].plot(daily_distance, marker='o')
axes[0].legend(['步数', '距离'])
axes[0].set_xlabel('日期')
axes[0].set_ylabel('步数/距离')

# 消耗卡路里
axes[1].bar(daily_calories.index, daily_calories)
axes[1].set_xlabel('日期')
axes[1].set_ylabel('消耗卡路里')

# 心率
axes[2].plot(daily_heart_rate, marker='o')
axes[2].set_xlabel('日期')
axes[2].set_ylabel('心率')

# 温度和体温变化
axes[3].plot(daily_temperature, marker='o')
axes[3].plot(daily_body_temperature, marker='o')
axes[3].legend(['温度', '体温'])
axes[3].set_xlabel('日期')
axes[3].set_ylabel('温度/体温')

# 设置图表标题和布局
fig.suptitle('手环数据分析', fontsize=16)
fig.tight_layout()

# 展示图表
plt.show()
