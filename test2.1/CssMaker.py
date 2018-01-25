##This will create a CSS sheet.
def create(filename):
    print("STARTING CssMaker.py...")
    run = True
    print()
    print()
    ##Open the CSS file for edditing or createing.
    inp = input("What sheet name will this have:  ")
    CssFile = open("style"+str(inp)+".css", 'x')

    ##Create basic outline:
    while run == True:
        print("Press 0 to exit, 1 to change text color")
        choice = input()
        if choice == '0':
            run = False
        elif choice == '1':
            color = input("What color do you want:  ")
            CssFile.write("""
body {
    color: """+str(color)+""";
}
""")        ##Link the css to the HTML
            HTMLFile = open(filename, 'a')
            HTMLFile.write("""
    <link rel="stylesheet" href="""+str(CssFile)+"""">
""")
    CssFile.close()
            
def link():
    print("STARTING CssMaker.py...")
    fileName = input("What is the name of the css file:  ")
    x = open(fileName, 'r')


print("CssMaker.py imported")
