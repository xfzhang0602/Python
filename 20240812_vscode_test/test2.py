import open3d as o3d
import numpy as np

# 生成一些随机点
points = np.random.rand(100, 3)  # 生成100个三维随机点

# 创建点云对象
point_cloud = o3d.geometry.PointCloud()

# 将点添加到点云对象中
point_cloud.points = o3d.utility.Vector3dVector(points)

# 可视化点云
o3d.visualization.draw_geometries([point_cloud])
