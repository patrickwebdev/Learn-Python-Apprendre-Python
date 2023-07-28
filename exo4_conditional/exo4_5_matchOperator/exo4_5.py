#Made with LOVE by Patrick Saint-Louis @2023
#Identify the range of a weekday 
print ('Identifier of weekday range. 1 is Monday and 7 is Sunday')
print ('Data Collection \n')

#Inputs
#Declare variables and assign values
userInput = str(input('Weekday name: \n'))

#Calculate
match userInput:
    case 'Monday' | 'monday' :    #First Uppercase OR all Lowercase
        range = 'the first'
    case 'Tuesday' | 'tuesday' :
        range = 'the second'
    case 'Wednesday' | 'wednesday' :
        range = 'the third'
    case 'Thursday' | 'thursday' :
        range = 'the fourth'
    case 'Friday' | 'friday' :
        range = 'the fifth'
    case 'Saturday' | 'saturday' :
        range = 'the sixth'
    case 'Sunday' | 'sunday' :
        range = 'the seventh'
    case _:
        range = 'NOT a'
    
#Display outputs
print ('\nIdentifier')
print('You entered',userInput)
print(userInput,'is',range,'day of the week. \n')



