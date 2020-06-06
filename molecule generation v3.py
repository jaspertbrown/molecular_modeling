import math
import random

#number of lines and length of each line
numBond = 30
bondLength = 70

#screen size
import turtle
turtle.screensize(canvwidth=numBond*bondLength, canvheight=numBond*bondLength)

#color and line width
turtle.color('blue')
turtle.pensize(5)

#initial position (atom 1)
start = turtle.position()

#begin dictionary of important locations
#dictionary of the form {atomLocation: [bondLocations]}
#every atom will have between 1 and 3 bond locations
nodeConnections = {start:[]}


#possible coordinates of 2nd atom (probably can be removed due to symmetry)
x1 = bondLength*math.cos(-60*((2*math.pi)/360))
y1 = bondLength*math.sin(-60*((2*math.pi)/360))
x2 = bondLength*math.cos(60*((2*math.pi)/360))
y2 = bondLength*math.sin(60*((2*math.pi)/360))
secondAtomLocations = [start+(x1,y1), start+(x2,y2)]
secondAtom = random.choice(secondAtomLocations)

#bond between first 2 atoms
#bond info must be added to entry for first atom
#entry for 2nd atom must be created, and must also have bond info
firstBond = ((start+secondAtom)[0]/2,(start+secondAtom)[1]/2)
nodeConnections[start].append(firstBond)
nodeConnections[secondAtom] = [firstBond]
turtle.goto(secondAtom)


#begin constructing molecule of size numBond
i = 1
turtle.color('red')
while i< numBond+1:
    
    #this is to help count bonds
    if i%5 == 0:
        turtle.color('blue')
    
    #lift pen up and move to random atom location
    turtle.penup()
    randAtom = random.choice(list(nodeConnections))
    turtle.goto(randAtom)
    
    #determine whether chosen atom has 1,2, or 3 bonds currently
    
    #if 1 bond must randomly choose between 2 available
    if len(nodeConnections[randAtom]) == 1:
        #turn towards bond that is already there
        turtle.seth(turtle.towards(nodeConnections[randAtom][0]))
        
        #randomly turn to one of the bonds and draw it
        choosePath = random.choice([-1,1])
        turtle.left(choosePath*120)
        turtle.pendown()
        turtle.forward(bondLength)
        
        #determine new position
        destination = turtle.position()
        
        #determine location of new bond
        newBond = ((randAtom+destination)[0]/2,(randAtom+destination)[1]/2)
        
        #add bond info to start atom
        nodeConnections[randAtom].append(newBond)
        
        #debugging check
        if len(nodeConnections[randAtom]) != 2:
            print(i)
            print('critical error 1')
            i = 50
            
        #check if destination already exists
        #if it does add the bond info to it, otherwise create new entry with bond info
        if destination in nodeConnections:
            nodeConnections[destination].append(newBond)
        else:
            nodeConnections[destination] = [newBond]
        i+=1
    
    #if random atom already has 2 bonds then the third bond must be drawn
    elif len(nodeConnections[randAtom]) == 2:
        
        #locations of pre-existing bonds
        t1 = nodeConnections[randAtom][0]
        t2 = nodeConnections[randAtom][1]
        
        #midpoint between bonds
        aveBondLoc = ((t1[0]+t2[0])/2,(t1[1]+t2[1])/2)
        
        #turn turtle towards midpoint
        turtle.seth(turtle.towards(aveBondLoc))
        
        #the bond we want to draw is exactly opposite this direction
        turtle.left(180)
        
        #draw new bond
        turtle.pendown()
        turtle.forward(bondLength)
        
        #determine new position
        destination = turtle.position()
        
        #determine location of new bond
        newBond = ((randAtom+destination)[0]/2,(randAtom+destination)[1]/2)
        
        #add bond info to start atom
        nodeConnections[randAtom].append(newBond)
        
        #debugging check
        if len(nodeConnections[randAtom]) != 3:
            print(i)
            print('critical error 2')
            i = 50
        
        #determine if destination already exists
        #if it does add the bond info to it, otherwise create new entry with bond info
        if destination in nodeConnections:
            nodeConnections[destination].append(newBond)
        else:
            nodeConnections[destination] = [newBond]
        i+=1
    
    #if random atom already has 3 bonds then it is not a valid location
    elif len(nodeConnections[randAtom]) == 3:
        pass
    
    #helps with counting bonds
    turtle.color('red')

#program crashes if not here
turtle.done()

