#คำนวณเงินที่จะแชร์กัน ป้อนเงิน ป้อนคน แล้วคำนวณและแสดงเงินที่จะแชร์กันทางหน้าจอ
#โดยให้เขียนเป็นฟังก์ชัน ขอ 2 ฟังก์ชัน

#cast/conversion

#รับค่าข้อมูล
def input_money_person( ) :
    money = float( input('ป้อนเงิน : '))
    person = int( input('ป้อนคน : '))
    return money, person

#คำนวณ แล้วแสดงผล
def cal_and_show_moneyshare(money, person ) :
    forMoney = format(float(money),'.2f')
    forAvg = round(money/person)
    #เงิน ขอทศนิยม 2 ตำแหน่ง แชร์กันขอเป็นเลขจำนวนเต็มปัดขึ้น
    print(f'จำนวนเงิน {forMoney} บาท คน {person} คน แชร์กันคนละ {forAvg} บาท') #ใช้ f-string
    print('จำนวนเงิน', forMoney, 'บาท คน', person, 'คน แชร์กันคนละ', forAvg, 'บาท' ) #ใช้ ,
    print('จำนวนเงิน '+ forMoney +' บาท คน '+ str(person) +' คน แชร์กันคนละ '+ str(forAvg) +' บาท') #ใช้ +
    print('จำนวนเงิน {} บาท คน {} คน แชร์กันคนละ {} บาท'.format(forMoney,person,forAvg) ) #ใช้เมธอต format
    print('จำนวนเงิน %s บาท คน %s คน แชร์กันคนละ %s บาท' % (forMoney,person,forAvg) ) #ใช้ %


money, person = input_money_person( )

cal_and_show_moneyshare( money, person )



