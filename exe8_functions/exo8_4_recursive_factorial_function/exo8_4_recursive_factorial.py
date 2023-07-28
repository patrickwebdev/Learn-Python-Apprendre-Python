#Made with LOVE by Patrick Saint-Louis @2023

import re
try_again="Y"

while (try_again=="Y"):
    
    #Calculate and display factorial using a recursive function
    print ('Calculate and display factorial using a recursive function')
    print ('Data Collection \n')

    #User-defined function to collect and save the data entered
    def getUserInput() :
        userInput = int(input('Positive Digit or Number (greater than or equal to 0) : \n'))
        return userInput

    #Recursive user-defined function to calculate factorial
    def getFactorial(a):
        if (a == 1 or a == 0):
            return 1
        else:
            return (a * getFactorial(a - 1))

    #User-defined function to save the messages to display
    def allMessages():
        messages = {
            'err_sign':"Error! It is not a positive digit or number (greater than or equal to 0) as required.",
            'result':"It's Factorial is equal to: ",
            'intro':'You entered : '
        }
        return messages

    #User-defined function to validate whether user input is positive or not 
    def validateIsPositiveOrNegative (inputData):    
        if (inputData >= 0):
            return True
        else:
            return False

    #Main user-defined function that calls the other functions to implement the context of this program
    #User-defined function to display outputs
    def displayOutputs():
        #Messages to display
        messages = allMessages()
        #Get input
        userData = getUserInput()
        #Display input
        print (messages['intro'], userData)
        #Validate if input is a positive digit or number
        if (validateIsPositiveOrNegative(userData)== False):
            print (messages['err_sign'])
        else:
            print (messages['result'], getFactorial(userData))

    #Call the function
    displayOutputs()

    #Inputs
    #Declare variables and assign values
    try_again = str(input('\nTry again? Y/N : \n'))

    if (try_again!="Y"):
        print("You chose to leave. See you soon!")
        exit()
