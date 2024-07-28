# @Time :2024/7/28 下午4:18
# @Author : xfzhang0602@163.com
# @File : test.py
# @Software: PyCharm

#
# import numpy as np
# import open3d as o3d
#
#
# points = np.random.rand(10000, 3)
# point_cloud = o3d.geometry.PointCloud()
# point_cloud.points = o3d.utility.Vector3dVector(points)
# o3d.visualization.draw_geometries([point_cloud])

# import numpy as np
# import open3d as o3d
#
# # 生成简单的点云数据
# points = np.random.rand(1000, 3)
# print("Points generated:", points.shape)
#
# # 创建Open3D点云对象
# point_cloud = o3d.geometry.PointCloud()
# # 将点云数据赋值给Open3D点云对象
# point_cloud.points = o3d.utility.Vector3dVector(points)
# print("Point cloud created")
#
# # 可视化点云
# o3d.visualization.draw_geometries([point_cloud])



#
# import open3d as o3d
# import numpy as np
#
# print("->正在加载点云... ")
# pcd = o3d.io.read_point_cloud("E:/1 基于手持LiDAR的文物三维模型重建/扫描暂存/鼎/模型/原始点云.txt")
# print(pcd)
#
# print("->正在可视化点云")
# o3d.visualization.draw_geometries([pcd])



import open3d as o3d
import numpy as np

# 使用相对路径读取点云文件
file_path = "E:/1 基于手持LiDAR的文物三维模型重建/扫描暂存/模型偏差分析/原始点云.pcd"

print("->正在加载点云... ")
try:
    pcd = o3d.io.read_point_cloud(file_path)
    if pcd.is_empty():
        raise ValueError("点云文件为空或格式不正确")
except Exception as e:
    print(f"读取点云文件时发生错误: {e}")
    exit(1)

print(pcd)

print("->正在可视化点云")
vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(pcd)
vis.run()
vis.destroy_window()

