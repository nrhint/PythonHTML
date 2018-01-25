print("Starting")

##Import files:
import CssMaker

##Setup Vars
run = True
xxx = True #Used for varius purpusses
MainMenu = {0:'Exit', 1:'Add lines'}

currMenu = MainMenu

##main loop
def MAIN():
    i= input("What is the name of the file that you wish to edit/create?  ")
    openF(i)
    while run == True:
        print(currMenu)
        inp = input()
        for x in currMenu:
            if int(inp) == x:
                print(currMenu[x])
                pass
                

##Define stuff

def openF(fname):
    try:
        f = open(fname, '+')
    except FileNotFoundError:
        f = open(fname, 'x')
MAIN()

###this will allow you to place your content where you want.
##
##print("STARTING MAIN.py...")
####Do stuff
##import CssMaker
##run = True
##
##print("This will create a HTML file for you where you will type inf the text and then be able yo use it in a webpage.")
##print()
##print()
####required to work:
##fileName = input("What will the name of your file be? (use index of its the first file in the web pages).  ")
##openFile = open(str(fileName) + ".html", 'x')
####use css sheet?
##CssX = input("do you want to use a css sheet (y/n):  ")
##if CssX == 'y':
##    CssZ = input("do you want to use a existing sheet (y/n):  ")
##    if CssZ == 'y':
##        cssFile = input("What is the CSS file name:  ")
##        CssMaker.link()
##    elif CssZ == 'n':
##        CssMaker.create(fileName)
##    else:
##        print("!!invalid input!!")
##        
####opening HTML tag
##openFile.write("<html>")
##
#####!!!NOT WORKING!!!###
##
######opening head tag
####openFile.write(" <head>")
####titleBar = input("What will the title bar display?  ")
####openFile.write(titleBar)
######closing head tag
####openFile.write(" </head>")
####opening body tag
##openFile.write(" <body>")
##
####define functions:
##
##def h1():
##    openFile.write("  <H1>")
##    ##insert hedding 1
##    pageTitle = input("What will be the hedder:  ")
##    openFile.write(pageTitle)
##    openFile.write("  </H1>")
##def p():
##    openFile.write("  <p>")
##    ##insert body content
##    mainBody = input("insert the text:  ")
##    openFile.write(mainBody)
##    openFile.write("  </p>")
##def link():
##    ##create a hyperlink:
##    linkText = input("What text will be displayed for the link:  ")
##    linkDest = input("What text will be the destinition for the link:  ")
##    openFile.write("  <a href=\""+linkDest+"\">"+linkText+"</a>")
####main loop:
##
##while run == True:
##    userIn = input("enter 0 to exit, 1 to add a header 2 to add body text and press 3 to add a internal link:  ")
##    if userIn == '0' or userIn == None:
##        run = False
##        print("Exiting programm...")
##    if userIn == '1':
##        h1()
##    if userIn == '2':
##        p()
##    if userIn == '3':
##        link()
####closing body tag
##openFile.write(" </body>")
####closing HTML tag
##openFile.write("</html>")
##openFile.write("This file was created by a programm for making HTML files.")
##openFile.close()
##
##
