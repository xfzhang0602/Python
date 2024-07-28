# @Time :2024/7/22 下午8:53
# @Author : xfzhang0602@163.com
# @File : demo1.py
# @Software: PyCharm


'''
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
print(word)
print(sentence)
print(paragraph)



str1 = "itsishu"
#正向索引：
# 0123456
#反向索引：
# -7...-3,-2 ,-1
print(len(str1)) # 内置函数 len() 获取字符串长度
print(str1) # 打印字符串
print(f"{str1}[2]:",str1[2]) # 获取字符串中的第二个字符
print(f"{str1}[0:2]:",str1[0:2]) # 截取字符串索引值为0~1的字符，不包括索引值为2的字符 [0,2) 左闭右开区间。
print(f"{str1}[2:5]:",str1[2:5]) # 截取字符串索引值为2~4的字符，不包括索引值为5的字符 [2,5) 左闭右开区间。
print(f"{str1}[2:-1]:",str1[2:-1]) # 截取字符串重索引值为2开始直到字符串结尾的前一个，-1的索引值表示最后一个
print(f"{str1}[2:len(str1)]:",str1[2:len(str1)]) # 截取字符串索引值2~8，最后一个字符的索引值为7，所以刚刚好能截取到字符串末尾
# 截取在列表中索引值为0-4的数据，冒号前面不设置参数，默认从0开始
print(f"{str1}[:4]:",str1[:4])
# 截取在列表中索引值为2-末尾的数据，冒号后面不设置参数，默认截取到最后一位数据
print(f"{str1}[2:]:",str1[2:])
print(f"{str1}[0:7:2]:",str1[0:7:2]) # [起始位置：结束位置：间隔值]
print(f"{str1}[-1:-6:-1]:",str1[-1:-6:-1]) #反向索引，倒序打印



str1 = "IT私塾。"
str1 += "学以致用"
print(str1 + "高效学习")
print('-' * 30)
str2 = "这是一个很长的字符串，以至于一行都写不完" \
"那就第二行接着写" \
"可以一直写下去，都算一个字符串"
print(str2)



# capitalize 字符串首字母大写
str1 = "itsishu"
res = str1.capitalize()
print(res) #输出:Itsishu
# title 每个单词的首字母大写 (非字母隔开的单词)
str1 = "It si shu"
res = str1.title()
print(res) #输出:It Si Shu
res = str1.istitle() #判断每个单词的首字母是否大写
print(res) #输出:False
#upper 将所有字母变成大写
str1 = "It Si Shu"
res = str1.upper()
print(res) #输出:IT SI SHU
# lower 将所有字母变成小写
res = str1.lower()
print(res) #输出:it si shu
# swapcase 大小写互换
res = str1.swapcase()
print(res) #输出:iI sI sHU



#count 统计字符串中某个元素的数量
str1 = "it si shu"
res = str1.count("s") #s为2；it为1；IT为0
print(res)


#find 查找某个字符串第一次出现的索引位置
#find('字符串',开始位置,结束位置) 结束位置取不到,取到之前的一个值
str1 = "IT私塾：高效学习，学以致用"
res = str1.find("学") # 7，标点符号也算字符
res = str1.find("学",8) # 10
res = str1.find("学",1,8) #-1表示没有匹配到 [1,7) 左闭右开区间
res = str1.find("学习") # 7
print(res)

#index 与 find 功能相同 find找不到返回-1,index找不到数据直接报错
res = str1.index("it") # 推荐使用find
print(res)



# startswith 判断是否以某个字符或字符串为开头
# startswith('字符串',开始位置,结束位置) 返回True或False
str1 = "IT私塾：高效学习，学以致用"
res= str1.startswith("IT") #True
res = str1.startswith("学",10) #True
res = str1.startswith("学以",10,12) #True
print(res)
# endswith 判断是否以某个字符或字符串结尾
# endswith('字符串',开始位置,结束位置) 返回True或False
res = str1.endswith("用") #True
res = str1.endswith("学习",-9,-5) #True
print(str1[-9:-5]) #高效学习
print(res)



# str1 = "IT私塾 高效学习 学以致用"
# res = str1.split()
# print(res) #['IT私塾', '高效学习', '学以致用']

str1 = "IT_私塾_高效_学习_学以_致用"
# res = str1.split("_",2) # 第二个参数是分割几次 (从左向右)
# print(res) #输出：['IT', '私塾', '高效_学习_学以_致用']
#rsplit 从右向左分割
res = str1.rsplit("_",1) # (从右向左)
print(res) # 返回列表，输出：['IT_私塾_高效_学习_学以','致用']
# #join 按某字符将列表拼接成字符串(容器类型都可)
# listvar = ['IT私塾',"高效学习","学以致用"]
# res = "*".join(listvar)
# print(res) # 输出：IT私塾*高效学习*学以致用



# replace 替换字符串(第三个参数选择替换的次数)
str1 = "IT私塾 高效学习 学以致用"
res = str1.replace(" ","/")
print(res) #输出：IT私塾/高效学习/学以致用
# 第三个参数为替换的次数
res = str1.replace("学","练",1)
print(res) #输出：IT私塾 高效练习 学以致用
# strip 默认去掉首尾两边的空白符
str1 = "\r IT私塾 \t \n"
print(str1) #输出： IT私塾
res = str1.strip()
print(res)
print("end") #输出：IT私塾
# end
#lstrip(),只去掉左侧的空白符
res = str1.lstrip() #输出：IT私塾
print(res)
print("end") # end
# rstrip(),只去掉右侧的空白符
res = str1.rstrip()
print(res) #输出： IT私塾
print("end") # end




#isspace() 字符串中只包含空白，则返回 True，否则返回 False
res = " " #True
res = "\t \r\n" #True
print(res.isspace())
# isalpha 字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
res = "abc" #True
# res = "123" #False
# res = "123.0" #False
res = "$123" #False
print(res.isalpha())
# isalnum,字符串至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
res = "abc" #True
res = "abc123" #True
res = "123.0" #False
res = "$123" #False
print(res.isalnum())
# isdecimal 检测字符串是否以数字组成 必须是纯数字
# isdigit() 字符串只包含数字则返回 True 否则返回 False
# isnumeric() 字符串中只包含数字字符，则返回 True，否则返回 False
res = "1234" #True
# res = "1234.0" #False
# res = "$1234" #False
print(res.isdecimal())
num = "1" #unicode
print(f"{num} isdigit:",num.isdigit()) # True
print(f"{num} isdecimal:",num.isdecimal()) # True
print(f"{num} isnumeric:",num.isnumeric()) # True
#切换全角：win10 在输入法的”设置“中，”按键“，选择”全/半角切换”中的“Shift+空格
num = "１" # 全角
print(f"{num} isdigit:",num.isdigit()) # True
print(f"{num} isdecimal:",num.isdecimal()) # True
print(f"{num} isnumeric:",num.isnumeric()) # True
num = b"1" # byte
print(f"{num} isdigit:",num.isdigit()) # True
#print(f"{num} isdecimal:",num.isdecimal()) # AttributeError 'bytes' object has
no attribute 'isdecimal'
#print(f"{num} isnumeric:",num.isnumeric()) # AttributeError 'bytes' object has
no attribute 'isnumeric'
num = "Ⅳ" # 罗马数字4
print(f"{num} isdigit:",num.isdigit()) # False
print(f"{num} isdecimal:",num.isdecimal()) # False
print(f"{num} isnumeric:",num.isnumeric()) # True
num = "四" # 汉字4
print(f"{num} isdigit:",num.isdigit()) # False
print(f"{num} isdecimal:",num.isdecimal()) # False
print(f"{num} isnumeric:",num.isnumeric()) # True




# len 计算容器类型长度
res = len("IT私塾")
print(res) #输出：4
# center 填充字符串,原字符居中 (默认填充空格)
str1 = "IT私塾"
res = str1.center(10,"*") #center(填充的个数,填充的字符)
print(res) #输出：***IT私塾***




# max 返回字符串中编码最大的字母
# min 返回字符串中编码最小的字母
str1 = "IT私塾"
print(max(str1)) #输出：私
print(min(str1)) #输出：I
# ord,内置函数，返回汉字或字母的Unicode编码
print("'I'的编码",ord("I")) #输出：'I'的编码 73
print("'T'的编码",ord("T")) #输出：'T'的编码 84
print("'私'的编码",ord("私")) #输出：'私'的编码 31169
print("'塾'的编码",ord("塾")) #输出：'塾'的编码 22654
#python3 默认是unicode，16位的编码
print(chr(22654)) #编码为65的字符 #输出：塾
str = "IT私塾"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
#b表示字节 2字符 = 2字节 1字节 = 8bit 比特位 比特 0或1
print(str)
print("UTF-8 编码：", str_utf8,type(str_utf8))
#输出：UTF-8 编码： b'IT\xe7\xa7\x81\xe5\xa1\xbe' <class
'bytes'>
print("GBK 编码：", str_gbk,type(str_gbk))
#输出：GBK 编码： b'IT\xcb\xbd\xdb\xd3' <class 'bytes'>
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict')) #输出：UTF-8 解码： IT私
塾
print("GBK 解码：", str_gbk.decode('GBK','strict')) #输出：GBK 解码： IT私塾

'''








