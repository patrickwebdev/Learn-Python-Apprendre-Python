#Made with LOVE by Patrick Saint-Louis @2023
#Identify the range of a weekday 
print ('Identifier of weekday range. 1 is Monday and 7 is Sunday')
print ('Data Collection \n')

#Inputs
#Declare variables and assign values
userInput = str(input('Weekday name: \n'))

#Calculate
if (userInput=='Monday'):
    range = 'the first'
elif (userInput=='Tuesday'):
    range = 'the second'
elif (userInput=='Wednesday'):
    range = 'the third'
elif (userInput=='Thursday'):
    range = 'the fourth'
elif (userInput=='Thursday'):
    range = 'the fifth'
elif (userInput=='Friday'):
    range = 'the sixth'
elif (userInput=='Friday'):
    range = 'the seventh'
else:
    range = 'NOT a'
    
#Display outputs
print ('\nIdentifier')
print('You entered',userInput)
print(userInput,'is',range,'day of the week. \n')



