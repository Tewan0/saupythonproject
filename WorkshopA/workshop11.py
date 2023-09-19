def userInfo( ) :
    name = input('ชื่อผู้ใช้โทรศัพท์ : ')
    phoneCall = str( input('เบอร์โทรศัพท์ : ') )
    return name, phoneCall

def minutesSpent( ) :
    minute = int( input('จำนวนนาทีที่ใช้โทรศัพท์ : ') )
    return minute

def calSpent( minute ) :
    if minute >= 1 and minute <= 15 :
        serviceFee = minute * 5
        print(f'ค่าบริการเท่ากับ {serviceFee} บาท')
    elif minute >= 16 and minute < 31 :
        serviceFee = minute * 3
        print(f'ค่าบริการเท่ากับ {serviceFee} บาท')
    else :
        serviceFee = minute * 1.50
        print(f'ค่าบริการเท่ากับ {serviceFee} บาท')

name, phoneCall = userInfo( )
minute = minutesSpent( )
calSpent( minute )
