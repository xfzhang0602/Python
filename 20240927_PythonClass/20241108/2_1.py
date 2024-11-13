import pandas as pd
import matplotlib.pyplot as plt

# 假设 gps_data 已经加载
# 请替换成正确的文件路径
gps_data = pd.read_csv('D:\\Users\\15055\\Desktop\\研一\\python大数据\\【批量下载】xiamen等3个文件\\taxiGps20190602\\taxiGps20190602.csv')

# 1. 处理 'GPS_TIME' 列，确保其为 datetime 类型
# 如果没有时间部分，填充为 ' 00:00:00'
gps_data['GPS_TIME'] = gps_data['GPS_TIME'].apply(lambda x: x if ' ' in x else x + ' 00:00:00')

# 使用 pd.to_datetime() 转换为 datetime 类型
gps_data['GPS_TIME'] = pd.to_datetime(gps_data['GPS_TIME'], format='%Y/%m/%d %H:%M:%S', errors='coerce')

# 2. 使用 groupby 按小时统计数据量
# 提取小时
gps_data['hour'] = gps_data['GPS_TIME'].dt.hour

# 按小时统计 GPS 数据量
hourly_data = gps_data.groupby('hour').size()

# 3. 使用 matplotlib 绘制每小时 GPS 数据量图表
plt.figure(figsize=(10,6))
plt.plot(hourly_data.index, hourly_data.values, marker='o', linestyle='-', color='b')
plt.title('Hourly GPS Data Count')
plt.xlabel('Hour of Day')
plt.ylabel('Number of GPS Records')
plt.grid(True)
plt.xticks(range(0, 24))  # 显示 0-23 小时
plt.tight_layout()
plt.show()
