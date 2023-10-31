class DtiTest01 :
    pass

class DtiTest02 :
    # data/attribute/property/field คือ ตัวแปรประเภทหนึ่ง
    infoA = ''
    infoB = 20

    # method คือ ฟังก์ชันประเภทหนึ่ง
    def showHi(self) :
        print('Hi....')

    def showInfoAandB(self) :
        print(self.infoA)
        print(self.infoB)

# สร้าง Object
objA = DtiTest02()
objB = DtiTest02()
sombat = DtiTest02()

objA.infoA = 'XXXX'
objB.infoB = 100

print(objA.infoB + objB.infoB)

sombat.showInfoAandB()