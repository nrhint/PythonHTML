##This will handle opening the file that you want to open.
##It will check for existing file first.

def openFile():
    File = input("What is the file name:  ")
    Exists = input("Does the file allready exist (y/n):  ")
    if Exists == 'y':
        
        open(File, 'a')
    elif Exists == 'n':
        open(File, 'x')
    else:
        print("Enter a valid exist")
