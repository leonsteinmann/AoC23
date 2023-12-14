import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from inputs.get_input import get_input

day = 10

# dict that translates a char and a direction to a new direction
charAndOldToNewDirection = {
    "|" : {
        "n" : "s",
        "s" : "n",
    },
    "-" : {
        "e" : "w",
        "w" : "e",
    },
    "L" : {
        "n" : "e",
        "e" : "n",
    },
    "J" : {
        "n" : "w",
        "w" : "n",
    },
    "7" : {
        "s" : "w",
        "w" : "s",
    },
    "F" : {
        "s" : "e",
        "e" : "s",
    },
}

# dict that translates new direction to old direction when moving forward to next position in grid
# this is used during movement to determine where we came from on the new position and calculate with charAndOldToNewDirection after the new direction
newToOldDirection = {
    "n" : "s",
    "s" : "n",
    "e" : "w",
    "w" : "e",
}

# dict that translates a direction to a position change
directionToPositionChange = {
    "n" : (-1, 0),
    "s" : (1, 0),
    "e" : (0, 1),
    "w" : (0, -1),
}


def solve():
    input = get_input(day)
    output = 0
    for i in range(len(input)):
        input[i] = list(input[i])

    # initially one of the connections of the "S" starting position depending on the input
    # in my case: "L" with position (42, 24) and the "S" on the right side --> newDirection = "n"
    currentPos = (42, 24)

    # always store the data were we came from the last position
    # is updated when moving to a new position --> oldDirection = newToOldDirection[newDirection]
    oldDirection = ""

    # always store the data were we go next in oder to determine new position
    # is updated when moving to a new position after updating oldDirection --> newDirection = charAndOldToNewDirection[input[currentPosition[0]][currentPosition[1]]][oldDirection]
    # 
    # initially the direction of the selected starting position
    newDirection = "n"
    
    # count the steps taken
    steps = 0
    sCounter = 0
    # move to next position until we reach again the starting position
    # after moving calculate new direction and update old direction
    while sCounter < 2:
        steps += 1
        currentPos = (currentPos[0] + directionToPositionChange[newDirection][0], currentPos[1] + directionToPositionChange[newDirection][1])
        if input[currentPos[0]][currentPos[1]] == 'S':
            break
        oldDirection = newToOldDirection[newDirection]
        newDirection = charAndOldToNewDirection[input[currentPos[0]][currentPos[1]]][oldDirection]
        
    # output is half of the steps taken
    # +1 because we dont actually start at the starting position but at the next position
    output = int((steps+1)/2)        
    
    print(f"Solution for day {day} part 1: {output}")


solve()
