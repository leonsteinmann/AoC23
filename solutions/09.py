import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from inputs.get_input import get_input

day = 9


def solve():
    input = get_input(day)
    output = 0
    
    for numberSeries in input:
        series = numberSeries.split(' ')
        series = list(map(int, series))
        rows = [series]

        lastRow = rows[0]
        while not all(n == 0 for n in lastRow):
            newRow = []
            for i in range(len(lastRow) - 1):
                newRow.append(lastRow[i + 1] - lastRow[i])
            rows.append(newRow)
            lastRow = newRow
        for i in range(len(rows) -1, 0, -1):
            rows[i-1].append(rows[i-1][-1] + rows[i][-1])
        output += rows[0][-1]

    print(f"Solution for day {day} part 1: {output}")

def solve2():
    input = get_input(day)
    output = 0
    
    for numberSeries in input:
        series = numberSeries.split(' ')
        series = list(map(int, series))
        rows = [series]

        lastRow = rows[0]
        while not all(n == 0 for n in lastRow):
            newRow = []
            for i in range(len(lastRow) - 1):
                newRow.append(lastRow[i + 1] - lastRow[i])
            rows.append(newRow)
            lastRow = newRow

        for i in range(len(rows) -1, 0, -1):
            rows[i-1].insert(0, rows[i-1][0] - rows[i][0])
        
        output += rows[0][0]

    print(f"Solution for day {day} part two: {output}")

solve()
solve2()


