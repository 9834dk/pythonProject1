a=12
#数据类型转换
a=str(a)
print(type(a),a)

#字符串拼接使用+用来连接两个字符串之间
name = 'wadw'
address="wuhan"
print(name+"  "+address)

#字符串格式化使用占位符号 %s %d %f：实现多种类型拼接
name="动物的编号"
age=15
tel=4534
print(name+"大无畏")    #字符串格式化：只能字符串与字符串进行拼接
print("name %s age %d"% (tel,age))  #格式 %（数据类型，数据类型）

#数据精度%5.2f   %m.n（四舍五入）m.n都可以四舍五入
num1=11.2
print("五位数保留两位小数 %5.2f" % num1)  #百分号用来控制确定占位符

#使用format快速格式化,缺点不能进行精度控制，括号里面所有类型都转化为字符串f"{}"
name = 'wadw'
address="wuhan"
print(f"我是{name},地址{address}")

#表达式格式化f"{}"
print(f"2X4乘法等于 {2*4}")