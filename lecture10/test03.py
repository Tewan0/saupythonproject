# เขียนข้อมูลลงไฟล์
# เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์
f_dti = open('myfile02.txt', 'x', encoding='utf-8')
f_dti.write('SAU...')
f_dti.write('DTI...\n')
f_dti.write('ลาก่อนทุกคน...\n')

f_dti.close()

print("บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว....")