# โปรแกรมตรวจสอบนํ้าหนักรถบรรทุกของด่านชั่งนํ้าหนักว่ารถบรรทุกนั้นมีนํ้าหนักรถผ่านเกณฑ์หรือไม่ 
# หากนํ้าหนักเกิน 1000 kg ให้แสดงข้อความว่า "รถนํ้าหนักไม่ผ่านเกณฑ์" 
# แต่หากนํ้าหนักตั้งแต่ 1000 kg ลงมาให้แสดงข้อความว่า "รถนํ้าหนักผ่านเกณฑ์" โดยให้ป้อนทะเบียนรถบรรทุกและนํ้าหนักรถบรรทุกทางแป้นพิมพ์

# วิเคราะห์
# มองหา feature การทำงานว่ามีอะไรบ้าง เพื่อจะไปสร้างเป็น function
# รับค่าทะเบียนรถ นํ้าหนักรถ -> inputCarDetial
# ตรวจสอบนํ้าหนักรถ และแสดงผล -> checkCarAndShowWeight

def inputCarDetail() :
    carNo = input('ป้อนทะเบียนรถ : ')
    carWeight = float( input('ป้อนนํ้าหนักรถ : ') )
    return carNo, carWeight

def checkCarAndShowWeight(carNo, carWeight) :
    if carWeight > 1000 :
        print(f'{carNo} นํ้าหนักไม่ผ่านเกณฑ์')
    else :
        print(f'{carNo} นํ้าหนักผ่านเกณฑ์')

print('-----------------------------')
print('------- Truck Checker -------')
print('-----------------------------')
carNo, carWeight = inputCarDetail()
print('-----------------------------')
checkCarAndShowWeight(carNo, carWeight)
print('-----------------------------')
