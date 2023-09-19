def info( ) :
    nameLeader = input('ชื่อหัวหน้ากรุ๊ปทัวร์ : ')
    leaderContactNumber = str( input('เบอร์ติดต่อของหัวหน้ากรุ๊ปทัวร์ : ') )
    return nameLeader, leaderContactNumber

def numberOfPeople( ) :
    amount = int(input('จำนวนคนที่จะไปทัวร์ : '))
    return amount

def calNumberOfPeople( amount ) :
    if amount >= 1 and amount <=2 :
        packagePrice = amount * 300
        print(f'ชื่อหัวหน้ากรุ๊ปทัวร์ {nameLeader} เบอร์ติดต่อ {leaderContactNumber} จำนวนคนที่จะไปทัวร์ {amount} คน แพ็กเกจคือ {packagePrice} บาท ')
   
    elif amount >= 3 and amount <= 5 :
        packagePrice = amount * 250
        print(f'ชื่อหัวหน้ากรุ๊ปทัวร์ {nameLeader} เบอร์ติดต่อ {leaderContactNumber} จำนวนคนที่จะไปทัวร์ {amount} คน แพ็กเกจคือ {packagePrice} บาท ')

    elif amount >= 6 and amount <= 10 :
        packagePrice = amount * 210
        print(f'ชื่อหัวหน้ากรุ๊ปทัวร์ {nameLeader} เบอร์ติดต่อ {leaderContactNumber} จำนวนคนที่จะไปทัวร์ {amount} คน แพ็กเกจคือ {packagePrice} บาท ')

    elif amount >= 11 :
        packagePrice = amount * 150
        print(f'ชื่อหัวหน้ากรุ๊ปทัวร์ {nameLeader} เบอร์ติดต่อ {leaderContactNumber} จำนวนคนที่จะไปทัวร์ {amount} คน แพ็กเกจคือ {packagePrice} บาท ')

nameLeader, leaderContactNumber = info ( )
amount = numberOfPeople( )
calNumberOfPeople(amount)
