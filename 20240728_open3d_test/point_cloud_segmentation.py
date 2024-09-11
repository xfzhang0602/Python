import open3d as o3d

pc=o3d.io.read_point_cloud("d:\\code\\Python\\Python\\20240728_open3d_test\\bunny1.ply")
pc=pc.uniform_down_sample(5) #采样
o3d.visualization.draw_geometries([pc])
# 返回模型系数plane model和内点索引inliers，并赋值
plane_model,inliers =pc.segment_plane(6.01,3,1008)#[距离模型的距离阈值，计算模型的点个数，随机次数]

#平面方程
[a, b,c,d]= plane_model
print("plane equation: {a:.2f}x + {b:.2f}y + {c:.2f}z + {d:.2f}= 0")
# 内点
inlier_cloud = pc.select_by_index(inliers)
inlier_cloud.paint_uniform_color([0,0,1.0])
#外点
outlier_cloud = pc.select_by_index(inliers, invert=True)
# outlier_cloud.paint_uniform_color([1.0,0,0])
# 可视化
o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])
#保存结果
o3d.io.write_point_cloud("plane.pcd",inlier_cloud)