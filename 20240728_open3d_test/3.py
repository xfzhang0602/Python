import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
# 0pen3D 0.16版本的 api

pcd =o3d.io.read_point_cloud("D:\\Users\\15055\\Desktop\\scannet\\scans\\scene0000_00\\scene0000_00_vh_clean_2.ply")
#计算法线
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=16), fast_normal_computation=True)
pcd.paint_uniform_color([0,0,1])

# #RANSAC
# [a,b,c,d], inliers = pcd.segment_plane(distance_threshold=0.01,ransac_n=3,num_iterations=1000)
# print(f"平面方程:{a:.2f}x+{b:.2f}y+{c:.2f}z+ {d:.2f} = θ")
# inlier_cloud = pcd.select_by_index(inliers)
# outlier_cloud =pcd.select_by_index(inliers, invert=True)
# inlier_cloud.paint_uniform_color([1.0,0,0])
# outlier_cloud.paint_uniform_color([0.6,0.6,0.6])
# o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])

# # DBSCAN
# labels =np.array(pcd.cluster_dbscan(eps=0.05,min_points=10))
# max_label = labels.max()
# print(f"point cloud has {max_label + 1} clusters")

# #给不同类别赋予不同的颜色
# colors = plt.get_cmap("tab20")(labels /(max_label if max_label > 0 else 1))
# colors[labels <0]=0
# pcd.colors =o3d.utility.Vector3dVector(colors[:,:3])
# o3d.visualization.draw_geometries([pcd])

segment_models={}
segments={}
max_plane_idx=40
rest=pcd
d_threshold=0.01
for i in range(max_plane_idx):
    colors = plt.get_cmap("tab20")(i)
    segment_models[i], inliers = rest.segment_plane(distance_threshold=0.01,ransac_n=3,num_iterations=1000)
    segments[i]=rest.select_by_index(inliers)
    labels = np.array(segments[i].cluster_dbscan(eps=d_threshold*10, min_points=10))
    candidates=[len(np.where(labels==j)[0]) for j in np.unique(labels)]
    best_candidate=int(np.unique(labels)[np.where(candidates==np.max(candidates))[0]])
    print("the best candidate is:",best_candidate)
    rest = rest.select_by_index(inliers, invert=True) + segments[i].select_by_index(list(np.where(labels != best_candidate)[0]))
    segments[i]=segments[i].select_by_index(list(np.where(labels==best_candidate)[0]))
    segments[i].paint_uniform_color(list(colors[:3]))
    print("pass",i+1,"/",max_plane_idx,"done.")

    labels = np.array(rest.cluster_dbscan(eps=0.05,min_points=5))
    max_label = labels.max()
    print(f"point cloud has {max_label + 1} clusters")

    colors = plt.get_cmap("tab10")(labels /(max_label if max_label > 0 else 1))
    colors[labels <0]=0
    rest.colors =o3d.utility.Vector3dVector(colors[:,:3])

# 为此，我们可以使用以下代码来创建一个合并的列表
all_segments = [segments[i] for i in range(max_plane_idx)] + [rest]

# 然后进行可视化
o3d.visualization.draw_geometries(all_segments)









# import open3d as o3d
# import numpy as np

# # 读取点云，确保路径正确
# pcd = o3d.io.read_point_cloud("D:\\Users\\15055\\Desktop\\scannet\\scans\\scene0000_00\\scene0000_00_vh_clean_2.ply")

# # 计算法线
# pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=16), fast_normal_computation=True)

# # 使用正确的颜色参数
# # 传入一个包含三个浮点数的列表，表示 RGB 颜色值
# pcd.paint_uniform_color([0.0, 0.1, 0.0])  # 绿色

# # RANSAC
# [a, b, c, d], inliers = pcd.segment_plane(distance_threshold=0.01, ransac_n=3, num_iterations=1000)
# print(f"平面方程: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f} = θ")

# # 选择内点和外点
# inlier_cloud = pcd.select_by_index(inliers)
# outlier_cloud = pcd.select_by_index(inliers, invert=True)

# # 颜色处理
# inlier_cloud.paint_uniform_color([1.0, 0, 0])  # 红色
# outlier_cloud.paint_uniform_color([0.6, 0.6, 0.6])  # 灰色

# # 可视化
# o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])



