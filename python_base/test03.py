# while循环打印九九乘法表
i=1

while i<=9:
    j = 1
    while j<=i:
        print("%d * %d = %d\t"%(j,i,i*j),end=" ")
        j=j+1
    print()
    i+=1

# for循环语法   for 临时变量 in 数据集序列（数字范围，字符串）
#                   待处理代码
# 定义字符串变量
name = "ithheima is a brand of itcast"
count=0
for i in name:   #i是for循环的临时变量，最好是将i定义以下后续成为全局变量
    if i=="a":
        count+=1
print(count)

# range(num1，num2，num3) num1:起步下标，默认是0 ,num2:结束下标(不可省略)，num3是步长，默认1
#九九乘法表
i=1
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} = {i*j}\t",end="")
        j+=1
    i+=1
    print("\n")
