# Git Repo: https://github.com/Hjortur17/HR_Assignment8

x = 1
y = 1

def moveUp():
    global y
    y += 1
    return y

def moveDown():
    global y
    y -= 1
    return y

def moveLeft():
    global x
    x -= 1
    return x

def moveRight():
    global x
    x += 1
    return x

def checkLocation(x, y):
    return x,y

while checkLocation != (3,3):
    if checkLocation(x, y) == (1, 1):
        print ("You can travel: (N)orth.")
        user_input = input("Direction: ")
        user_lower = user_input.lower()

        if user_lower == "n":
            moveUp()
        else:
            print ("Not a valid direction!")
    elif checkLocation(x, y) == (1, 2):
        print ("You can travel: (N)orth or (E)ast or (S)outh.")
        user_input = input("Direction: ")
        user_lower = user_input.lower()

        if user_lower == "n":
            moveUp()
        elif user_lower == "e":
            moveRight()
        elif user_lower == "s":
            moveDown()
        else:
            print ("Not a valid direction!")
else:
    print("Victory!")