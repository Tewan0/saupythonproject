var2 = (10, 20, 'Hello', True, (111, 'Wow') , 'มานะ')

# var2[2] = 'Hi' error
# การเปลี่ยนแปลงค่า เพิ่ม ลบ ข้อมูลใน Tuple
# list(), tuple()
varTemp = list(var2)
varTemp[2] = 'Hi'
var2 = tuple(varTemp)
print(var2)