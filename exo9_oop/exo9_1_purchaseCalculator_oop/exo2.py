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

#Class for calculating price
class PriceCalculator:
    
    #Properties
    nam = quantity = unitprice = subtotal = tps = tvq = total = ""

    #Methods for initialization (constructor)
    def __init__(self, nam, prc, qty):
        self.name = nam
        self.unitprice = prc
        self.quantity = qty
        self.setSubtotal()
        self.setTps()
        self.setTvq()
        self.setTotal()

    #Methods for calculating data
    def setSubtotal (self):
        self.subtotal= self.quantity * self.unitprice

    def setTps (self):
        self.tps= self.subtotal * constant.TPSRATE

    def setTvq (self):
        self.tvq= self.subtotal * constant.TVQRATE

    def setTotal (self):
        self.total= self.subtotal + self.tps + self.tvq

    #Methods for getting collected and calculated data
    #Collected
    def getName (self):
        return self.name

    def getQuantity (self):
        return self.quantity

    def getPrice (self):
        return self.unitprice
    
    #Calculated
    def getSubtotal (self):
        return (round(self.subtotal, 2))

    def getTps (self):
        return (round(self.tps, 2))

    def getTvq (self):
        return (round(self.tvq, 2))

    def getTotal (self):
        return (round(self.total, 2))

        #Method for displaying outputs 
    def getOutputs(self):
        print ('\nCalculator \n')
        print ('Item Name       : ', self.getName(), ' \n')
        print ('Item Unit Price : ', self.getPrice(), ' $ca \n')
        print ('Quantity bought : ', self.getQuantity(), ' $ca \n')
        print ('Subtotal        : ', self.getSubtotal(), ' $ca \n')
        print ('TVQ             : ', self.getTps(), ' $ca \n')
        print ('TPS             : ', self.getTvq(), ' $ca \n')
        print ('Total           : ', self.getTotal(), ' $ca \n')

#Call the user defined function to collect data
user_data = getInputs()
#Instanciate an object of the class with the data collected to calculate prices
current_buyer = PriceCalculator(user_data['name'], user_data['uPrice'], user_data['quantity'])
#Invoke the method with the object created to display outputs
current_buyer.getOutputs()

