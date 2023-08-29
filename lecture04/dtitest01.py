width = float( input('ป้อนความกว้าง : ') )
long = float( input('ป้อนความยาว : ') )
high = float( input('ป้อนความสูง : ') )

print('----------------------------')

total_area = ( (width * long)*2 ) + ( (width * high)*2 ) + ( (high * long)*2 )
gallon_amount = round( total_area/5 )

print( f"กล่องนี้กว้าง {width} cm ยาว {long} cm สูง {high} cm ต้องใช้สี {gallon_amount} gallon " )
print("กล่องนี้กว้าง", width,"cm ยาว", long, "cm สูง", high, "cm ต้องใช้สี", gallon_amount, "gallon" )
print("กล่องนี้กว้าง " + str(width) + " cm ยาว " + str(long) + " cm สูง " + str(high) + " cm ต้องใช้สี " + str(gallon_amount) + " gallon")