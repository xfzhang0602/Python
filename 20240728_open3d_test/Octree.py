import open3d as o3d
pcd = o3d.io.read_point_cloud("d:\\code\\Python\\Python\\20240728_open3d_test\\bunny.ply")
# 设置颜色
pcd.paint_uniform_color([1.0, 0.0, 0.0])
#建立八叉树
octree=o3d.geometry.Octree(max_depth=10)#设置最大深度
octree.convert_from_point_cloud(pcd,size_expand=0.1)#size expand叶子节点大小
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
     