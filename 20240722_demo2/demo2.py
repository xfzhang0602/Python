# @Time :2024/7/27 下午9:15
# @Author : xfzhang0602@163.com
# @File : demo2.py
# @Software: PyCharm


'''
namelist = [] #定义一个空的列表

namelist = ["小张","小王","小李"]
print(namelist,type(namelist)) #输出：[] <class 'list'>


testList = [1, 'a', True, 2.3, 1] #元素内容可以重复




a = list() #创建一个空的列表对象
print(a)
a = list(range(10)) #将range所定义的数据作为列表元素 [0,9)
a = list(range(2,-3,-1))
print(a)
a = list("IT私塾") #将字符串的每个字符作为列表元素



a = [x*2 for x in range(5)] #循环创建多个元素
print(a)



# # （1）len() 获取列表元素个数
# namelist = ["小张","小王","小李","小赵"]
# print(len(namelist)) #4
# i = 0
# while i < len(namelist):
#     print(namelist[i])
#     i += 1
#
#（2）max() 和min() 获取列表中最大和最小的元素
# list1 = [3,2,1]
# list1= ["aa","bb","cc"]
# #list1 = [False, 2.0, 30, "aa"] #max和min函数调用时会报错，字符串和数值无法比较
# list1 = [0, False, 2.0, 30]
# print(max(list1))
# print(min(list1))

#(3) sum() 对全部为数值型元素的列表求和
list1 = [10,20,30,2.0,True]
print(sum(list1)) #输出：63.0





#增： 【append】追加
namelist = ["小张","小王","小李","小赵"]
print("-------增加前，名单列表的数据-------")
for name in namelist:
    print(name,end=",")
nametemp = input("\n请输入学生姓名：")
namelist.append(nametemp) #在末尾追加一个元素
print("-------增加后，名单列表的数据-------")
for name in namelist:
    print(name,end=",")


#增： 【extend】扩展
a = [1,2]
b = [3,4]
# a.append(b) #将列表当作一个元素，加入到a列表中
# print(a)
a.extend(b) #将b列表中的每个元素，逐一追加到a列表中
print(a)
'''


#增： 【+】连接
list1 = [10,20,30]
list2 = [40,50]
res = list1 + list2
print(res,id(res)) #[10, 20, 30, 40, 50]
print(list1,id(list1))
list1.extend(list2)
print(list1,id(list1))


















