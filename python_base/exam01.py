# name="单位"
# stock_price=19.99
# stock_code=1213
# stock_price_daily=1.2 #增长系数
# growth_days=7
# print("经过%d天的增长后，股价达到%.2f"%(growth_days,stock_price*stock_price_daily**growth_days))
# print(f"公司{name}, 股票代码{stock_code}")
#
# import random
#
# a=random.randint(1,10)
# b=int(input("请输入数字："))
# if b==a:
#     print("猜对了")
# elif b>a:
#     print("猜大了")
# else:
#     print("猜小了")

#1~100累加求和
# i=1
# sum=0
# while i<=100:
#     sum+=i
#     i+=1
# print(sum)

# #发工资
# import random
# i=1
# salary = 10000
# people=20
# while i<=people:
#
#     score=random.randint(1,10)
#     if score<5:
#         print(f"员工{i},绩效分{score},低于5，不发工资，下一位。")
#     else:
#         salary=salary - 1000
#         print(f"向员工{i}发放工资1000，账户余额还剩余{salary}")
#     if salary == 0:
#         print("工资发完了下个月领取吧")
#         break
#     i=i+1



f=open("E:/test.txt","w",encoding="utf-8")
f.write("nice") #会将原有的文件内容覆盖掉
f=open("E:/test.txt","a",encoding="utf-8")
f.write("nice") #追加文件而不是覆盖文件

f=open("E:/test.txt","r",encoding="utf-8")
cunt=f.read()
count=cunt.count("w")
print(count)
print(cunt)
f.close()