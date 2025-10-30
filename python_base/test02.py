#input输入
name=input("please input name") #input带有提示输入信息
print(f"姓名是{name},数据类型：{type(name)}")
#input输入的类型都是字符串，如果需要什么类型，进行类型转换即可以下两种同样作用
age=int(input("please input age"))
print(f"年龄：{age}，数据类型：{type(age)}")
int(age)
print(f"年龄：{age}")

#bool类型 == != >= <= > < 六种比较运算符返回值为bool类型
#只有两种返回值类型True False
num1=1
num2=2
print(f"你大于我{num1>num2}")

#判断语句if 表达式：
#    (四个空格)条件成立执行,,,
#       else：
#    (四个空格)条件不成立执行,,,
#    多项判断if 条件一 elif条件二 else都不满足
num3=0
if num1>num2:
    print("1大于2")
    num3+=1
else:
    print("1小于2")
print(num3)
#判断条件嵌套
if num3>num1:
    if num3>num2:
        print("yes")
    else:
        print("no")
else:
    print("no")