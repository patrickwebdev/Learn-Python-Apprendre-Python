#Price Calculator (Subtotal, taxes TPS and TVQ, and Total)
print ('Calculator of Subtotal, taxes TPS and TVQ, and Total \n')
print ('Data Collection \n')

#Load the file where the constants are declared and assigned
import constant

#Inputs
#Declare variables and assign values
itemName = str(input('Item Name: \n'))
itemUnitPrice = float(input('Item Unit Price: \n')) 
itemQuantity = float(input('Item Quantity \n'))  

#Calculate
subtotal= itemQuantity * itemUnitPrice
tps= subtotal * constant.TPSRATE
tvq= subtotal * constant.TVQRATE
total= subtotal + tps + tvq

#Keep only 2 digits as decimal values
itemUnitPrice=round(itemUnitPrice, 2)
subtotal=round(subtotal, 2) 
tps=round(tps, 2) 
tvq=round(tvq, 2) 
total=round(total, 2) 

#Display outputs 
print ('\nCalculator \n')
print ('Item Name       : ', itemName, ' \n')
print ('Item Unit Price : ', itemUnitPrice, ' $ca \n')
print ('Quantity bought : ', itemQuantity, ' $ca \n')
print ('Subtotal        : ', subtotal, ' $ca \n')
print ('TVQ             : ', tvq, ' $ca \n')
print ('TPS             : ', tps, ' $ca \n')
print ('Total           : ', total, ' $ca \n')

    
