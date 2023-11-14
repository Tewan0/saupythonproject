# อ่านข้อมูลจากไฟล์
f_dti = open('myfile01.txt', 'r', encoding='utf-8')

try :
    data = f_dti.readline() # อ่านทีละบรรทัด
    print(data, end='')
    data = f_dti.readline()
    print(data, end='')
    data = f_dti.readline()
    print(data)
except Exception :
    print("ติดต่อ Admin 02555555...")
finally :
    f_dti.close()    
    data = f_dti.readline() # อ่านทีละบรรทัด
    print(data)