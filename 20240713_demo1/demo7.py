# @Time :2024/7/21 下午8:37
# @Author : xfzhang0602@163.com
# @File : demo7.py
# @Software: PyCharm


'''
//1.for循环
for i in range(5): #相当于range(0,5),打印范围是 [0,5),左闭右开区间
    print(i)
print('end')


for i in range(0,12,3):
    print(i)


for i in range(-10,-101,-30):
    print(i)



#字符串
city = "chengdu"
for i in city:
    print(i,end="\t")

#元组
a = (10,20,30)
for i in a:
    print(i)

#列表
n = ["aa","bb","cc"]
for i in n:
    print(i)
n = ["aa","bb","cc","dd"]
print(len(n))
for _ in range(len(n)):
    print(f"{_}位置，元素{n[_]}")

while True: #死循环，交互模式种使用Ctrl+C中断程序运行
    s = input("请输入内容：")
    print("您输入了：", s)
i = 0
while i<5:
    print(i)
i += 1 #i = i + 1



total = 0 #保存求和结果
n = 1 #当前循环的数字
while n <= 100:
    total += n #total = total + n
    n += 1
print("1到100的和为：",total)


#range(101) #[0,100]
print("1到100的和为：",sum(range(101)))

total = 0
n = 100
while n > 0:
    total += n
    n -= 2
print("1到100的偶数和为：",total)




i = 0
while i<10:
    i = i+1
    print('----')
    if i==5:
        continue
    print(i)


for i in range(3):
    cmd = input("请输入指令:")
    if cmd == "exit":
        break
    print("您输入了",cmd)
else: #else语句在循环被中断的情况下不执行
    print("您输入了3次命令")



a = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
for j in a:
    print(j,end="、")
print()
for i in range(4):
    print(f"第{i+1}周:")
    for j in a:
        print(j,end="、")
    print(i)

'''







 







































