#Made with LOVE by Patrick Saint-Louis @2023

#Content to add to the file
data = "Python is a widely used high-level programming language for general-purpose programming, that uses whitespace indentation to delimit code blocks rather than curly brackets or keywords, and a syntax that allows programmers to express concepts in fewer lines of code."

#Message to display
messages = {
'file-exist' : "The file is not created because it already exists",
'file-created' : "The file is successfully created",
'file-written' : "The data is successfully written in the file",
'file-not-written' : "The text was not added to the file because it already exists",
'file-created-error' : "The file failed to be created",
'file-written-error' : "The data failed to be written in the file",
'file-open-error' : "The file cannot be opened for writing"
}

fname = 'helloworld.txt'

#Open the file for reading 
#Just open it if it exists or create it if it doesn't exist yet and open it
try:
    f = open(fname, 'r', encoding="utf-8")
    print (messages['file-exist'])
except:
    f = open(fname, 'w', encoding="utf-8")
    print (messages['file-created'])
    try:
        f = open(fname, 'r', encoding="utf-8")
    except:
        print (messages['file-created-error'])
        exit()

#Write in the file only if the file is empty
    
#Read the file
with open('helloworld.txt', encoding="utf-8") as f:
    read_data = f.read()
#If the file is empty
if (read_data=='')   :
    #Open the file for writing
    #Shown error message if the file cannot be opened
    try:
        f = open(fname, 'w', encoding="utf-8")
    except:
        print (messages['file-open-error'])
        exit()

    #Write in the file 
    try:
        f.write(data)
        print (messages['file-written'])
    except:
        print (messages['file-written-error'])
        exit()
else:
     print (messages['file-not-written'])
     
#close the file and immediately free up any system resources used by it
f.close()


