def value( ) :
   valueX = int(input('ค่า X : '))
   return valueX

def calvalue( valueX ) :
   calEquation = (2*(valueX**2)) + (2*valueX) + 1
   return calEquation
def showValue( ) :
   print(f'ได้สมการ {calEquation}')

valueX = value( )
calEquation = calvalue( valueX )
showValue( )
