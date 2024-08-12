# 同时显示两个窗口，按ESC退出
import open3d as o3d
from pynput import keyboard    # 加载pynput用于键盘监听

# 当键盘按下时的回调函数
def on_press(key):
    global stop_flag
    if key == keyboard.Key.esc:
        stop_flag = True

pcd_1 = o3d.io.read_point_cloud("cloud_bin_0.pcd")
vis_1 = o3d.visualization.Visualizer()

pcd_2 = o3d.io.read_point_cloud("cloud_bin_1.pcd")
vis_2 = o3d.visualization.Visualizer()

# 创建窗口
vis_1.create_window(window_name="Window 1", width=1080, height=720)
vis_2.create_window(window_name="Window 2", width=1080, height=720)

# 添加点云数据
vis_1.add_geometry(pcd_1)
vis_2.add_geometry(pcd_2)

# 开始键盘监听
listener = keyboard.Listener(on_press=on_press)
listener.start()

# 窗口循环渲染
stop_flag = False
while not stop_flag:
    vis_1.poll_events()
    vis_1.update_renderer()
    
    vis_2.poll_events()
    vis_2.update_renderer()

# 销毁窗口
vis_1.destroy_window()
vis_2.destroy_window()

# 停止监听
listener.stop()
