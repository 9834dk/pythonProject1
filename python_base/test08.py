#*表示位置不定长，arg接收多个参数作为元组存入函数中
def user_info1(*args):
    print(args)
    print(type(args))  #元组形式
user_info1(1,2,3,4,5)

#**键值对存储形式关键字不定长，传入参数必须是字典形式一个键对应一个值
def user_info2(**kwargs):
    print(kwargs)
    print(type(kwargs))
user_info2(name="Tom",age=20,gender="male")

# 函数作为传入参数
def compute(x,y):
    return x+y
#传入计算逻辑，而不是数据
def user_info3(compute):
    result=compute(1,4)
    print(type(compute))
    print(result)
user_info3(compute)

#匿名函数lambda
def user_info4(computer):
    result=computer(1,7)
    print(result)
user_info4(lambda x,y:x+y) #只能用一次不能重复使用 lambda 传入参数：一行函数体

#文件的操作方式
#open(name,mode,encoding) 文件路径名称，r,w,s模式，编码方式
f=open("test.txt","w",encoding="utf-8")
f.read() #读取文中内容 传入参数是读取长度，不传入参数就是读取全部内容
#readlines()读取文件所有行返回到一个列表中
# readline()读取一行的内容
lines=f.readlines() #读取文件时候会续接前面读取的内容
#for循环读取文件,读取每一行
for line in f:
    print(line)
#关闭文件，使用open函数后必须使用close()函数
f.close()
#使用with open后，文件执行操作后会自动关闭
with open("E:\\test.txt","w",encoding="utf-8") as f:
    f.read()
