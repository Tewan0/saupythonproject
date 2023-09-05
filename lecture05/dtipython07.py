#โปรแกรมคำนวณหาพื้นที่วงกลม เส้นรอบวงกลม และปริมาตรวงกลม จากรัศมีที่ป้อนโดยผู้ใช้ทางแป้นพิมพ์ และแสดงผลพื้นที่ เส้นรอบ และปริมาตรทางหน้าจอ

#ขอ 5 ฟังก์ชัน
import math
#inputRadius
def inputRadius() :
    # r = input('ป้อนรัศมี : ')
    # return r

    # return input('ป้อนรัศมี : ')

    return float( input('ป้อนรัศมี : '))

#calAreaCircle
def calAreaCircle( r ) :
    #area = math.pi * r ** 2
    #area = math.pi * r * r
    # area = math.pi * math.pow(r, 2)
    # return area
    return math.pi * math.pow(r, 2)

#calRoundCirle 2 * PI * r
def calRoundCirle( r ) :
    return 2*(math.pi * r)


#calCubeCirle 4 / 3 * PI * r * r * r
def calCubeCirle( r ) :
    return 4/3 * math.pi * (r**3)

#showResul ขอทั้งหมดทศนิยม 4 ตำแหน่ง
#พื้นที่วงกลมเป็น ?? เส้นรอบวงเป็น ?? ปริมาตรทรงกลมเป็น ?? 
def showResul( ) :
    r = inputRadius()
    area = calAreaCircle( r )
    round = calRoundCirle( r )
    cube = calCubeCirle( r )
    print(f'ป้อนรัศมี {"%.4f"%r} cm มีพื้นที่ {"%.4f"%area} cm เส้นรอบวง {"%.4f"%round} cm มีปริมาตร {"%.4f"%cube}' )
