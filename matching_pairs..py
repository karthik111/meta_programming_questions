import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
    match = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            s_1 = swap(s, i, j)
            if (compare(t, s_1) > match):
                match = compare(t, s_1)

    return match

# Write your code here

def swap(s, i, j):
    new = list(s)
    c = s[i]
    d = s[j]
    new[i] = d
    new[j] = c
    return "".join(new)

def compare(a, b):
    count = 0
    for x, y in zip(a, b):
        if x == y:
            count += 1

    return count

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


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
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    # Add your own test cases here
