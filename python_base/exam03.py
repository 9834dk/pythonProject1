str1="itheima itcast boxuegu"
print(str1.count("it"))
str2=str1.replace(" ","|")
print(str2)
list=str2.split("|")
print(f"分割后的字符串{list}，类型是{type(list)}")

my_list=['黑马程序员','传智博客','黑马程序员','传智博客','itheima','itcast','itheima','itcast','best']
null_set=set()
for item in my_list:
        null_set.add(item)
print(f'{null_set},{type(null_set)}')

employee_dict={"王力宏":{"部门":"科技部","工资":3000,"级别":1},
               "周杰伦":{"部门":"市场部","工资":5000,"级别":2},
               "林俊杰":{"部门":"市场部","工资":7000,"级别":3},
               "张学友":{"部门":"科技部","工资":4000,"级别":1},
               "刘德华":{"部门":"市场部","工资":6000,"级别":2},}
keys=employee_dict.keys()
for key in keys:
    if employee_dict[key]["级别"]==1:
        employee_dict[key]["级别"]=2
        employee_dict[key]["工资"]+=1000
print(employee_dict)
#容器转换 list（容器）tuple(容器) set（容器）字符串会分成子符存储，字典会抛弃value存储key，不能统统转字典其余的都可以互相转换
#容器排序 sorted(容器，逆序（reverse=True）)，正序的不用写第二个参数
