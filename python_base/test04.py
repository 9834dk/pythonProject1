#continue和break的区别

for i in range(1,3):
    for j in range(1,i+1):
        print('第一')
        continue   #执行完第一就直接进行下一次循环跳过第二
        print('第二')
    print('第三')

for i in range(1,3):
    for j in range(1,i+1):
        print("first")
        break      #直接结束内层循环，所有continue和break都是匹配单独循环的
        print("second")
    print("third")

def len1(n):
    '''
    函数说明:（string n）
    多行注释
    '''
    count=0
    for i in n:
        count+=1
    print(f"字符串长度为{count}")
def more_return():
    return 1,"hello",True


x,y,z=more_return()
print(x,y,z)
str1="dwdwadwdws"
len1(str1)
s=len1(str1)
print(type(s))  #None无返回值

num=100
def test1():
    global num    #全局变量
    num=200
test1()
print(num)


