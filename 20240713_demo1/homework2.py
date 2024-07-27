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





'''

# （2）一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

# 计算总距离
total_distance = 100  # 第一次落地的距离
height = 100  # 初始高度

for i in range(1, 10):
    height /= 2
    total_distance += 2 * height

print(f"第10次落地时，共经过 {total_distance} 米")

# 计算第10次反弹的高度
height = 100  # 初始高度

for i in range(9):
    height /= 2

print(f"第10次反弹的高度是 {height} 米")


'''





'''
# （3）有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？


# 生成所有由1、2、3、4组成的不重复的三位数

numbers = [1, 2, 3, 4]
valid_numbers = []

for i in numbers:
    for j in numbers:
        for k in numbers:
            if i != j and j != k and i != k:
                valid_numbers.append(i * 100 + j * 10 + k)

# 打印结果
count = len(valid_numbers)
print(f"共有 {count} 个互不相同且无重复数字的三位数，它们是：")
for number in valid_numbers:
    print(number)

'''




'''
# （4）一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数。


# （4）一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数。

def find_perfect_numbers(limit):
    perfect_numbers = []

    for num in range(2, limit):  # 从2开始，因为1没有真因子
        sum_of_factors = 0

        # 找出num的所有真因子
        for i in range(1, num):
            if num % i == 0:
                sum_of_factors += i

        # 如果因子之和等于num，则为完数
        if sum_of_factors == num:
            perfect_numbers.append(num)

    return perfect_numbers


# 找出1000以内的所有完数
perfect_numbers = find_perfect_numbers(1000)

# 打印结果
print("1000以内的完数有：")
for number in perfect_numbers:
    print(number)



'''





'''
# （5）输入两个数值：
# 		求两个数的最大公约数和最小公倍数
# 		最小公倍数=(num1 * num2) / 最大公约数


# 输入两个数值，求两个数的最大公约数和最小公倍数

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

num1 = int(input("请输入第一个数: "))
num2 = int(input("请输入第二个数: "))

gcd_result = gcd(num1, num2)
lcm_result = lcm(num1, num2)

print(f"{num1} 和 {num2} 的最大公约数是: {gcd_result}")
print(f"{num1} 和 {num2} 的最小公倍数是: {lcm_result}")


'''




'''
# （6）将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

# （6）将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

def prime_factors(n):
    factors = []
    divisor = 2

    while n >= 2:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

num = int(input("请输入一个正整数: "))

factors = prime_factors(num)
factors_str = "*".join(map(str, factors))

print(f"{num} = {factors_str}")


'''




'''
# （7）打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。

# （7）打印出所有的“水仙花数”

def is_narcissistic(num):
    # 获取个位、十位和百位数字
    hundreds = num // 100
    tens = (num % 100) // 10
    units = num % 10

    # 计算各位数字的立方和
    sum_of_cubes = hundreds ** 3 + tens ** 3 + units ** 3

    # 检查是否为水仙花数
    return sum_of_cubes == num


# 打印所有的水仙花数
print("所有的水仙花数：")
for i in range(100, 1000):
    if is_narcissistic(i):
        print(i)


'''



'''
# （8）用户登录需求：
#
# - 输入用户名和密码；
#
# - 判断用户名和密码是否正确（name=‘root’,passwd=‘123456’）,密码输入错误三次则会报错
#
# - 登录仅有三次机会，超过3次会报错


# （8）用户登录需求：输入用户名和密码；
# 判断用户名和密码是否正确（name='root', passwd='123456'）,密码输入错误三次则会报错
# 登录仅有三次机会，超过3次会报错

# 正确的用户名和密码
correct_name = 'root'
correct_passwd = '123456'

# 最大尝试次数
max_attempts = 3

for attempt in range(max_attempts):
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    if username == correct_name and password == correct_passwd:
        print("登录成功")
        break
    else:
        remaining_attempts = max_attempts - (attempt + 1)
        if remaining_attempts > 0:
            print(f"用户名或密码错误，还有 {remaining_attempts} 次尝试机会")
        else:
            print("用户名或密码错误，尝试次数已用完，登录失败")

# 如果所有尝试均失败，输出错误信息
if username != correct_name or password != correct_passwd:
    print("登录失败，程序终止")



'''


''''''
# （10）【递归练习】
# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？


# （10）【递归练习】
# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

def fibonacci(n):
    # 如果是第一个月或第二个月，兔子总数为1对
    if n == 1 or n == 2:
        return 1
    # 否则兔子总数为前两个月之和
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

month = int(input("请输入月份数: "))
total_rabbits = fibonacci(month)
print(f"第 {month} 个月的兔子总数为 {total_rabbits} 对")


