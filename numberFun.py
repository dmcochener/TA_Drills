# Python    3.6.1
#
# Author:   Deanna Cochener
#
# Purpose:  Drill for the Tech Academy to show skills in basic Python
#           Fun with Numbers

from math import isnan, floor

def start():
    welcome = "Welcome to our little numbers and math demonstration!" #assign string to variable
    print (welcome)
    x = int(input("What is your favorite number? "))
    #Use print function and format notation
    print("Your number is {}.\nLet's have some fun with numbers! \nFirst let's count...".format(x)) 
    countUp(x)
    print("Now let's do some simple functions.")
    y = int(input("Let's pick another number! What number would you like? "))
    print("Great! Now your numbers are {} and {}...".format(x,y))
    simpleFunc(x,y)
    print("Ok, now let's do some comparisons, so pick another number!")
    z = int(input("What number would you like? "))
    print("Great! your third number is " + str(z) + ".")
    compare(x,y,z)
    print("Now let's learn look at those numbers squared, and to the power of 3...")
    power(x,y,z)
    print("See numbers are fun! \nLet's use them to count other things, like the length of words.")
    c = 0  # assign int to variable
    c = getNumber(c)
    #Create a tuple, see colorsList for iteration print
    colors_dict = {3: ['red','ash'], 4: ['blue','aqua'], 5: ['green','slate'], 6: ['yellow','orange'],
                   7: ['magenta','apricot'], 8: ['cerulean','mahogany'], 9: ['turquoise','persimmon']}
    print("Let's find a couple color names with {} characters in them!".format(c))
    # Call function that returns a string and print 
    picked_colors = colors(c,colors_dict)
    print (picked_colors[0].capitalize() + " and " + picked_colors[1] + " both have {} characters".format(c))
    colorsList(colors_dict)
    print("I hope you had fun! I did!")


def countUp(x):
    i = 0    #assign integer
    while i <= x: #Use while loop
        print (i)
        i += 1   #Use +=


def simpleFunc(x,y):
    addition = x + y  # Use +
    subtraction = x - y # Use -
    multiply = x*y #Use *
    divide = float(x)/float(y) #Use /
    divint = floor(divide) #Use =
    remain = x%y # Use %
    print("Your numbers add up to {}. \nYour first number number ({}) minus your second number ({}) is {}.".format(addition,x,y,subtraction))
    print("If we multiply the numbers, we get {}, \nAnd if we divide the first ({}) by the second ({}), we get {}.".format(multiply,x,y,divide))
    print("You could also express the division as {} with a remainder of {}, \nbut it only makes sense if the first number is the larger one.".format(divint,remain))

def compare(x,y,z):  #Use if, elif, else, operators and, or, not
    if (x > y) & (x > z):
        print("Your first number, {}, is the largest number!".format(x))
    elif (y > x) & (y > z):
        print("Your second number, {}, is the largest number!".format(y))
    elif (z > x) & (z > y):
        print("Your third number, {}, is the largest number!".format(z))
    elif (x == y & x != z) | (x == z & x != y) | (y == z & z !=x):
        print("You chose two numbers that are equal!")
        if (x == y) & (x > z):
            print("The first and second numbers {} are larger than the third!".format(x))
        elif x == y:
            print("The third number {} is larger than the others!".format(z))
        elif (x == z) & (x > y):
            print("The first and third numbers {} are larger than the second!".format(x))
        elif x == z:
            print("The second number {} is larger than the others!".format(y))
        elif (y == z) & (y > x):
            print("The second and third numbers {} are larger than the first!".format(y))
        else:
            print("The first number {} is larger than the others!".format(x))
    else:
        print("All three numbers have the same value!")

def power(x,y,z):  # Create list and iterate through to print each item on new line
    number_list_or = [x,y,z]
    number_list_sq = []
    for number in number_list_or:
        number_list_sq.append(number**2)
    number_list_tr = []
    for number in number_list_or:
        number_list_tr.append(number**3)
    i = 0
    for number in number_list_or:
        print("Your number {} is {} when squared and to the third power, it's {}".format(number_list_or[i],number_list_sq[i],number_list_tr[i]))
        i += 1
    
    
def getNumber(c):
    i = 0
    for i in range(0,4): #Use for loop
        if (i != 0) & ((int(c) < 3) | (int(c) > 9)):    # use of !=, 
            print("Please enter a valid selection")
            
        if  (int(c) < 3) | (int(c) > 9): #use OR operator
            c = input("Pick a new number between 3 and 9: ")
            i +=1
        else:
            c = floor(float(c)) #assign float to variable
            return c

    print("Too many invalid selections. Quitting program.")
    x = 0
    return x
    exit()


def colors(c,colors_dict):    # Function that returns a string
    picked_colors = colors_dict[c]
    return picked_colors

def colorsList(colors_dict):
    stop = True
    while stop:
        choice = input("\nDo you want to see the whole colors list? y/n: ").lower()
        if choice == "y":  # iterate through tuple and print
            v = 3
            for color in colors_dict:
                colors=colors_dict[v]
                print("Colors with {} characters include {} and {}.".format(v,colors[0],colors[1]))
                v += 1
            stop = False
        elif choice == "n":
            print("\nOk. Thanks for playing along. Have a good day!")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y' for 'YES', 'n' for 'NO'...")
    
    
    
    
    
    
if __name__ == "__main__":
    start()

    
