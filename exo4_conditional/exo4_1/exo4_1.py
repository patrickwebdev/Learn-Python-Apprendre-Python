#Made with LOVE by Patrick Saint-Louis @2023
#Identify negative, null or positive input digit or number
print ('Identifier of negative, null or positive input digit or number \n')
print ('Data Collection \n')

#Inputs
#Declare variables and assign values
user_number = int(input('Digit or Number: \n')) 

#Calculate
#Identify digit or number
if (user_number>-10 and user_number<10):
    digitNumber='digit'
else:
    digitNumber='number'

#Identify positive, negative, or null
if (user_number>0):
    result="positif"
elif (user_number==0):
    result="null"
else:
    result="negative"

#Display outputs 
print ('\nIdentifier \n')
print ('You entered ', user_number, ' \n')
print (user_number, ' is a ', result, digitNumber, '')
