
def all_subarrays(arr):
    sub = {}
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(arr[i:j+1])
            sub[(i,j)] = arr[i:j+1]

    return sub