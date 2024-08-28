import open3d as o3d
import numpy as np
from os import listdir
from os.path import isfile, join
 
# 指定包含点云文件的目录
cloud_dir = 'D:\Users\15055\Downioads\斯坦福bunny\data'
 
# 只获取.pcd格式的文件
files = [f for f in listdir(cloud_dir) if isfile(join(cloud_dir, f)) and f.endswith('.pcl')]
 
# 初始化一个空的点云
merged_cloud = o3d.geometry.PointCloud()
 
for file in files:
    # 加载每个点云文件
    pcd = o3d.io.read_point_cloud(join(cloud_dir, file))
 
    # 将点云添加到合并后的点云中
    merged_cloud += pcd
 
# 保存合并后的点云
o3d.io.write_point_cloud('merged_rabbit.pcd', merged_cloud)