#Made with LOVE by Patrick Saint-Louis @2023

#Price Calculator (Subtotal, taxes TPS and TVQ, and Total) including input validation
print ('Calculator of Subtotal, taxes TPS and TVQ, and Total \n')
print ('Data Collection \n')

#Load the file where the constants are declared and assigned
import constant

#User defined functions for inputs and their validation
def getInputs():
    #Declare variables and initialize
    count = 0
    itemName = itemUnitPrice = itemQuantity = ""
    #Get inputs, validate, and assign values
    while (itemName=="" or itemUnitPrice=="" or itemQuantity==""):
        itemName = str(input('Item Name: \n'))
        itemUnitPrice = str(input('Item Unit Price: \n')) 
        itemQuantity = str(input('Item Quantity \n'))
        count=count+1
        if (count>0 and (itemName=="" or itemUnitPrice=="" or itemQuantity=="")):
            print ('Empty data input found. Try again! \n')
    #Convert to float
    itemUnitPrice = float(itemUnitPrice)
    itemQuantity = float(itemQuantity)
    inputs = {'name': itemName, 'uPrice': itemUnitPrice, 'quantity': itemQuantity}
    return inputs

#User defined functions for calculations
def setSubtotal (quantity,unit_price):
    subtotal= quantity * unit_price
    return (round(subtotal, 2))

def setTps (price):
    tps= price * constant.TPSRATE
    return (round(tps, 2))

def setTvq (price):
    tvq= price * constant.TVQRATE
    return (round(tvq, 2))

def setTotal (quantity,unit_price):
    total= setSubtotal(quantity,unit_price) + setTps(setSubtotal(quantity,unit_price)) + setTvq(setSubtotal(quantity,unit_price))
    return (round(total, 2))

#User defined functions for outputs (main function)
def getOutputs():
    user_data=getInputs()
    print ('\nCalculator \n')
    print ('Item Name       : ', user_data['name'], ' \n')
    print ('Item Unit Price : ', round(user_data['uPrice'], 2), ' $ca \n')
    print ('Quantity bought : ', user_data['quantity'], ' $ca \n')
    print ('Subtotal        : ', setSubtotal(user_data['quantity'],user_data['uPrice']), ' $ca \n')
    print ('TVQ             : ', setTvq(setSubtotal(user_data['quantity'],user_data['uPrice'])), ' $ca \n')
    print ('TPS             : ', setTps(setSubtotal(user_data['quantity'],user_data['uPrice'])), ' $ca \n')
    print ('Total           : ', setTotal(user_data['quantity'],user_data['uPrice']), ' $ca \n')

#Call the main function
getOutputs()
