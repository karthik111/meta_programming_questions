import math


# Add any extra import statements you may need here


# Add any helper functions you may need here

count = [1]
bfs = []
Done = False

def minOperations(arr):
    global count
    global bfs
    global Done

    if Done:
        return count.pop()

    print("Arr: ", arr)
    for i in range(len(arr)):
        perm_arr = [] + arr[0:i+1]
        prefix_arr = [] + arr[i+1:]
        prefix_arr.reverse()

        new_arr = perm_arr + prefix_arr
        print('new_arr: ', new_arr)
        print('arr: ', arr)
        if is_sorted(new_arr) or is_sorted(arr):
            q = count.pop()
            print("Done: ", q)
            count.append(q)
            Done = True
            return q

        rev_arr = [] + new_arr
        rev_arr.reverse()

        bfs.append(rev_arr)


    for e in bfs:
        count.append(count.pop() + 1)
        minOperations(e)




def minOperations1(arr):
    count = 0
    if is_sorted(arr):
        return count

    #for i in range(len(arr) - 1):
    while not is_sorted(arr):
        start = 0
        end = start + 1
        start, end = find_start_end(arr)

        if start == 0:
            rev_sub_arr = arr[end::-1]
        else:
            rev_sub_arr = arr[end:start-1:-1]

        print("arr: ", arr, ' start: ', start, ' end: ', end, ' rev_sub_array: ', rev_sub_arr, ' count: ', count)
        if count == 10:
            return count

        r = 0
        for j in range(start, end + 1):
            arr[j] = rev_sub_arr[r]
            r += 1

        print(' reversed arr: ', arr)

        count += 1
        if (is_sorted(arr)):
            return count


# Write your code here

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def find_start_end(arr):
    start = 0
    end = start + 1
    while end < len(arr) and arr[end] <= arr[start]:
        start += 1
        end = start + 1

    while end+1 < len(arr) and arr[end+1] >= arr[end]:
        end += 1

    return start, end

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
    n_1 = 5
    arr_1 = [1, 2, 5, 4, 3]
    expected_1 = 1
    output_1 = minOperations(arr_1)
    check(expected_1, output_1)

    Done = False
    bfs = []
    count = [1]

    n_2 = 3
    arr_2 = [3, 1, 2]
    expected_2 = 2
    output_2 = minOperations(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
