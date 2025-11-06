import csv
import random
from datetime import datetime, timedelta
import os


# 生成随机数据
def generate_employee_data(num_records=20):
    first_names = ['张', '李', '王', '刘', '陈', '杨', '赵', '黄', '周', '吴']
    last_names = ['明', '华', '强', '伟', '芳', '娜', '磊', '静', '军', '杰']
    departments = ['技术部', '销售部', '市场部', '人事部', '财务部', '研发部', '客服部', '运营部']
    positions = ['经理', '工程师', '专员', '主管', '助理', '分析师', '顾问']

    employees = []

    for i in range(num_records):
        emp_id = f"EMP{i + 1:03d}"
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        full_name = first_name + last_name
        department = random.choice(departments)
        position = random.choice(positions)
        salary = random.randint(5000, 20000)

        # 生成随机入职日期（过去1-5年内）
        start_date = datetime.now() - timedelta(days=random.randint(365, 1825))
        hire_date = start_date.strftime("%Y-%m-%d")

        email = f"{first_name}{last_name}{i + 1}@company.com"
        phone = f"1{random.randint(30, 89)}{random.randint(1000, 9999)}{random.randint(1000, 9999)}"

        employees.append({
            '员工ID': emp_id,
            '姓名': full_name,
            '部门': department,
            '职位': position,
            '薪资': salary,
            '入职日期': hire_date,
            '邮箱': email,
            '电话': phone
        })

    return employees


# 生成数据
employee_data = generate_employee_data(20)

# 写入CSV文件
with open('../jupyter_Demo/employees.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['员工ID', '姓名', '部门', '职位', '薪资', '入职日期', '邮箱', '电话']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for employee in employee_data:
        writer.writerow(employee)

print("employees.csv 文件已生成成功！")
print("\n生成的数据预览：")
print("-" * 80)
print(f"{'员工ID':<10} {'姓名':<8} {'部门':<8} {'职位':<8} {'薪资':<8} {'入职日期':<12} {'邮箱':<25} {'电话':<15}")
print("-" * 80)
for emp in employee_data[:5]:  # 只显示前5条作为预览
    print(
        f"{emp['员工ID']:<10} {emp['姓名']:<8} {emp['部门']:<8} {emp['职位']:<8} {emp['薪资']:<8} {emp['入职日期']:<12} {emp['邮箱']:<25} {emp['电话']:<15}")
print("... (还有15条记录)")
print(f"文件保存在：{os.getcwd()}")