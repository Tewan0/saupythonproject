def employeeInfo( ) :
    str( input('รหัสพนักงาน : ') )
    input('ชื่อพนักงาน : ')

def Sales( ) :
    employeeSales = float( input('ยอดขายของพนักงาน : ') )
    return employeeSales

def calCommission( employeeSales ) :
    if employeeSales <= 1000 :
        print(f'ไม่ได้ค่าคอมมิชชั่น')

    elif employeeSales >= 1001 and employeeSales <= 2000 :
        commissionMoney = employeeSales * 0.01
        print(f'ได้ค่าคอมมิชชั่น {commissionMoney} บาท')
    
    elif employeeSales >= 2001 and employeeSales <= 3000 :
        commissionMoney = employeeSales * 0.03
        print(f'ได้ค่าคอมมิชชั่น {commissionMoney} บาท')

    elif employeeSales >= 3001 :
        commissionMoney = employeeSales * 0.05
        print(f'ได้ค่าคอมมิชชั่น {commissionMoney} บาท')

employeeInfo( )
employeeSales = Sales( )
calCommission( employeeSales )

