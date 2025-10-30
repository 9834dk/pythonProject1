#序列的操作，列表，元组，字符串都是有序的序列
#切片操作，不会影响序列本身而是通过返回值来达到目的
list02=[0,1,2,3,4,5,6,7,8,9]
result1=list02[3:6]   #从下标3开始到6之前不包含6，步长默认为1
#从右边9到3之前不包括3，步长为1反向一定要全都是复数
result2=list02[-1:-7:-1]
print(result1)
print(result2)
str2="万过薪月,员序程马黑来,nohtyp学"
list2=str2.split(",")
list3=list2[1]
list4=list3.replace("来"," ")
list5=list4[::-1]
print(list5.strip())
#集合的操作
my_set={'dwdw',12,'ccc'}
#添加新元素
my_set.add('yu')
#移除元素
my_set.remove(12)
print(my_set)
#随机取出一个元素
ele=my_set.pop()
print(f'取出的元素{ele}')
print(f'剩下的元素{my_set}')
#清空集合   my_set.clear()
#消除两个集合的差集
set1={1,2,3}
set2={2,3,4}
#set1.difference_update(set2)
print(set1)
#合并集合
set3=set1.union(set2)
print(set3)
#集合遍历,不支持下标索引不能使用while循环，只能用for

#定义字典不允许重复
my_dict={"周杰":99,"dwa":98,"aa":90}
print(type(my_dict))
#使用key获取value,不能用value来获取key
print(my_dict["周杰"])  #类似于序列的下标
#字典的嵌套，key不为字典其余都可以，value都可以
name_grade={"王力宏":{"语文":77,"数学":66,"英语":33},
            "周杰伦":{"语文":88,"数学":86,"英语":55},
            "林俊杰":{"语文":99,"数学":96,"英语":93}}
print(name_grade["王力宏"]["数学"])
#字典常用功能：新增和更新键值对（key的值存在是更新，不存在就是新增）
my_dict["周鑫"]=78
print(my_dict)
#删除元素，得到返回值
ele=my_dict.pop("周鑫")
print(f'{ele},{my_dict}')
#字典的遍历：第一步获取所有的key，第二步进行循环
keys=my_dict.keys()
for key in keys:
    print(f'字典的key是：{key},字典的value：{my_dict[key]}')
#统计字典内的元素数量:键值对数量
print(len(my_dict))
