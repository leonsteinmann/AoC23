import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
from inputs.get_input import get_input

day = 2

redLimit = 12
greenLimit = 13
blueLimit = 14

def parse_games(input_lines):
    games = []
    
    for line in input_lines:
        game_info = line.split(': ')
        game_id = int(game_info[0].split()[1])  # Extract game ID
        
        subsets = game_info[1].split('; ')  # Split subsets
        
        game_data = {'game_id': game_id, 'subsets': []}
        for subset in subsets:
            subset_data = {}
            subset_split = subset.split(', ')
            
            for subset_item in subset_split:
                quantity, color = subset_item.split()
                subset_data[color] = int(quantity)
                
            game_data['subsets'].append(subset_data)
        
        games.append(game_data)
    
    return games

def solve():
    input = get_input(day)
    output = 0

    parsed_games = parse_games(input)
    for game in parsed_games:
        inValidGame = False
        for subset in game['subsets']:
            if 'red' in subset and subset['red'] > redLimit:
                inValidGame = True
            if 'green' in subset and subset['green'] > greenLimit:
                inValidGame = True
            if 'blue' in subset and subset['blue'] > blueLimit:
                inValidGame = True
        
        if inValidGame == False:
            output += game['game_id']

    print(f"Solution for day {day}: \n\n{output}")


def solve2():
    input = get_input(day)
    output = 0
    parsed_games = parse_games(input)


    for game in parsed_games:
        maxDict = {}
        for subset in game['subsets']:
            if 'red' in subset:
                if 'red' not in maxDict or subset['red'] > maxDict['red']:
                    maxDict['red'] = subset['red']
            if 'green' in subset:
                if 'green' not in maxDict or subset['green'] > maxDict['green']:
                    maxDict['green'] = subset['green']
            if 'blue' in subset:
                if 'blue' not in maxDict or subset['blue'] > maxDict['blue']:
                    maxDict['blue'] = subset['blue']

        # add to the output the product of maxDict values
        product = 1
        for key in maxDict:
            product *= maxDict[key]
        output += product
    

    print(f"Solution for day {day} part 2: \n\n{output}")

solve()
solve2()

