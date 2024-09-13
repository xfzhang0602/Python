import open3d as o3d
# 采样、法线估计、计算 FPFH 特征
def preprocess_point_cloud(pcd, voxel_size):
    pcd_down=pcd.voxel_down_sample(voxel_size)
    pcd_down.estimate_normals(
        o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size * 2.0,
                                            max_nn=30))
    pcd_fpfh =o3d.pipelines.registration.compute_fpfh_feature(
        pcd_down,
        o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size * 5.0,
                                            max_nn=100))
    return(pcd_down, pcd_fpfh)

if __name__ =='__main__':
    src_path="cloud bin 0.pcd"
    dst_path="cloud bin 1.pcd"
    voxel_size=0.05 #采样格子大小
    max_iterations=64 #配准的最大迭代次数
    max_tuples=1000 #最多同名点个数
    distance_threshold=1.5*voxel_size #同名点之间距离阈值

    #读取数据
    src=o3d.io.read_point_cloud(src_path)
    dst=o3d.io.read_point_cloud(dst_path)

    src.paint_uniform_color([1, 0, 0])
    dst.paint_uniform_color([0, 1, 0])

    #显示配准之前的点云
    o3d.visualization.draw([src, dst])

    # 预处理
    src_down,src_fpfh= preprocess_point_cloud(src.voxel_size)
    dst_down,dst_fpfh = preprocess_point_cloud(dst, voxel_size)

    # FGR
    result = o3d.pipelines.registration.registration_fgr_based_on_feature_matching(
        src_down,dst_down,src_fpfh,dst_fpfh,
        o3d.pipelines.registration.FastGlobalRegistrationOption(
            maximum_correspondence_distance=distance_threshold, # 同名点之间的最大距离
            iteration_number=max_iterations,#最大迭代次数
            maximum_tuple_count=max_tuples))# 同名点对个数

    #显示配准后的点云
    o3d.visualization.draw([src.transform(result.transformation), dst])