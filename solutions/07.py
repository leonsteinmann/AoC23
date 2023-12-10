import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from inputs.get_input import get_input

day = 7


def solve():
    input = get_input(day)
    output = 0

    five = []
    four = []
    fullHouse = []
    three = []
    twoPair = []
    onePair = []
    high = []

    for inputCard in input:
        card = tuple(inputCard.split(' '))
        counts = {}

        for char in card[0]:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

        values = list(counts.values())
        if values.count(5) == 1:
            five.append(card)
            continue
        if values.count(4) == 1:
            four.append(card)
            continue
        if values.count(3) == 1 and values.count(2) == 1: 
            fullHouse.append(card)
            continue
        if values.count(3) == 1:
            three.append(card)
            continue
        if values.count(2) == 2:
            twoPair.append(card)
            continue
        if values.count(2) == 1:
            onePair.append(card)
            continue
        high.append(card)



    custom_order = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7,
                '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
    def custom_sort_key(tuple_item):
        return [custom_order[char] for char in tuple_item[0]]
    
    five.sort(key=custom_sort_key, reverse=True)
    four.sort(key=custom_sort_key, reverse=True)
    fullHouse.sort(key=custom_sort_key, reverse=True)
    three.sort(key=custom_sort_key, reverse=True)
    twoPair.sort(key=custom_sort_key, reverse=True)
    onePair.sort(key=custom_sort_key, reverse=True)
    high.sort(key=custom_sort_key, reverse=True)

    allCards = five + four + fullHouse + three + twoPair + onePair + high
    currentRank = len(allCards)
    for card in allCards:
        output += int(card[1]) * currentRank
        currentRank -= 1

    print(f"Solution for day {day}: \n\n{output}")

solve()
