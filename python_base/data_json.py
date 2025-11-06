import json
import random
from datetime import datetime, timedelta


def generate_employee_json(num_records=10):
    first_names = ['张', '李', '王', '刘', '陈', '杨', '赵', '黄', '周', '吴']
    last_names = ['明', '华', '强', '伟', '芳', '娜', '磊', '静', '军', '杰']
    departments = ['技术部', '销售部', '市场部', '人事部', '财务部', '研发部', '客服部', '运营部']
    positions = ['经理', '工程师', '专员', '主管', '助理', '分析师', '顾问']
    cities = ['北京', '上海', '广州', '深圳', '杭州', '成都', '武汉', '西安']

    employees = []

    for i in range(num_records):
        emp_id = f"EMP{i + 1:03d}"
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        full_name = first_name + last_name

        # 生成随机年龄
        age = random.randint(22, 45)

        department = random.choice(departments)
        position = random.choice(positions)
        salary = random.randint(5000, 20000)

        # 生成随机入职日期
        start_date = datetime.now() - timedelta(days=random.randint(365, 1825))
        hire_date = start_date.strftime("%Y-%m-%d")

        email = f"{first_name}{last_name}{i + 1}@company.com"
        phone = f"1{random.randint(30, 89)}{random.randint(1000, 9999)}{random.randint(1000, 9999)}"

        # 随机生成地址
        city = random.choice(cities)
        address = f"{city}市{random.choice(['朝阳区', '浦东新区', '天河区', '南山区', '西湖区', '武侯区', '江汉区', '雁塔区'])}"

        employee = {
            'employee_id': emp_id,
            'personal_info': {
                'name': full_name,
                'age': age,
                'email': email,
                'phone': phone,
                'address': address
            },
            'work_info': {
                'department': department,
                'position': position,
                'salary': salary,
                'hire_date': hire_date,
                'employee_status': random.choice(['在职', '试用期'])
            },
            'skills': random.sample(['Python', 'Java', 'JavaScript', '项目管理', '沟通能力', '团队合作', '数据分析'], 3)
        }

        employees.append(employee)

    return employees


# 生成JSON数据
employee_json_data = generate_employee_json(10)

# 保存为JSON文件
with open('E:/data/pythonProject/jupyter_Demo/employees.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(employee_json_data, jsonfile, ensure_ascii=False, indent=2)

# 同时在控制台输出预览
print("employees.json 文件已生成成功！")
print("\n生成的JSON数据预览：")
print(json.dumps(employee_json_data[:2], ensure_ascii=False, indent=2))
print("... (还有8条记录)")
