def classYear( ) :
    classY = int( input('ชั้นปี : ') )
    return classY

def welcomeMessage( classY ) :
    if classY == 1 :
        print(f'Welcome Freshman')
    elif classY == 2 :
        print(f'Welcome Sophomore')
    elif classY == 3 :
        print(f'Welcome Junior')
    elif classY == 4 :
        print(f'Welcome Senior')

classY = classYear( )
welcomeMessage( classY )
