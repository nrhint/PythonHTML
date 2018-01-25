##This will create a CSS sheet.
def create():
    print("STARTING CssMaker.py...")
    run = True
    print()
    print()
    ##Open the CSS file for edditing or createing.
    inp = input("What sheet number will this be:  ")
    CssFile = open("style"+str(inp)+".css", 'x')

    ##Create basic outline:
    CssFile.write("body{")
    while run == True:
        print("Press 0 to exit, 1 to change text color")
        choice = input()
        if choice == '0':
            run = False
        elif choice == '1':
            input("What color do you want:  ")
            
def link():
    print("STARTING CssMaker.py...")
    fileName = input("What is the name of the css file:  ")
    x = open(fileName, 'r')


print("CssMaker.py imported")
