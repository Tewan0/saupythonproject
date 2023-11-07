# เขียนข้อมูลลงไฟล์
# เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์
f_dti = open('myfile03.txt', 'a', encoding='utf-8')

f_dti.write('CCCCCCC\n')
f_dti.write('BBBBBBB\n')


f_dti.close()

print("บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว....")