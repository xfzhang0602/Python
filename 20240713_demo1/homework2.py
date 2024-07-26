# @Time :2024/7/26 下午10:34
# @Author : xfzhang0602@163.com
# @File : homework2.py
# @Software: PyCharm


'''

# 1.求1-100的所有数的和  			（for循环基本概念）


# 求1-100的所有数的和  （for循环基本概念）

total = 0

for i in range(1, 101):
    total += i

print(f"1到100的所有数的和是: {total}")

'''


'''
# 2.输出1-100内所有的奇数/偶数	（循环+条件语句）


# 输出1-100内所有的奇数/偶数  （循环+条件语句）

print("1到100内的所有奇数:")
for i in range(1, 101):
    if i % 2 != 0:
        print(i, end=' ')

print("\n1到100内的所有偶数:")
for i in range(1, 101):
    if i % 2 == 0:
        print(i, end=' ')

'''



'''
# 3.for循环打印金字塔					（双重循环）

# for循环打印金字塔  （双重循环）

height = int(input("请输入金字塔的高度: "))

for i in range(1, height + 1):
    # 打印每一行前面的空格
    for j in range(height - i):
        print(" ", end="")
    # 打印每一行的星号
    for k in range(2 * i - 1):
        print("*", end="")
    # 换行
    print()

'''

'''
# 4.for循环打印99乘法表				（双重循环）

# 4.for循环打印99乘法表  （双重循环）

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()
'''



'''
# 5.完成猜数字游戏：					 （break练习）
#
# - 系统随机生成一个1～100的数字；
#
# - 用户共有5次机会猜；
#
# - 如果用户猜测数字大于系统给出的数字，打印"大了"
#
# - 如果用户猜测数字小于系统给出的数字，打印"小了"
#
# - 如果用户猜测的数字等于系统给出的数字，打印"恭喜中奖"，并退出循环
#
#   >提示：
#   >
#   >随机生成一个整数的代码为：
#   >
#   >import random		#引入随机库
#   >
#   >num = random.randint(0,2)  	#随机生成0、1、2中的一个数字，赋值给变量num
#


# 5.完成猜数字游戏：  （break练习）

import random

# 系统随机生成一个1～100的数字
num = random.randint(1, 100)

# 用户共有5次机会猜
for i in range(5):
  user_guess = int(input(f"请输入您第{i + 1}次猜测的数字: "))

  if user_guess > num:
    print("大了")
  elif user_guess < num:
    print("小了")
  else:
    print("恭喜中奖")
    break  # 猜对了，退出循环

if user_guess != num:
  print(f"很遗憾，5次机会用完了。正确答案是 {num}")

'''


# 【扩展练习】



'''
# （1）猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个，第二天早上又将剩下的桃子吃掉一半，
# 又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。


# 猴子吃桃问题是经典的递归问题。我们可以从第10天开始，逆向推理回去，计算出第一天猴子摘了多少桃子。
#
# 设第n天猴子剩下的桃子数为P(n)，根据题意：
#
# 第10天早上剩下1个桃子，即P(10) = 1。
# 第n天早上剩下的桃子数是第n-1天晚上吃掉一半零一个后的结果，即P(n) = (P(n+1) + 1) * 2。
# 我们可以从第10天开始，逐步计算出第1天猴子摘的桃子数。
#
# 以下是Python代码实现：

def monkey_peach(day):
  if day == 10:
    return 1
  else:
    return (monkey_peach(day + 1) + 1) * 2


# 计算第一天猴子摘的桃子数
first_day_peaches = monkey_peach(1)
print(f"第一天猴子共摘了 {first_day_peaches} 个桃子")


# 解释：
#
# 第10天早上剩下1个桃子。
# 第9天晚上剩下的桃子数是(1 + 1) * 2 = 4。
# 第8天晚上剩下的桃子数是(4 + 1) * 2 = 10。
# 以此类推，直到第1天。
# 最终计算出第一天猴子摘了1534个桃子。



'''




# （2）一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？









