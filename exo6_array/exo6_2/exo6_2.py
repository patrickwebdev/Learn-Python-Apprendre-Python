#Made with LOVE by Patrick Saint-Louis @2023

import re

try_again="Y"

while (try_again=="Y"):
    #Calculate product table using a loop and a counter variable
    print ('Identifier and calculator of grade information')
    print ('Data Collection \n')

    #Create the messages to display
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

    #Inputs
    #Declare variables and assign values
    user_data = str(input('At least 3 grades out of 100 with a comma between each 2 grades (ex: 60,80,40): \n'))
    #Create an array with the input data
    allGrades = user_data.split(',')
    nbrOfGrades = len(allGrades)
    
    #Validate number of data entered
    if (nbrOfGrades < 3):
        print(messages['errQty'])

    else:
        #Validate data content using regex
        i = 0
        incorrectGrade = 0
        
        while (i<nbrOfGrades):
            isGradeOnly0to9 = not re.match('[0-9-]+$', allGrades[i])
            if (isGradeOnly0to9):  
                incorrectGrade = incorrectGrade + 1
            i = i + 1
        
        if (incorrectGrade > 0):
            print(messages['errType'])

        else :
            #Convert string to int
            i = 0
            while (i<nbrOfGrades):
                allGrades[i] = int(allGrades[i])
                i = i + 1
                
            #Order array elements in ascending
            allGrades.sort()
            
            #Check whether the grades are between 0 and 100
            firstGradeIndex=0
            lastGradeIndex=nbrOfGrades-1
            if (allGrades[firstGradeIndex] < 0 or allGrades[lastGradeIndex] > 100):
                print(messages['errRange'])
            else :
                #Calculate success (grade >=0) and failure (grade > 60)
                countSuccess = 0
                for i in range(0, nbrOfGrades):
                    if (allGrades[i]<60):
                        continue
                    countSuccess = countSuccess + 1
                    
                countFailure = nbrOfGrades - countSuccess

                #Calculate average
                gradeAvg = sum(allGrades) / nbrOfGrades

                #Display outputs
                #Number of grades<60 (failure) and >=60 (success)
                print ('\n')
                print (messages['size'], nbrOfGrades, '\n')
                print (messages['content'])
                for i in range(firstGradeIndex, nbrOfGrades):
                        print(allGrades[i])
                print ('\n')
                print (messages['failure'], countFailure, '\n')
                print (messages['success'], countSuccess, '\n')
                print (messages['lowest'], allGrades[firstGradeIndex], '\n')
                print (messages['greatest'], allGrades[lastGradeIndex], '\n')
                print (messages['avg'], gradeAvg, '\n')

    #Inputs
    #Declare variables and assign values
    try_again = str(input('\nTry again? Y/N : \n'))

    if (try_again!="Y"):
        print("You chose to leave. See you soon!")
        exit()
    
