#this took forever, lots of fiddling with global variables

def lineUp(commands):
    global right
    right = 0
    global left
    left = 0
    global around
    around = 0
    global p1direction
    p1direction = 'south'
    global p2direction
    p2direction = 'south'
    global same_direction
    same_direction = 0

    def p1turn_right(): 
        print "P1 TURNING RIGHT"
        global right
        right += 1
        global p1direction
        if p1direction == 'south':
            p1direction = 'west'
        elif p1direction == 'west': 
            p1direction = 'north'
        elif p1direction == 'north': 
            p1direction = 'east'
        elif p1direction == 'east': 
            p1direction = 'south'

    def p1turn_left(): 
        print "P1 TURNING LEFT"
        global left
        left += 1
        global p1direction
        if p1direction == 'south':
            p1direction = 'east'
        elif p1direction == 'east': 
            p1direction = 'north'
        elif p1direction == 'north': 
            p1direction = 'west'
        elif p1direction == 'west': 
            p1direction = 'south'

    def p1turn_around(): 
        print "P1 TURNING AROUND"
        global around
        around += 1
        global p1direction
        if p1direction == 'south':
            p1direction = 'north'
        elif p1direction == 'north': 
            p1direction = 'south'
        elif p1direction == 'east': 
            p1direction = 'west'
        elif p1direction == 'west': 
            p1direction = 'east'

    def p2turn_left(): 
        print "P2 ACCIDENTALLY TURNING RIGHT"
        global right
        right += 1
        global p2direction
        if p2direction == 'south':
            p2direction = 'west'
        elif p2direction == 'west': 
            p2direction = 'north'
        elif p2direction == 'north': 
            p2direction = 'east'
        elif p2direction == 'east': 
            p2direction = 'south'

    def p2turn_right(): 
        print "P2 ACCIDENTALLY TURNING LEFT"
        global left
        left += 1
        global p2direction
        if p2direction == 'south':
            p2direction = 'east'
        elif p2direction == 'east': 
            p2direction = 'north'
        elif p2direction == 'north': 
            p2direction = 'west'
        elif p2direction == 'west': 
            p2direction = 'south'

    def p2turn_around(): 
        print "P2 TURNING AROUND"
        global around
        around += 1
        global p2direction
        if p2direction == 'south':
            p2direction = 'north'
        elif p2direction == 'north': 
            p2direction = 'south'
        elif p2direction == 'east': 
            p2direction = 'west'
        elif p2direction == 'west': 
            p2direction = 'east'

    for letter in commands: 
        
        if letter == "R": 
            p1turn_right()
            p2turn_right()
            if p2direction == p1direction: 
                print "HURRAY"
                same_direction += 1
        elif letter == "L":
            p2turn_left()
            p1turn_left()
            if p2direction == p1direction: 
                print "HURRAY"
                same_direction += 1
        elif letter == 'A': 
            p1turn_around()
            p2turn_around()
            if p2direction == p1direction: 
                print "HURRAY"
                same_direction += 1

    print "right turns:",right 
    print "left turns:",left
    print p1direction
    print p2direction
    return same_direction
