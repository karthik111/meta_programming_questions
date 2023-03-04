import math


# Add any extra import statements you may need here


# Add any helper functions you may need here

MAX_I = 1000000
MAX_R = 1000000

def rotationalCipher(input, rotation_factor):
    # Write your code here

    output = ""
    for c in input:
        if c.isdigit():
            c_out = rotate_digit(c, rotation_factor)
        elif c.isalpha():
            c_out = rotate_alpha(c, rotation_factor)
        else:
            c_out = c
        output = output + str(c_out)

    return output

def rotate_digit(c, rotation_factor):
    #global MAX_I, MAX_R

    rotation_factor = rotation_factor % 10

    if int(c) + rotation_factor > 9:
        c_out = rotation_factor - (9 - int(c) + 1)
    else:
        c_out = int(c) + rotation_factor

    return c_out

def rotate_alpha(c, rotation_factor):

    rotation_factor = rotation_factor % 26
    if c.islower():
        max = ord('a') + 25
        start = ord('a')
    else:
        max = ord('A') + 25
        start = ord('A')

    if ord(c) + rotation_factor > max:
        c_out = start + rotation_factor - (max - ord(c)) - 1
    else:
        c_out = ord(c) + rotation_factor

    return chr(c_out)

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    check(expected_2, output_2)

    # Add your own test cases here
