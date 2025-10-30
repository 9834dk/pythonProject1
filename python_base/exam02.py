#ATM取款机模拟
money=500000
def balance():
        print(f"你好，{name}，你的账户余额还有{money}")

def deposit(m):
    global name,money
    money+=m
    print(f"存款成功，当前余额为{money}")
def draw_money(m):
    global name, money
    if name=={'zs','ls'}:
        if money>0:
            money=money-m
            print(f"取款成功，当前余额为{money}")
        else:
            print("no money")
    else:
        return
def menu():

    while True:
        print("-----------------选择业务----------------\n"
              "-----------------1-查询余额--------------\n"
              "-----------------2-存款-----------------\n"
              "-----------------3-取款-----------------\n"
              "-----------------0-退出-----------------\n")
        num = int(input())
        if num==1:
            balance()
            continue
        elif num==2:
            money=int(input("请输入存款数量"))
            deposit(money)
            continue
        elif num==3:
            money = int(input("请输入取款数量"))
            draw_money(money)
            continue
        else:
            print("结束")
            break
name=input("---------------请输入客户姓名------------\n")
menu()