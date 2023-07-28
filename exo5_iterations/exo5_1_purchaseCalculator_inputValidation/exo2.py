#Price Calculator (Subtotal, taxes TPS and TVQ, and Total) including input validation
print ('Calculator of Subtotal, taxes TPS and TVQ, and Total \n')
print ('Data Collection \n')

#Load the file where the constants are declared and assigned
import constant

#Declare variables and initialize
count = 0
itemName = itemUnitPrice = itemQuantity = ""

#Inputs, validate, and assign values
while (itemName=="" or itemUnitPrice=="" or itemQuantity==""):
    itemName = str(input('Item Name: \n'))
    itemUnitPrice = str(input('Item Unit Price: \n')) 
    itemQuantity = str(input('Item Quantity \n'))
    count=count+1
    if (count>0 and (itemName=="" or itemUnitPrice=="" or itemQuantity=="")):
        print ('Empty data input found. Try again! \n')
    
#Calculate
subtotal= float(itemQuantity) * float(itemUnitPrice)
tps= subtotal * constant.TPSRATE
tvq= subtotal * constant.TVQRATE
total= subtotal + tps + tvq

#Keep only 2 digits as decimal values
itemUnitPrice=round(float(itemUnitPrice), 2)
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

    
