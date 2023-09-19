def enterNumbers( ) :
    number = int(input('ป้อนตัวเลขที่ต้องการทาย : ') )
    return number

def ifCorrect( number ) :
    if number == 25 :
        print(f'Correct, You are the winner')

def ifincorrect( number ) :
    if number != 25 :
        print(f'Not Correct !!!')

number = enterNumbers( )
ifCorrect( number )
ifincorrect( number )
