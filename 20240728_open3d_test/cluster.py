import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
pcd =o3d.io.read_point_cloud("d:\\code\\Python\\Python\\20240728_open3d_test\\bunny1.ply")
o3d.visualization.draw_geometries([pcd])
with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug)as cm:
    labels=np.array(pcd.cluster_dbscan(eps=0.4,min_points=5))#进行聚类
min_label = labels.min()
max_label= labels.max()
pcList =[]
colors =plt.get_cmap("tab20")(labels /(max_label if max_label >0 else 1))
colors[labels<0]=0
pcd.colors=o3d.utility.Vector3dVector(colors[:,:3])
#分离出每个聚类的点云
for i in range(min_label,max_label+1):
    label_index=np.where(labels==i)
    temp_pc=pcd.select_by_index(np.array(label_index)[0])
    pcList.append(temp_pc)
    #o3d.visualization.draw geometries([temp pc])
    o3d.io.write_point_cloud(str(i)+".pcd",temp_pc)
o3d.visualization.draw_geometries([pcd])