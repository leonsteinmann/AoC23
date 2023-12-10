import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from inputs.get_input import get_input

day = 3


def solve():
    input = get_input(day)
    output = 0
    coordinates = set()

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if not char.isdigit() and char != '.':
                for i in [y - 1, y, y + 1]:
                    for j in [x - 1 , x, x + 1]:
                        if input[i][j].isdigit():
                            xCoordinate = j
                            while xCoordinate > 0 and input[i][xCoordinate-1].isdigit():
                                xCoordinate -= 1
                            
                            coordinates.add(tuple([xCoordinate, i]))
                            


    for coordinate in coordinates:
        number = ""
        xPointer = coordinate[0]
        while xPointer < len(input[0]) and input[coordinate[1]][xPointer].isdigit():
            number = number + input[coordinate[1]][xPointer]
            xPointer += 1

        print(number)
        output += int(number)

    print(f"Solution for day {day}: \n\n{output}")



solve()
