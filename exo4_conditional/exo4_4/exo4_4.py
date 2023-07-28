#Made with LOVE by Patrick Saint-Louis @2023
#Identify the category of a triangle 
print ('Identifier of triangle category: Equilateral, Isosceles, or Scalene \n')
print ('Data Collection \n')

#Inputs
#Declare variables and assign values
size1 = float(input('Size of 1st Side in Meters: \n'))
size2 = float(input('Size of 2nd Side in Meters: \n'))
size3 = float(input('Size of 3rd Side in Meters: \n'))

#Calculate
if (size1==size2 and size2==size3):
    category="Equilateral"
    reason='3 sides of equal size'
elif(size1==size2 or size2==size3 or size1==size3):
    category="Isosceles"
    reason='2 sides of equal size'
else:
    category="Scalene"
    reason='3 sides of unequal size'
    
#Display outputs
print ('\nIdentifier \n')
print('size 1 = ',size1,'Meters. \n')
print('size 2 = ',size2,'Meters. \n')
print('size 3 = ',size3,'Meters. \n')
print('Consequently, your triangle is',category,
      'because it includes',reason,'. \n')



