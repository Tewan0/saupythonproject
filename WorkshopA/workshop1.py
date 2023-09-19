def inputProductDetails( ) :
    namePrice = input('ชื่อสินค้า : ')
    productPrice = float( input('ราคาสินค้า : ') )
    return namePrice, productPrice

def calPrice( ) :
    sellingPrice = productPrice + ( productPrice * 10 / 100 )
    return sellingPrice
def showPrice( namePrice, sellingPrice ) :
    print(f'ชื่อสินค้า {namePrice} ราคาขายสินค้า {sellingPrice:.2f} บาท')

namePrice, productPrice = inputProductDetails( )

sellingPrice = calPrice( )

showPrice( namePrice, sellingPrice )
