import os
import random
import re
import string

def roll_dice(n, s):
    ''' Returns a list with the results of rolling n dice,
    each dice with s sides; the sum is the last list element

    for example, if n = 2 and s = 6, roll_dice calculates the
    sum of two rolls of a six-sided die '''

    # error checks
    assert abs(n) > 0, "not allowed to roll 0 dice!"
    assert abs(s) > 1, "can't roll 0 or 1 sided dice!"

    # list that holds the results of the dice roll, currently isn't returned
    results = []
    # the roll's total value
    total = 0

    for i in range(abs(n)):
        current = random.randrange(s) + 1
        results.append(current)
        total += current

    # used to interpret subtraction e.g. if the user inputs 1d20 - 2d6
    if n < 0:
        total = -total

    results.append(total)
    # return results
    return total

def parse_roll(roll):
    ''' Returns a list of all the elements in the roll string, which is
    comprised of dice rolls (e.g. 2d20) and modifiers (e.g. 1, -5, 13) joined
    by + or - '''

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

    # calculate result
    result = ""
    total = 0

    for i in range(len(parts)):
        if type(parts[i]) is int:
            # the list element is a modifier, so just add it to the total
            result += str(parts[i])
            total += parts[i]
        else:
            # the list element is a dice roll
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

def print_roll(roll):

    # destroy all whitespace
    for char in string.whitespace:
        roll = roll.replace(char, "")

    # check for invalid characters
    valid = True
    allowed_chars = string.digits + 'd' + '+' + '-' + 'r'

    for char in roll:
        if not (char in allowed_chars):
            print("Invalid roll! Roll can only contain:", allowed_chars)
            valid = False
            break

    if valid:
        parse_roll(roll)

def roll_loop():
    while True:
        roll = input("\nEnter roll: ").strip()

        if roll == 'quit':
            print("Exiting...")
            break
        elif roll == '':
            print ("No roll entered.")
        else:
            print()
            if 'r' in roll:
                roll = roll.replace('r', prev)

            print_roll(roll)
            prev = roll

print("Simple Dice Roller v0.1")
print("author: usipeus")
print("type 'quit' to quit")

roll_loop()
