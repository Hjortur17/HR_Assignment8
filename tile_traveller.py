# Git Repo: https://github.com/Hjortur17/HR_Assignment8

x = 1
y = 1

def moveUp(y):
    y += 1
    return y

def moveDown(y):
    y -= 1
    return y

def moveLeft(x):
    x -= 1
    return x

def moveRight(x):
    x += 1
    return x

def checkLocation(x,y):
    return x,y

for locX in range(1, 4):
    for locY in range(1, 4):
        # if checkLocation
            # You can travel: (N)orth or (E)ast or (S)outh.
        print("Location:", checkLocation(locX, locY))