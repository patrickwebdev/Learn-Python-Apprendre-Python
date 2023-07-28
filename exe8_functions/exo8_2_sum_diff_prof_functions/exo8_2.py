#Made with LOVE by Patrick Saint-Louis @2023

try_again="Y"

while (try_again=="Y"):
    
    #Use functional structure to calculate and display sum, difference and product table using a loop and a counter variable
    print ('Use functional structure to calculate and display sum, difference and product table using a loop and a counter variable')
    print ('Data Collection \n')


    #Input
    userInput = int(input('Digit or Number: \n'))


    #User-defined function to calculate and display the sum
    def getSum(a):
        print("SUM")
        for i in range(1, 11, 1):
            print(a ," + ", i ," = ", a + i, "\n")

    #User-defined function to calculate and display the sum
    def getDiff(a):
        print("DIFFERENCE")
        for i in range(1, 11, 1):
            print(a ," - ", i ," = ", a - i, "\n")    

    #User-defined function to calculate and display the sum
    def getProd(a):
        print("PRODUCT")
        for i in range(1, 11, 1):
            print(a ," x ", i ," = ", a * i, "\n")    

    #Call the functions
    getSum(userInput)
    getDiff(userInput)
    getProd(userInput)

    #Inputs
    #Declare variables and assign values
    try_again = str(input('\nTry again? Y/N : \n'))

    if (try_again!="Y"):
        print("You chose to leave. See you soon!")
        exit()
