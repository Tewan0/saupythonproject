emp_id = input("รหัสพนักงาน : ")
emp_name = input("ชื่อพนักงาน : ")
normal_salary = float( input("เงินเดือนปกติ : ") )

net_salary = normal_salary - (normal_salary * 7 / 100) - 500

print(f"รหัสพนักงาน {emp_id} ชื่อพนักงาน {emp_name} เงินเดือนสุทธิ {net_salary} บาท")