# เขียนข้อมูลลงไฟล์
f_dti = open('myfile01.txt', 'w', encoding='utf-8') # เปิดไฟล์เพื่อเขียนข้อมูลลงไฟล์
f_dti.write('Wow...')
f_dti.write('Woo...\n')
f_dti.write('ลาก่อนทุกคน...\n')

f_dti.close()

print("บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว....")