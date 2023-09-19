def nameInformation( ) :
    name = input('ชื่อผู้กู้ : ')
    return name

def loanAmount( ) :
    loan = float(input('จำนวนเงินกู้ : ') )
    return loan

def calInterestRate( name, loan ) :
    if loan > 1000 :
        x = (loan * 2.5) / 100
        print(f'ชื่อผู้กู้ {name} อัตราดอกเบี้ย {float(x):.2f} บาท')
    else :
        y = (loan * 5.5) / 100
        print(f'ชื่อผู้กู้ {name} อัตราดอกเบี้ย {float(y):.2f} บาท')

name = nameInformation( )
loan = loanAmount( )
calInterestRate( name, loan )
