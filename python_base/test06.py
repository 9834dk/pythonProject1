# #元组：不可以修改的列表
# from scipy.constants import value
#
# t1=('周杰六',11,['football','music'])
# i=0
# while i<len(t1):
#     print(f'元组里的元素：{t1[i]}')
#     i+=1
# for element in t1:
#     print(f'元组里的元素：{element}')
# #查询年龄所在的下标
# print(t1.index(11))
# #查询姓名
# print(t1[0])
# #删除学生爱好的football
# t1[2].pop(0)
# print(t1)
# #增加爱好：coding到爱好list内
# t1[2].insert(1,'coding')
# print(t1)
#字符串
str1='wasdd fasd'
str2='12fef gty 21'
#字符串只读容器不能修改
print(str1[1])
#index方法可以获取元素的下标起步
value1=str1.index('as')
print(value1)
#replace方法替换字符串，不是修改原来的字符串
value2=str1.replace('as','123')
print(value2)
#split方法，按照指定的分隔符字符串，存入列表(list)对象中
my_list=str1.split(" ")
print(my_list)
#strip方法，规整字符串去除前后字符串不传参数取出首尾空格,按照字符去掉1和2不是顺序
ip=str2.strip('12')
print(ip)
#count方法，统计字符串出现的次数
print(str1.count('as'))
#len()统计字符串长度
print(len(str1))


