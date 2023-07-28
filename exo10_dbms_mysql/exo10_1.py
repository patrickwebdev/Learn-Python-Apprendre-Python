#Made with LOVE by Patrick Saint-Louis @2023

try_again="Y"

while (try_again=="Y"):

    #The module PyMySQL is not part of the default modules of a fresh installed copy of python
    #To install it, you can for example use pip, like this > pip install PyMySQL 
    #And then you will be able to import it to implement it in your code
    import pymysql
    
    #Declare variables and assign values 
    dbName = 'users' 
    tbName = 'employees'
    
    #Collect information, insert it to MySQL database, select and display it
    print ('Collect information, insert it to MySQL database, select and display it')
    print ('Data Collection \n')
    
    #Input
    #userInput = int(input('Digit or Number: \n'))
    theFirstName=str(input('Employee First Name: \n'))
    theLastName=str(input('Employee Last Name: \n'))
    theEmail=str(input('Employee Email: \n'))

    #1-Connect to the DBMS MySQL using PyMySql
    try:
        connection = pymysql.connect(host='localhost',user='root',password='')
        print ('Connection opened successfully to MySQL')
    except pymysql.Error as e:
        print("Could not open connection to MySQL. Error PyMySQL %d: %s" %(e.args[0], e.args[1]))
        exit()

    #2-Create the database if it doesn't exist yet
    try:
        #Prepare a cursor object using cursor() method
        cursor = connection.cursor()
        #Execute sql request
        sqlRequest = "CREATE DATABASE IF NOT EXISTS " + dbName
        cursor.execute(sqlRequest)
        #Commit to save the changes because connection is not autocommit by default 
        connection.commit()
        print ("Database '",dbName,"' already exists or was created successfully to MySQL")
    except pymysql.Error as e:
        print("Could not create the database '",dbName,"'. Error PyMySQL %d: %s" %(e.args[0], e.args[1]))
        exit()
    
    #3-Select the database
    try:
        connection.select_db(dbName)
        print ("Database '",dbName,"' successfully selected")
    except pymysql.Error as e:
        print("Could not select the database '",dbName,"'. Error PyMySQL %d: %s" %(e.args[0], e.args[1]))
        exit()

    #4-Create the table if it doesn't exist yet
    try:
        #Execute sql request
        sqlRequest = "CREATE TABLE IF NOT EXISTS " + tbName + " (id INT(5) PRIMARY KEY AUTO_INCREMENT,firstname VARCHAR(35) NOT NULL,lastname VARCHAR(35) NOT NULL,email VARCHAR(35) NOT NULL) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"         
        cursor.execute(sqlRequest)
        #Commit to save the changes because connection is not autocommit by default 
        connection.commit()
        print ("Table '",tbName,"' already exists or was created successfully to MySQL")
    except pymysql.Error as e:
        print("Could not create table '",tbName,"'. Error PyMySQL %d: %s" %(e.args[0], e.args[1]))
        exit()
    
    #5-Record data to table columns (Insert) 
    try:
        #Execute sql request
        #"INSERT INTO employees (firstname, lastname, email) VALUES ('theFirstName', 'theLastName', 'theEmail')"
        sqlRequest = "INSERT INTO " + tbName + " (firstname, lastname, email) VALUES (' "+theFirstName+" ', ' "+theLastName+" ', ' "+theEmail+" ')"
        cursor.execute(sqlRequest)
        #Commit to save the changes because connection is not autocommit by default 
        connection.commit()
        print ("Data was successfully recorded to table '",tbName," '")
    except pymysql.Error as e:
        print("Could not record data to table '",tbName,"'. Error PyMySQL %d: %s" %(e.args[0], e.args[1]))
        exit()

    #6-Retrieve and display data from table columns (select) 
    try:
        #Execute sql request
        sqlRequest = "SELECT * FROM " + tbName 
        cursor.execute(sqlRequest)
        #Commit to save the changes because connection is not autocommit by default 
        connection.commit()
        numberOfRowsFound = cursor.rowcount
        print (numberOfRowsFound,"rows were successfully retrieved from table '",tbName," '")
        # Fetch all the rows and display them using a loop
        if (numberOfRowsFound==0):
            print ("There is no data to display")
        else :
            print ("Find below these data:")
            dataFound = cursor.fetchall()
            print('ID ','Firstname ','Lastname ','Email')
            for eachRow in dataFound:
                print(eachRow[0],eachRow[1],eachRow[2],eachRow[3])
    except pymysql.Error as e:
        print("Could not retrieve data from table '",tbName,"'. Error PyMySQL %d: %s" %(e.args[0], e.args[1]))
        exit()
    
    #7-Disconnect from the DBMS MySQL 
    try:
        connection.close()
        print("Connection closed successfully from MySQL")
    except pymysql.Error as e:
        print("Could not close connection from MySQL. Error PyMySQL %d: %s" %(e.args[0], e.args[1]))

    #Inputs
    #Declare variables and assign values
    try_again = str(input('\nTry again? Y/N : \n'))

    if (try_again!="Y"):
        print("You chose to leave. See you soon!")
        exit()
