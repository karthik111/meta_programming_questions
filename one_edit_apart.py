
def OneEditApart(s1, s2):
    if abs(len(s1) - len(s2)) >= 2:
        return False
    if len(s1) == len(s2):
       once = False
       for i in range(len(s1)):
           if s1[i] != s2[i]:
               if once == True:
                   return False
               once = True
       return True

    if len(s2) > len(s1):
        c = s1
        s1 = s2
        s2 = c

    for i in range(len(s1)):
        if i < len(s2) - 1 and s1[i] != s2[i]:
            if s1[i+1:len(s1)] == s2[i:len(s2)]:
                return True
            else:
                return False

    return True


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

if __name__ == '__main__':

    expected_1 = False
    output_1 = OneEditApart("cat", "dog")
    check(expected_1, output_1)

    output_2 = OneEditApart("cat", "cats")
    expected_2 = True
    check(expected_2, output_2)

    output_3 = OneEditApart("cat", "cut")
    expected_3 = True
    check(expected_3, output_3)

    output_4 = OneEditApart("cat", "cast")
    expected_4 = True
    check(expected_4, output_4)

    output_5 = OneEditApart("cat", "at")
    expected_5 = True
    check(expected_5, output_5)

    output_6 = OneEditApart("cat", "act")
    expected_6 = False
    check(expected_6, output_6)