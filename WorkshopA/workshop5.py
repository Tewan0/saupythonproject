def employeeInformation( ) :
    employeeID = input('รหัสพนักงาน : ')
    employeeName = input('ชื่อพนักงาน : ')
    salary = float(input('เงินเดือน : ') )
    return employeeID, employeeName, salary

def calNetSalary( salary ) :
    netSalary = salary - ((salary * 7) / 100) - 500
    return netSalary

def showNetSalary( employeeID, employeeName, netSalary ) :
    print(f'รหัสพนักงาน {str(employeeID)} ชื่อพนักงาน {employeeName} เงินเดือนสุทธิ {float(netSalary):.2f} บาท')

employeeID, employeeName, salary = employeeInformation( )
netSalary = calNetSalary( salary )
showNetSalary( employeeID, employeeName, netSalary )
