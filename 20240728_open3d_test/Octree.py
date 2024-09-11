import open3d as o3d
pcd = o3d.io.read_point_cloud("d:\\code\\Python\\Python\\20240728_open3d_test\\wukong.pcd")
# 设置颜色，将点云pcd的颜色设置为统一的红色（RGB值为[1.0, 0.0, 0.0]）。
pcd.paint_uniform_color([1.0, 0.0, 0.0])
#建立八叉树
octree=o3d.geometry.Octree(max_depth=10)#设置了最大深度为10
octree.convert_from_point_cloud(pcd,size_expand=0.1)#使用convert_from_point_cloud方法将点云数据转换为八叉树结构，size_expand参数用于设置叶子节点的大小。
# 可视化
o3d.visualization.draw_geometries([octree], window_name="八叉树",width=800,height=600)






# import open3d as o3d

# try:
#     pcd = o3d.io.read_point_cloud("d:\\code\\Python\\Python\\20240728_open3d_test\\bunny.ply")
#     if pcd.is_empty():
#         raise ValueError("点云文件为空或不存在")
    
#     # 设置颜色
#     pcd.paint_uniform_color([1.0, 0.0, 0.0])
    
#     # 建立八叉树
#     octree = o3d.geometry.Octree(max_depth=10)  # 设置最大深度
#     octree.convert_from_point_cloud(pcd, size_expand=0.1)  # size expand叶子节点大小
    
#     # 可视化
#     o3d.visualization.draw_geometries([octree], window_name="八叉树", width=800, height=600)
# except Exception as e:
#     print(f"发生错误: {e}")



# import open3d as o3d
# import os

# file_path = "d:\\code\\Python\\Python\\20240728_open3d_test\\bunny.ply"

# try:
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f"{file_path} 文件不存在")
    
#     pcd = o3d.io.read_point_cloud(file_path)
#     if pcd.is_empty():
#         raise ValueError("点云文件为空")
    
#     # 设置颜色
#     pcd.paint_uniform_color([1.0, 0.0, 0.0])
    
#     # 建立八叉树
#     octree = o3d.geometry.Octree(max_depth=10)  # 设置最大深度
#     octree.convert_from_point_cloud(pcd, size_expand=0.1)  # size expand叶子节点大小
    
#     # 可视化
#     o3d.visualization.draw_geometries([octree], window_name="八叉树", width=800, height=600)
# except Exception as e:
#     print(f"发生错误: {e}")



# import os
# print(os.getcwd())  # 打印当前工作目录
     





# import open3d as o3d
# import numpy as np

# # 读取点云
# pcd = o3d.io.read_point_cloud("d:\\code\\Python\\Python\\20240728_open3d_test\\wukong.pcd")

# # 计算单位体积/面积的点数量
# points = np.asarray(pcd.points)
# # 假设点云是均匀分布的，这里简单地用点数除以体积
# # 注意：get_volume()方法在Open3D中并不存在，这里假设点云是一个立方体，体积为(max(x)-min(x))*(max(y)-min(y))*(max(z)-min(z))
# min_bound = pcd.get_min_bound()
# max_bound = pcd.get_max_bound()
# volume = np.prod(max_bound - min_bound)
# point_density = len(points) / volume
# print(f"单位体积的点数量: {point_density}")

# # 计算点云中点的平均距离
# distances = []
# kdtree = o3d.geometry.KDTreeFlann(pcd)
# for point in points:
#     [k, idx, _] = kdtree.search_knn_vector_3d(point, 2)  # 查找每个点的最近邻点（包括自身）
#     if k > 1:
#         distances.append(np.linalg.norm(point - points[idx[1]]))  # 计算到最近邻点的距离
# average_distance = np.mean(distances)
# print(f"点云中点的平均距离: {average_distance}")

