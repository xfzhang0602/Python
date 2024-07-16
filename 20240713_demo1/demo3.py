# @Time: 2024/7/14 
# @Author:xfzhang0602
# @File:demo3.py
# @Software: PyCharm

'''
# %输出
age=18
country="中国"
print("我的年龄是%d岁，我来自%s"%(age,country))


#format()函数
#1.顺序填充
str="我的名字是{}，我的年龄是{}，我的国籍是{}".format("张三",18,"中国")
print(str)

#2.索引填充
str="{0},{1},{0}".format("你好","世界")
print(str)

#3.关键字填充
str="姓名：{name},年龄：{age}".format(age=18,name="张三")
print(str)

#4.通过字典设置参数, ** 展开map集合
info = {"name":"张三","age":18}
str = "姓名:{name},年龄:{age}".format(**info)
print(str)


#5.利用列表的索引设置参数
list = ["IT私塾","www.itsishu.cn"]
str = "网站名称：{0[0]}，网址：{0[1]}，时间：{1}".format(list,2020)
print(str)


print("圆周率：{:+.2f}".format(3.1415926)) #输出：圆周率：+3.14
print("{:,}".format(10000000)) #输出：10,000,000
print("{:.2e}".format(1000000)) #输出：1.00e+06
print("{:.1%}".format(0.25)) #输出：25.0%


str = "IT私塾"
print("{:*>10}".format(str)) #输出：******IT私塾
print("{:*<10}".format(str)) #输出：IT私塾******
print("{:#^10}".format(str)) #输出：###IT私塾###

'''






