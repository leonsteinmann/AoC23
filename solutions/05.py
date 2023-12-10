import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from inputs.get_input import get_input_string

day = 5


def solve():
    input = get_input_string(day)
    output = 0
    split = input.split('\n\n')
        
    # SEEDS
    seeds = split[0].split(': ')[1].split(' ')
    seeds = list(map(int, seeds))
    # MAPS
    maps = []
    for i in split[1:8]:
        tempMap = i.split(':\n')[1].splitlines()
        for count, j in enumerate(tempMap):
            entry = j.split(' ')
            entry = list(map(int, entry))
            tempMap[count] = entry
        maps.append(tempMap)

    # iterate maps and transform seeds in each round
    # return lowest seed after all transformations
    for seedPosition in range(len(seeds)):
        for conversionMap in maps:
            for entry in conversionMap: 
                if seeds[seedPosition] >= entry[1] and seeds[seedPosition] <= entry[1] + entry[2]:
                    seeds[seedPosition] += entry[0] - entry[1]
                    break
                    
                print(entry[0], entry[1], entry[2])  
                print(seeds)
                 
    print(seeds)
    output = min(seeds)

    
    
    print(f"Solution for day {day}: \n\n{output}")

def solve2():
    input = get_input_string(day)
    output = 0
    split = input.split('\n\n')
        
    # SEEDS
    ranges = split[0].split(': ')[1].split(' ')
    ranges = list(map(int, ranges))

    seeds = []
    for i in range(0, len(ranges), 2):
        start = ranges[i]
        length = ranges[i + 1]
        seeds.extend(list(range(start, start + length)))
        print(i)

    print(len(seeds))
    # MAPS
    maps = []
    for i in split[1:8]:
        tempMap = i.split(':\n')[1].splitlines()
        for count, j in enumerate(tempMap):
            entry = j.split(' ')
            entry = list(map(int, entry))
            tempMap[count] = entry
        maps.append(tempMap)

    # iterate maps and transform seeds in each round
    # return lowest seed after all transformations
    for seedPosition in range(len(seeds)):
        for conversionMap in maps:
            for entry in conversionMap: 
                if seeds[seedPosition] >= entry[1] and seeds[seedPosition] <= entry[1] + entry[2]:
                    seeds[seedPosition] += entry[0] - entry[1]
                    break
                    
                print(entry[0], entry[1], entry[2])  
                print(seeds)
                 
    output = min(seeds)

    
    
    print(f"Solution for day {day} part two: \n\n{output}")

#solve()
solve2()
