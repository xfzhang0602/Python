import open3d as o3d
import numpy as np

#获取示例数据
source_cloud =o3d.io.read_point_cloud("cloud bin e.pcd")
target_cloud =o3d.io.read_point_cloud("cloud bin 1.pcd")
source_cloud.paint_uniform_color([1,0.706,0])
target_cloud.paint_uniform_color([0,0.651,0.929])
threshold=0.02   #RMSE残差阈值，小于该残差值，迭代终止

#初始位姿
trans_init =np.asarray([[0.862,0.011,-0.507,0.5],
                        [-0.139,0.967,-0.215,0.7],
                         [0.487,0.255,0.835,-1.4],
                          [0.0,0.0,0.0,1.0]])

#显示未配准点云
o3d.visualization.draw_geometries([source_cloud, target_cloud],
                                  zoom=0.4459,
                                  front=[0.9288,-0.2951,-0.22421]
                                  lookat=[1.6784,2.0612,1.4451]
                                  up=[-0.3402,-0.9189,-0.1996])

#点到点的ICP
result =o3d.pipelines.registration.registration_icp(
       source_cloud,target_cloud,threshold,trans_init,
       o3d.pipelines.registration.TransformationEstimationPointToPoint())
print(result)
print("Transformation is:")
print(result.transformation)

#显示点到点的配准结果
source_cloud.transform(result.transformation)
o3d.visualization.draw_geometries([source_cloud, target_cloud],
                                  zoom=0.4459,
                                  front=[0.9288,-0.2951,-0.2242],
                                  lookat=[1.6784,2.0612,1.4451],
                                  up=[-0.3402,-0.9189,-0.1996])

#重置点到点的配准结果
source_cloud=o3d.io.read_point_cloud("cloud bin g.pcd")
target_cloud =o3d.io.read_point_cloud("cloud bin 1.pcd")
source_cloud.paint_uniform_color([1,0.706,0])
target_cloud.paint_uniform_color([0,0.651,0.929])

#点到面的ICP
result=o3d.pipelines.registration.registration_icp(
    source_cloud,target_cloud,threshold,trans_init,
    o3d.pipelines.registration.TransformationEstimationPointToPlane())
print(result)
print("Transformation is:")
print(result.transformation,"\n")

#显示点到面的配准结果
source_cloud.transform(result.transformation)
o3d.visualization.draw_geometries([source_cloud, target cloud],
                                  zoom=0.4459,
                                  front=[0.9288,-0.2951,-0.22421],
                                  lookat=[1.6784,2.0612,1.4451],
                                  up=[-0.3402,-0.9189,-0.1996])
