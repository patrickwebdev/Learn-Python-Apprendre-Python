#Made with LOVE by Patrick Saint-Louis @2023

try_again="Y"

while (try_again=="Y"):
    #Calculate product table using a loop and a counter variable
    print ('Identifier of weekday by range or keyword using array and loop')
    print ('Data Collection \n')

    #Create numbered and associative arrays
    dayDigit=[
            'monday', 
            'tuesday', 
            'wednesday', 
            'thursday', 
            'friday', 
            'saturday', 
            'sunday'
            ]
    
    dayText={
            'mo':'monday', 
            'tu':'tuesday', 
            'we':'wednesday', 
            'th':'thursday', 
            'fr':'friday', 
            'sa':'saturday', 
            'su':'sunday'
            }

    #Inputs
    #Declare variables and assign values
    user_data = str(input('Digit (1-7) or Keyword (2 first letter of weekday): \n'))


    #Validate, calculate and display outputs
    print("You entered",user_data,'.')
    
    if (user_data=='1' or user_data=='2' or user_data=='3' or user_data=='4' or user_data=='5' or user_data=='6' or user_data=='7'):
        print ("It corresponds to",dayDigit[int(user_data)-1],'.')
        
    else:
        correct_keyword=0
        for key in dayText: 
            if (user_data == key):
                print ("It corresponds to",dayText[key],'.')
                correct_keyword=1
                break
            
        if (correct_keyword==0):
                print ("Invalid data found. Enter a digit (1-7) or Keyword (2 first letter of weekday)") 

    #Inputs
    #Declare variables and assign values
    try_again = str(input('\nTry again? Y/N : \n'))

    if (try_again!="Y"):
        print("You chose to leave. See you soon!")
        exit()
        

