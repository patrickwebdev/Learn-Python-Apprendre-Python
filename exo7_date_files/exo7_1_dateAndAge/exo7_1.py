#Made with LOVE by Patrick Saint-Louis @2023

import re
from datetime import date

try_again="Y"

while (try_again=="Y"):
    #Calculate product table using a loop and a counter variable
    print ('Calculator of age using the birth date')
    print ('Data Collection \n')

    #Create the messages to display
    messages = {
        'currentDate':'Today is: ',
        'birthDate':'You were born on: ',
        'age':'You are: ',
        'old':'old',
        'errType':"Error! You didn't enter only numbers for your birth date!",
        'errInvalid':"Error! You didn't enter a valid date for your birth date!",
        'errQty':"Error! You didn't enter a value for the day, month and year for your birth date!"
        }

    #Inputs
    #Declare variables and assign values
    user_data = str(input('Birth Date with a hyphen between Day, Month, and Year(DD-MM-YYYY): \n'))
    #Create an array with the input data
    userEnteredDateArray = user_data.split('-')
    nbrOfEnteredDateItems = len(userEnteredDateArray)

    #Validate number of data entered
    if (nbrOfEnteredDateItems != 3):
        print(messages['errQty'])

    else:
        #Validate data content using regex
        incorrectDateContent = 0
        
        for i in range(0, 3):
            isDateItemsOnly0to9 = not re.match('[0-9-]+$', userEnteredDateArray[i])
            if (isDateItemsOnly0to9):  
                incorrectDateContent = incorrectDateContent + 1
    
        if (incorrectDateContent > 0):
            print(messages['errType'])
        
        else:
            #Calculate current year to validate birth date year       
            nowDate = date.today()
            nowDateArray = str(date.today())
            nowDateItems = nowDateArray.split('-')
            nowDateYear=int(nowDateItems[0])
            nowDateMonth=int(nowDateItems[1])
            nowDateDay=int(nowDateItems[2])

            if (int(userEnteredDateArray[0])<1 or int(userEnteredDateArray[0])>31):
                print(messages['errInvalid'])
            elif (int(userEnteredDateArray[1])<1 or int(userEnteredDateArray[1])>12):
                print(messages['errInvalid'])
            elif (int(userEnteredDateArray[0])>nowDateDay and int(userEnteredDateArray[1])==nowDateMonth and int(userEnteredDateArray[2])==nowDateYear):
                print(messages['errInvalid'])
            elif (int(userEnteredDateArray[2])>nowDateYear):
                print(messages['errInvalid'])
            
            else:
                #Save birth date in correct format
                birthdate = date(int(userEnteredDateArray[2]), int(userEnteredDateArray[1]), int(userEnteredDateArray[0]))

                #Calculate age
                age = nowDate - birthdate
                ageInDays=age.days;
                ageInYears = int(ageInDays / 365);
                ageInMonths = int((ageInDays - (ageInYears * 365)) / 30);
            
                #Display outputs
                print ('\n')
                print (messages['currentDate'], nowDateItems[2], '-' , nowDateItems[1], '-' , nowDateItems[0], '\n')
                print (messages['currentDate'], nowDate.strftime("%A %B %d"), '\n')
                print (messages['birthDate'], userEnteredDateArray[0], '-' , userEnteredDateArray[1], '-' , userEnteredDateArray[2], '\n')
                print (messages['birthDate'], birthdate.strftime("%A %B %d"), '\n')
                print (messages['age'], ageInDays, 'days', messages['old'], '\n')
                print (messages['age'], 'approximately', ageInYears, 'years', ageInMonths, 'months', messages['old'], '\n')
            

    #Inputs
    #Declare variables and assign values
    try_again = str(input('\nTry again? Y/N : \n'))

    if (try_again!="Y"):
        print("You chose to leave. See you soon!")
        exit()
    
