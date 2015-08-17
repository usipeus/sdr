import random
import re
import string

def roll(n, s):
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
    return results

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
    roll = roll.replace('-', '+ -')
    parts = roll.split('+')

    return parts

def print_roll(roll):
    parts = parse_roll(roll)

    print("You entered:", roll)
    # print("Interpreted as:", )
    # print("Result:", 

print(parse_roll("4 - 1d20 + 4d6 - 5 + 2"))
print(roll(-2, 6))
