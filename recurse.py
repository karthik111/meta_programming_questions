
def fibonnaci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

if __name__ == '__main__':
    for i in range(10):
        print(fibonnaci(i+1), end = '  ')
