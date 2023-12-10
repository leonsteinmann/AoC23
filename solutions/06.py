import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from inputs.get_input import get_input

day = 6


def solve():
    input = get_input(day)
    output = 1
   
    times = input[0].split(':        ')[1].split('     ')
    times = list(map(int, times))
    distances = input[1].split(':   ')[1].split('   ')
    distances = list(map(int, distances))

    for i in range(len(times)):
        beatingCounter = 0
        t = times[i]
        record = distances[i]
        for t1 in range(t):
            distance = t1 * t - pow(t1, 2)
            if distance > record:
                beatingCounter += 1
        output *= beatingCounter
    print(f"Solution for day {day}: {output}")


def solve2():
    input = get_input(day)
    output = 1
   
    

    beatingCounter = 0
    t = 52947594
    record = 426137412791216
    for t1 in range(t):
        distance = t1 * t - pow(t1, 2)
        if distance > record:
            beatingCounter += 1
    output *= beatingCounter


    print(f"Solution for day {day} part two: {output}")



solve()
solve2()
