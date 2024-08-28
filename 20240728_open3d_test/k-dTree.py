#功能 点云相交、求异
import open3d as o3d
import numpy as np
#首先读取原始点云和求异点云
pc1 = o3d.io.read_point_cloud("1.ply",remove_nan_points=True,remove_infinite_points=True)#原始点云
pc2 = o3d.io.read_point_cloud("2.ply",remove_nan_points=True,remove_infinite_points=True)#求异点云
#建立原始数据点云的k-d树结构
k_dTree = o3d.geometry.KDTreeFlann(pc1)
#ptsIdx是指灵片点云中相同部分的索引
ptsIdx=[]
#k是指K-NN搜索的参数，也就是说搜索另外一片点云中距离它的最近点
k=1
#将距离阈值设置为8.1
dist_max=0.1
#得到点个数
points = np.array(pc2.points)
pointNum=points.shape[0]
#遍历点云
for i in range(0, pointNum):
    #k返回点个数
    # idx 返回点索引
    # dist 返回点距离
    [k, idx,dist]= k_dTree.search_knn_vector_3d(pc2.points[i],k)#通过k-d Tree进行搜索最近点
    if dist[0]< dist_max:#如果另外一片点云中能够找到距离小于给定距离阌值的点，则判定为点云中相同的部分
            ptsIdx.append(i)

#最后将点云中相同的部分和不同的部分分别取出来进行显示
same_part=pc2.select_by_index(ptsIdx)
diff_part=pc2.select_by_index(ptsIdx,invert=True)
same_part.paint_uniform_color([0,0,1])
diff_part.paint_uniform_color([1,0,0])
o3d.visualization.draw_geometries([same_part,diff_part])