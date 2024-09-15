import open3d as o3d
import numpy as np
import copy
def draw_registration_result(source, target, transformation):
    source_temp= copy.deepcopy(source)
    source_temp.transform(transformation)
    source_temp.paint_uniform_color([0, 0, 1])
    target.paint_uniform_color([1, 0, 0])
    o3d.visualization.draw([source_temp, target])

source = o3d.io.read_point_cloud("frag_ 115.ply")
target =o3d.io.read_point_cloud("frag_116.ply")
#初始位姿
current_transformation = np.identity(4)
#显示未配准点云
draw_registration_result(source, target, current_transformation)
print(current_transformation)
voxel_radius=[0.04,0.02,0.01]
max_iter =[50,30,14]
current_transformation = np.identity(4)

print(current_transformation)

for scale in range(3):
    iter = max_iter[scale]
    radius = voxel_radius[scale]
    print([iter, radius, scale])

#采样 加快处理速度
source_down=source.voxel_down_sample(radius)
target_down=target.voxel_down_sample(radius)

#计算法线
source_down.estimate_normals(
    o3d.geometry.KDTreeSearchParamHybrid(radius=radius * 2, max_nn=30))
target_down.estimate_normals(
    o3d.geometry.KDTreeSearchParamHybrid(radius=radius * 2, max_nn=30))

# Color ICP
result_icp = o3d.pipelines.registration.registration_colored_icp(
    source_down,target_down,radius,current_transformation.
    o3d.pipelines.registration.TransformationEstimationForColoredICP()
    o3d.pipelines.registration.ICPConvergenceCriteria(
        relative fitness=1e-6,relative rmse=1e-6,max iteration=iter))
current_transformation = result_icp.transformation
print(result_icp, "\n")

#显示配准结果
draw_registration_result(source, target, result_icp.transformation)