def refactor(arr):
    i = 0
    while i < len(arr)-1:
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        i += 2 
    print(arr)


a = list(map(int, input().split()))
refactor(a)

