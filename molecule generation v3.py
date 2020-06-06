import math
import random


numBond = 30
bondLength = 70

import turtle
turtle.screensize(canvwidth=numBond*bondLength, canvheight=numBond*bondLength)

turtle.color('blue')
turtle.pensize(5)
start = turtle.position()
nodeConnections = {start:[]}

x1 = bondLength*math.cos(-60*((2*math.pi)/360))
y1 = bondLength*math.sin(-60*((2*math.pi)/360))
x2 = bondLength*math.cos(60*((2*math.pi)/360))
y2 = bondLength*math.sin(60*((2*math.pi)/360))

secondAtomLocations = [start+(x1,y1), start+(x2,y2)]
secondAtom = random.choice(secondAtomLocations)
firstBond = ((start+secondAtom)[0]/2,(start+secondAtom)[1]/2)
nodeConnections[start].append(firstBond)
nodeConnections[secondAtom] = [firstBond]
turtle.goto(secondAtom)

i = 1
turtle.color('red')
while i< numBond+1:
    if i%5 == 0:
        turtle.color('blue')
    turtle.penup()
    randAtom = random.choice(list(nodeConnections))
    turtle.goto(randAtom)
    if len(nodeConnections[randAtom]) == 1:
        turtle.seth(turtle.towards(nodeConnections[randAtom][0]))
        choosePath = random.choice([-1,1])
        turtle.left(choosePath*120)
        turtle.pendown()
        turtle.forward(bondLength)
        destination = turtle.position()
        newBond = ((randAtom+destination)[0]/2,(randAtom+destination)[1]/2)
        nodeConnections[randAtom].append(newBond)
        if len(nodeConnections[randAtom]) != 2:
            print(i)
            print('critical error 1')
            i = 50
        if destination in nodeConnections:
            nodeConnections[destination].append(newBond)
        else:
            nodeConnections[destination] = [newBond]
        i+=1
    elif len(nodeConnections[randAtom]) == 2:
        t1 = nodeConnections[randAtom][0]
        t2 = nodeConnections[randAtom][1]
        aveBondLoc = ((t1[0]+t2[0])/2,(t1[1]+t2[1])/2)
        turtle.seth(turtle.towards(aveBondLoc))
        turtle.left(180)
        turtle.pendown()
        turtle.forward(bondLength)
        destination = turtle.position()
        newBond = ((randAtom+destination)[0]/2,(randAtom+destination)[1]/2)
        nodeConnections[randAtom].append(newBond)
        if len(nodeConnections[randAtom]) != 3:
            print(i)
            print('critical error 2')
            i = 50
        if destination in nodeConnections:
            nodeConnections[destination].append(newBond)
        else:
            nodeConnections[destination] = [newBond]
        i+=1
    elif len(nodeConnections[randAtom]) == 3:
        pass
    turtle.color('red')

turtle.done()

