def info( ) :
    input('จังหวัด : ')
    
def infoPH( ) :
    phValue = float( input('ค่า PH : ') )
    return phValue

def check( phValue ) :
    if phValue < 7 :
        print(f'Result is Alkali')
    
    elif phValue >= 7 and phValue <= 8 :
        print(f'Result is Normal')

    elif phValue > 8 :
        print(f'Result is Acid')

info( )
phValue = infoPH( )
check( phValue )
