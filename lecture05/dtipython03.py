#Function 3 : no parameter/have returns
def dti1( ) :
    print(1)
    print(2)
    a, b, c = dti2( )
    print(f'สวัสดี {b} อายุ {a} และ {c}')
    return 999


def dti2( ) :
    print(3)
    return 10 + 20, 'สมชาย', True


print( dti1( ) )
x = dti1( )
y = dti1( ) + 1 + 2
print('-----------------')




