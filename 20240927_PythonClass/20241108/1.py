import pandas as pd

# 1. 读取数据
data = pd.read_csv('D:\\Users\\15055\\Desktop\\研一\\python大数据\\【批量下载】xiamen等3个文件\\taxiGps20190602\\taxiGps20190602.csv')

# 检查数据前几行
print(data.head())

# 2. 数据筛选
# 选择相关列：OPERATING_STATUS, GPS_TIME, LONGITUDE, LATITUDE, CARNO
data = data[['OPERATING_STATUS', 'GPS_TIME', 'LONGITUDE', 'LATITUDE', 'CARNO']]

# 3. 数据清洗
data.dropna(inplace=True)
data = data[(data['LONGITUDE'] >= 118) & (data['LONGITUDE'] <= 120) &
            (data['LATITUDE'] >= 24) & (data['LATITUDE'] <= 25)]

# 4. 生成OD数据
data.sort_values(['CARNO', 'GPS_TIME'], inplace=True)

od_data = []

# 遍历每辆车的数据，根据运营状态生成OD记录
for carno, group in data.groupby('CARNO'):
    origin = None

    for _, row in group.iterrows():
        if row['OPERATING_STATUS'] == 6 and origin is None:
            # 记录起点（乘客上车）
            origin = row
        elif row['OPERATING_STATUS'] == 1 and origin is not None:
            # 记录终点（乘客下车）并生成OD记录
            od_data.append({
                'CARNO': carno,
                'origin_time': origin['GPS_TIME'],
                'origin_longitude': origin['LONGITUDE'],
                'origin_latitude': origin['LATITUDE'],
                'destination_time': row['GPS_TIME'],
                'destination_longitude': row['LONGITUDE'],
                'destination_latitude': row['LATITUDE']
            })
            origin = None

# 转换OD数据为DataFrame
od_df = pd.DataFrame(od_data)

# 输出生成的OD数据
print(od_df.head())


# 保存为 CSV 文件
od_df.to_csv('od_data.csv', index=False, encoding='utf-8-sig')
