import numpy as np

def spiral(n):

    rows = n
    cols = n

    a = np.zeros((n,n))
    round = n
    i=1
    top_row = 0
    right_col = n-1
    bottom_row = n-1
    left_col = 0
    while (i <= n*n):
             # do top row
            for tr in range(top_row, round):
                a[top_row, tr] = i
                i = i + 1

            # do right col
            for rc in range(top_row+1, round):
                a[rc, right_col] = i
                i = i + 1

            # do bottom row
            for br in range(round - 1 - 1, n - round - 1, -1):
                a[bottom_row, br] = i
                i = i + 1

            # do left column
            for lc in range(round - 1 - 1, n - round, -1):
                a[lc, left_col] = i
                i = i + 1

            round = round - 1
            top_row = top_row + 1
            bottom_row = bottom_row - 1
            right_col -=1
            left_col +=1
            #print(round, i)
            #print(a)

    return a

print(__name__)

if __name__ == '__main__':
    a = spiral(6)
    print(a)
