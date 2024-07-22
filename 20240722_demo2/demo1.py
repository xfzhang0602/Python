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
'''
































