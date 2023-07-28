#Made with LOVE by Patrick Saint-Louis @2023

try_again="Y"

while (try_again=="Y"):
    #Calculate product table using a loop and a counter variable
    print ('Calculator of product table using a loop and a counter variable')
    print ('Data Collection \n')

    #Inputs
    #Declare variables and assign values
    user_number = int(input('Number between 1 to 10: \n'))


    #Validate, calculate and display outputs
    if (user_number<1 or user_number>10):
        print("Error! You didn't enter a number between 1 to 10 \n")
    else:
        print("You entered",user_number,"\n")
        
        #While loop
        print("Multiplication Table Calculator with a WHILE loop")
        count = 1
        
        while (count <= 10):
            print(count,"x",user_number,"=",count * user_number)
            count=count+1

        #For loop
        print("Multiplication Table Calculator with a FOR loop")
        for count in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print(count,"x",user_number,"=",count * user_number)

    #Inputs
    #Declare variables and assign values
    try_again = str(input('\nTry again? Y/N : \n'))

    if (try_again!="Y"):
        print("You chose to leave. See you soon!")
        exit()
        

