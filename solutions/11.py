import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from inputs.get_input import get_input

day = 11


def solve():
    inputGrid = get_input(day)
    # input grid is a 2 dimensional field consiting of Stars: "#" or Empty: "."
    # Definition Row: row of position n == inputGrid[n]
    # Definition Column: column of position n == [inputGrid[i][n] for i in range(len(inputGrid))]
    inputGrid = [list(line) for line in inputGrid]
    output = 0
    
    
    initRowsCount = len(inputGrid)
    initColumnsCount = len(inputGrid[0])

    rowsWithNoStars = []
    columnsWithNoStars = []
    # if a entire row contains entirely "." and no "#", add the row index to rowsWithNoOccupiedSeats
    for i in range(initRowsCount):
        if inputGrid[i].count("#") == 0:
            rowsWithNoStars.append(i)
    
    
    # if a entire column contains entirely "." and no "#",  add the row index to columnsWithNoOccupiedSeats
    for i in range(initColumnsCount):
        if [inputGrid[j][i] for j in range(initRowsCount)].count("#") == 0:
            columnsWithNoStars.append(i)

    # for each rowIndex in rowsWithNoStars, insert a row of "." before the row with index rowIndex
    for rowIndex in rowsWithNoStars:
        inputGrid.insert(rowIndex, ["." for i in range(initColumnsCount)])
        for i in range(len(rowsWithNoStars)):
            rowsWithNoStars[i] += 1

    # for each columnIndex in columnsWithNoStars, insert a column of "." before the column with index columnIndex
    for columnIndex in columnsWithNoStars:
        for row in inputGrid:
            row.insert(columnIndex, ".")
        for i in range(len(columnsWithNoStars)):
            columnsWithNoStars[i] += 1

    # find the coordinates of all stars and store them in starPositions
    starPositions = []
    for rowIndex in range(len(inputGrid)):
        for columnIndex in range(len(inputGrid[rowIndex])):
            if inputGrid[rowIndex][columnIndex] == "#":
                starPositions.append((rowIndex, columnIndex))
    

    # dic with position as key and a list of already used positions
    alreadyCountedPairs = {}
    # add the shortest distance between all pairs of stars to the output
    # saves the already used pairs of stars in  alreadyCountedPairs
    for position in starPositions:
        for otherPosition in starPositions:
            if position == otherPosition or (position) in alreadyCountedPairs and otherPosition in alreadyCountedPairs and (otherPosition in alreadyCountedPairs[position] or position in alreadyCountedPairs[otherPosition]):
                continue
            output += abs(otherPosition[0] - position[0]) + abs(otherPosition[1] - position[1]) 
        
            if position in alreadyCountedPairs:
                alreadyCountedPairs[position].append(otherPosition)
            else:
                alreadyCountedPairs[position] = [otherPosition]

            if otherPosition in alreadyCountedPairs:
                alreadyCountedPairs[otherPosition].append(position)
            else:
                alreadyCountedPairs[otherPosition] = [position]
            print("stars: " + str(position) + " and " + str(otherPosition) + " added: " + str(abs(otherPosition[0] - position[0]) + abs(otherPosition[1] - position[1])))

    print(f"Solution for day {day}: \n\n{output}")

solve()
