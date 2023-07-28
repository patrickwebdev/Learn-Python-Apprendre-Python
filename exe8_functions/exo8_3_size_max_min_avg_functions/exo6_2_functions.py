#Made with LOVE by Patrick Saint-Louis @2023

import re

try_again="Y"

while (try_again=="Y"):
    #Calculate product table using a loop and a counter variable
    print ('Identifier and calculator of grade information')
    print ('Data Collection \n')

    #User-defined function to save the messages to display
    def allMessages():
        messages = {
            'size':'The number of grades entered is: ',
            'content':'The grades entered are: ',
            'success':'The number of grades greater than or equal to 60% is: ',
            'failure':'The number of grades lower than 60% is: ',
            'avg':'The average grade is: ',
            'greatest':'The greatest grade is: ',
            'lowest':'The lowest grade is: ',
            'errType':"Error! You didn't enter only numbers for the grades!",
            'errRange':"Error! You didn't enter only numbers between 0 and 100 for the grades!",
            'errQty':"Error! You didn't enter a minimum of 3 grades!"
        }
        return messages

    #User-defined function to collect and save the data entered
    def getGrades() :
        #Declare variables and assign values
        user_data = str(input('At least 3 grades out of 100 with a comma between each 2 grades (ex: 60,80,40): \n'))
        #Create an array with the input data
        allGrades = user_data.split(',')
        return allGrades

    #User-defined function to validate number of data entered
    def validateNbrOfGrades(allGrades):
        #Calculate number of grades
        nbrOfGrades = len(allGrades)
        #Compare number of grades
        if (nbrOfGrades < 3):
            return False
        else:
            return True
        
    #User-defined function to validate data content using regex
    def validateIsGradeNumber (allGrades):
        i = 0
        incorrectGrade = 0  
        #Check whether each grade include only combination of 0 to 9 or not
        while (i<len(allGrades)):
            isGradeOnly0to9 = not re.match('[0-9-]+$', allGrades[i])
            if (isGradeOnly0to9):  
                incorrectGrade = incorrectGrade + 1
            i = i + 1
        if (incorrectGrade > 0):
            return False
        else :
            return True
        
    #User-defined function to convert string array elements to int
    def convertStrArraytoIntArray(allGrades):
        i = 0
        while (i<len(allGrades)):
            allGrades[i] = int(allGrades[i])
            i = i + 1
        return allGrades

    #User-defined function to order int array elements in ascending
    def orderGradesInAsc(allGrades):         
        allGrades.sort()
        return allGrades
            
    #User-defined function to validate whether int array elements are between 0 and 100
    def isGradeBetween0And100(allGrades):
        firstGradeIndex=0
        lastGradeIndex=len(allGrades)-1
        if (allGrades[firstGradeIndex] < 0 or allGrades[lastGradeIndex] > 100):
            return False
        else :
            return True

    #User-defined function to calculate quantity of array elements that are greater or equal to or lower than 60 
    def isLowerThan60OrNot(allGrades):
        countSuccess = 0
        #Calculate greater or equal to 60 (success) 
        for i in range(0, len(allGrades)):
            if (allGrades[i]<60):
                continue
            countSuccess = countSuccess + 1
        #Calculate lower than 60 (failure) 
        countFailure = len(allGrades) - countSuccess
        #Save success and failure counted in an array an return it
        dayDigit={'successCount':countSuccess, 'failureCount':countFailure}
        return dayDigit

    #User-defined function to calculate average of int array elements 
    def calculateAverage(allGrades):
        gradeAvg = sum(allGrades) / len(allGrades)
        return gradeAvg


    #Main user-defined function that calls the other functions to implement the context of this program
    #User-defined function to display outputs
    def displayOutputs():
        #Call the user-defined function that returns the messages to display
        messages = allMessages()
        #Call the user-defined function that reads the grades and save them
        listOfGrades = getGrades()
        #Call the user-defined function that validates whether the quantity of grades is correct or not
        if (validateNbrOfGrades(listOfGrades)==True):
            #Call the user-defined function that validates whether the grades entered includes only digits or not
            if (validateIsGradeNumber (listOfGrades)==True):
                #Call the user-defined function that converts string array elements grades to int and order them in ascending
                listOfGrades = orderGradesInAsc(convertStrArraytoIntArray(listOfGrades))
                #Call the user-defined function to validate whether grades are between 0 and 100
                if (isGradeBetween0And100(listOfGrades)==True):
                    #Everything is okay, let's calculate and display results
                    #Display the quantity of grades
                    firstGradeIndex = 0
                    lastGradeIndex = len(listOfGrades) - 1
                    print ('\n')
                    print (messages['size'], len(listOfGrades), '\n')
                    #Display all the grades
                    print (messages['content'])
                    for i in range(firstGradeIndex, len(listOfGrades)):
                        print(listOfGrades[i])
                    print ('\n')
                    #Call the user-defined function to calculate quantity of grades that are greater or equal to or lower than 60
                    successOrFailure=isLowerThan60OrNot(listOfGrades)
                    #Display the quantity of grades < 60 (failure) and >= 60 (success)
                    print (messages['failure'], successOrFailure['failureCount'], '\n')
                    print (messages['success'], successOrFailure['successCount'], '\n')
                    #Display the greatest and the lowest grades
                    print (messages['lowest'], listOfGrades[firstGradeIndex], '\n')
                    print (messages['greatest'], listOfGrades[lastGradeIndex], '\n')
                    #Call the user-defined function to calculate average of grades and display it
                    print (messages['avg'], calculateAverage(listOfGrades), '\n')
                else:
                    print(messages['errRange'])  
            else:
                print(messages['errType'])
        else:
            print(messages['errQty'])
            
    #Call the function
    displayOutputs()
    
    #Inputs
    #Declare variables and assign values
    try_again = str(input('\nTry again? Y/N : \n'))

    if (try_again!="Y"):
        print("You chose to leave. See you soon!")
        exit()
    
