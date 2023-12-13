import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from inputs.get_input import get_input

day = 8


def solve():
    input = get_input(day)
    output = 0
    
    leftRightInstructions = input[0]
    
    nodes = {}
    for i in range(2, len(input)):
        node = input[i]
        splitNameAndNodes = node.split(" = ")

        leftNodeName = splitNameAndNodes[1][1:4]
        rightNodeName = splitNameAndNodes[1][6:9]
        nodes[splitNameAndNodes[0]] = (leftNodeName, rightNodeName)

    currentNode = 'AAA'
    while currentNode != 'ZZZ':
        for instruction in leftRightInstructions:
            if currentNode == 'ZZZ':
                break
            if instruction == 'L':
                currentNode = nodes[currentNode][0]
            elif instruction == 'R':
                currentNode = nodes[currentNode][1]
            else:
                print("ERROR: Invalid instruction")
                break
            output += 1
    

    print(f"Solution for day {day}: \n\n{output}")



solve()
