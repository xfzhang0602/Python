import pandas as pd
import matplotlib.pyplot as plt

# 读取OD数据文件
# 请替换成实际的文件路径
od_data = pd.read_csv('D:\\code\\Python\\Python\\20240927_PythonClass\\20241108\\od_data.csv')

# 1. 处理起点和终点的时间
# 转换为datetime类型
od_data['origin_time'] = pd.to_datetime(od_data['origin_time'], format='%Y/%m/%d %H:%M:%S', errors='coerce')
od_data['destination_time'] = pd.to_datetime(od_data['destination_time'], format='%Y/%m/%d %H:%M:%S', errors='coerce')

# 2. 提取起点和终点的小时
od_data['origin_hour'] = od_data['origin_time'].dt.hour
od_data['destination_hour'] = od_data['destination_time'].dt.hour

# 3. 统计每小时的OD数据量
# 统计起点时间的每小时数量
origin_hourly_count = od_data.groupby('origin_hour').size()

# 统计终点时间的每小时数量
destination_hourly_count = od_data.groupby('destination_hour').size()

# 4. 绘制每小时OD数据量的图表
plt.figure(figsize=(12,6))

# 绘制起点每小时数量
plt.subplot(1, 2, 1)
plt.plot(origin_hourly_count.index, origin_hourly_count.values, marker='o', linestyle='-', color='b')
plt.title('Hourly OD Data (Origin)')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Records')
plt.grid(True)
plt.xticks(range(0, 24))

# 绘制终点每小时数量
plt.subplot(1, 2, 2)
plt.plot(destination_hourly_count.index, destination_hourly_count.values, marker='o', linestyle='-', color='r')
plt.title('Hourly OD Data (Destination)')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Records')
plt.grid(True)
plt.xticks(range(0, 24))

# 调整布局
plt.tight_layout()
plt.show()
