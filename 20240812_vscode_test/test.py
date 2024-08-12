import turtle

# 创建画布
canvas = turtle.Screen()

# 设置画布背景色
canvas.bgcolor("black")

# 创建画笔
pen = turtle.Turtle()

# 设置画笔颜色和粗细
pen.color("white")
pen.pensize(3)

# 绘制花瓣
for i in range(10):
    pen.circle(50)
    pen.right(36)

# 绘制花心
pen.color("yellow")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

# 隐藏画笔
pen.hideturtle()

# 完成绘制
turtle.done()
