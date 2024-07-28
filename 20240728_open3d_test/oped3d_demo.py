# @Time :2024/7/28 上午11:43
# @Author : xfzhang0602@163.com
# @File : oped3d_demo.py
# @Software: PyCharm



'''
import numpy as np
import open3d as o3d

# 生成随机点云数据
points = np.random.rand(10000, 3)
# 创建Open3D点云对象
point_cloud = o3d.geometry.PointCloud()
# 将点云数据赋值给Open3D点云对象
point_cloud.points = o3d.utility.Vector3dVector(points)
# 可视化点云
o3d.visualization.draw_geometries([point_cloud])

'''





import open3d as o3d
import numpy as np

# 创建一个简单的立方体点云
points = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])

# 创建Open3D点云对象
point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)

# 可视化点云
o3d.visualization.draw_geometries([point_cloud])
