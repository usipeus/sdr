import os
import random
import re
import string

def roll_dice(n, s):
    ''' Returns a list with the results of rolling n dice,
    each dice with s sides; the sum is the last list element '''
    assert abs(n) > 0, "not allowed to roll 0 dice!"
    assert abs(s) > 1, "can't roll 1 sided dice!"

    results = []
    total = 0
    for i in range(abs(n)):
        current = random.randrange(s) + 1
        results.append(current)
        total += current

    if n < 0:
        total = -total

    results.append(total)
    # return results
    return total

def parse_roll(roll):
    ''' Returns a list of all the elements in the roll '''

    # destroy all whitespace
    for char in string.whitespace:
        roll = roll.replace(char, "")

    # check for invalid characters
    allowed_chars = string.digits + 'd' + '+' + '-'
    for char in roll:
        if not (char in allowed_chars):
            print("Invalid roll! Roll can only contain:", allowed_chars)
            break

    # separate into parts (divided by + or -)
    roll = roll.replace('-', '+-')
    parts = roll.split('+')

    # create a list for each dice roll and convert everything to ints
    for i in range(len(parts)):
        if 'd' in parts[i]:
            # find the integers to the left and right of the 'd'
            d_loc = parts[i].find('d')
            parts[i] = [int(parts[i][:d_loc]), int(parts[i][d_loc + 1:])]
        else:
            # convert the modifiers to integers
            parts[i] = int(parts[i])

    return parts

def print_roll(roll):
    parts = parse_roll(roll)
    result = ""
    total = 0

    # calculate result
    for i in range(len(parts)):
        if type(parts[i]) is int:
            result += str(parts[i])
            total += parts[i]
        else:
            current_roll = roll_dice(parts[i][0], parts[i][1])
            result += "{" + str(parts[i][0]) + "d" + str(parts[i][1])
            result += ": " + str(current_roll) + "}"
            total += current_roll

        if i != len(parts) - 1:
            result += ' + '

    print("You entered:", roll)
    print("Interpreted as:", parts)
    print("Result:", result)
    print("Total:", total)
    print()

print("Simple Dice Roller v0.1")
print("author: usipeus")
print("type r to reroll, q to quit")

while True:
    roll = input("Enter roll: ").strip()
    if roll == 'q':
        print("\nExiting...")
        break
    elif roll == 'r':
        print_roll(prev)
    else:
        print()
        print_roll(roll)
        prev = roll
