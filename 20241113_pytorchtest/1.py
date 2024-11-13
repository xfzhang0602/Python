# @Time :2024/11/13 上午9:14
# @Author : xfzhang0602@163.com
# @File : 1.py.py
# @Software: PyCharm


import torch

print(torch.__version__)
print(torch.version.cuda)
print(torch.cuda.is_available())  # 输出为True，则安装成功
