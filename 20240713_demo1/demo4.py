# @Time: 2024/7/16 下午11:42
# @Author:xfzhang0602
# @File:demo4.py
# @Software: PyCharm

'''
#整型(int)
#type()函数可以查看变量的类型
a10 = 100           #数字100，十进制表示
print(type(a10))
a2 = 0b01100100     #数字100，二进制表示
print(a2,type(a2))
a8 = 0o144          #数字100，八进制表示
print(a8,type(a8))
a16 = 0x64          #数字100，十流进制表示
print(a16,type(a16))



#十进制转为二进制
print(bin(100)) #binary
#十进制转为八进制
print(oct(100)) #octonary
#十进制转为十六进制
print(hex(100)) #hexadecimal
#二进制：01100100 0 * 2**7 + 1 * 2**6 + 1 * 2**5 + 0 * 2**4 + 0 * 2**3
#               + 1 * 2**2 + 0 * 2**1 + 0 * 2**0
#十进制：100 1 * 10**2 + 0 * 10**1 + 0 * 10**0
#八进制：144 1 * 8**2 + 4 * 8**1 + 4 * 8**0
#十六进制：64 6 * 16**1 + 4 * 16**0



#1.顺序填充
str = "我的名字是{},我的年纪是{},我的国籍是{}".format("张三",18,"中国")
print(str)
#2.索引填充
str = "{0},{1},{0}!".format("你好","世界")
print(str)
#3.关键字填充
str = "姓名:{name},年龄:{age}".format(age=18,name="张三")
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

a = 3.1415926
print(a,type(a))
a = 2.1e-2 #浮点型表示方法一
b = 5.67e3 #浮点型表示方法二，科学计数法
print(a,type(a))
print(b,type(b))



c = 3 + 4j
print(c,type(c))
c = complex(3,4)
print(c,type(c))



#自动类型转换

#(a) bool + int
state = False #False在底层存储，本质是数字0
print("bool + int：",state + 3) #True在底层存储，本质是数字1
#(b) bool + float
print("bool + float: ",True + 3.2) #结果默认为浮点型
#(c) bool + complex
print("bool + complex: " , False + 2+3j)
#(d) int + float
print("int + float: " , 10 + 20.0)
#(e) int + complex
print("int + complex: " , 10 + 5+6j)
#(f) float + complex
print("float + complex: " , 3.14 + 5+6j)



num1 = 10
num2 = 22.99
num3 = True
num4 = 4+5j
num5 = "567"
num6 = "a78"
#int()
res = int(num2) #22
print(res)
res = int(num3) #True为1,False为0
res = int(num5) #567
print(res,type(num5))
#res = int(num6) #:报错
print(res)
#float()
res = float(num1) #10.0
res = float(num3) #0.0
res = float(num5) #567.0
print(res)
#complex
res = complex(num1) #10+0j
res = complex(num2) #22.22+0j
res = complex(num3) #1+0j
res = complex(num5) #567+0j
print(res)
#bool
res = bool(num4) #3+4j
print(res)
res = bool(num6) #a78
print(res)



a = 3.1415926
print(a,type(a))
a = 2.1e-2 #浮点型表示方法一
b = 5.67e3 #浮点型表示方法二，科学计数法
print(a,type(a))
print(b,type(b))




c = 3 + 4j
print(c,type(c))
c = complex(3,4)
print(c,type(c))




num1 = 10
num2 = 22.99
num3 = True
num4 = 4+5j
num5 = "567"
num6 = "a78"

res = float(num3) #1.0

print(res)

'''












