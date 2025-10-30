#列表容器
name_list=['zhangsan','lisi']
#嵌套列表
# double_list=[]
# print(name_list[-1])  #反向索引从右向左第一个是-1，每次减一
# print(name_list[1])   #正向索引从左向右第一个是0，每次加一
# print(name_list)      #可以直接取

# index=0
# while index<len(name_list):
#     a = name_list[index]
#     print(a)
#     index+=1
#
# for i in name_list:
#     print(i)
#
# #1.定义列表
# stu_list=[21,25,21,23,22,20]
# #追加31到列表尾部
# stu_list.append(31)
# print(stu_list)
# #追加新列表[29,33,30],到列表的尾部
# stu_list.extend([29,33,30])
# print(stu_list)
# #取出第一个元素（21）
# a=stu_list[0]
# print(f'第一个元素是{a}')
# #取出最后一个元素
# b=stu_list[-1]
# print(f'最后一个元素是{b}')
# #查找元素31的下标
# print(stu_list.index(31))

list01=[1,2,3,4,5,6,7,8,9,10]
list02=[]
i=0
while i<len(list01):
    if list01[i]%2==0:
        list02.append(list01[i])
    i+=1
print(f'通过while循环，从列表：{list01}中取出偶数，组成新列表：{list02}')
list02.clear()
for it in list01:
    if it%2==0:
        list02.append(it)
print(f'通过for循环，从列表：{list01}中取出偶数，组成新列表：{list02}')