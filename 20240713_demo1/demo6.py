# @Time :2024/7/20 下午9:45
# @Author : xfzhang0602@163.com
# @File : demo6.py
# @Software: PyCharm


'''
score = 90
if 90<= score and score <= 100:
    print("本次考试，等级为A")
if score >= 80 and score < 90:
    print("本次考试，等级为B")
if (score >= 70) and (score < 80):
    print("本次考试，等级为C")
if (score >= 60 and score < 70) :
    print("本次考试，等级为D")
if score >= 0 and score < 60:
    print("本次考试，等级为E")




score = 77
if 90 <= score <= 100:
    print("本次考试，等级为A")
elif 80 <= score < 90:
    print("本次考试，等级为B")
elif 70 <= score < 80:
    print("本次考试，等级为C")
elif 60 <= score < 70:
    print("本次考试，等级为D")
# elif 0 <= score <= 60: #elif可以和else一起使用
# print("本次考试，等级为E")
else:
    print("本次考试，成绩不合格")
'''


light = "红灯"
pedestrian = 1 #行人
turn_round = 0 #调头
if light == "绿灯":
    # 《道路交通安全法》第47条中的规定
    if pedestrian == 1:
        print("礼让，等待。。。。")
    else:
        print("绿灯行")
else :
    # 《道路交通安全法》第49条中的规定
    if turn_round == 1:
        print("可以调头。。。。")
    else:
        print("停止,等待。。。")

