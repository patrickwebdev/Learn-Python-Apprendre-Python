#Made with LOVE by Patrick Saint-Louis @2023
#Identify the gap between 2 digits or numbers
print ('Identifier of gap between 2 digits or numbers \n')
print ('Data Collection \n')

#Inputs
#Declare variables and assign values
userData1 = int(input('1st Digit or Number: \n'))
userData2 = int(input('2nd Digit or Number: \n')) 

#Calculate
#Identify gap
if (userData1==userData2):
    gap = "null"
else:
    gap = abs(userData1 - userData2)

#Display outputs
print ('\nIdentifier \n')
print('You entered 2 numbers that are',userData1,'and', userData2,'. \n')
print('Consequently, the gap between them is',gap,'.')
