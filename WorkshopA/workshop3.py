def inputProductDetails( ) :
    nameProduct = input('ชื่อสินค้า : ')
    productPrice = float(input('ราคาสินค้า : ') )
    return nameProduct, productPrice

def calTaxes( ) :
    taxesPrice = (productPrice * 7) / 100
    return taxesPrice

def showTaxes( ) :
    print(f'ชื่อสินค้า {nameProduct} ราคาสินค้า {float(productPrice):.2f} บาท ราคาภาษี {float(taxesPrice):.2f} บาท')

nameProduct, productPrice = inputProductDetails( )
taxesPrice = calTaxes( )
showTaxes( )
