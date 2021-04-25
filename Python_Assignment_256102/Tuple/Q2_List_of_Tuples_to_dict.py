def list_to_dict(arr):
    hash = dict()
    for i in range(len(arr)):
        hash[i] = arr[i]

    print(hash)


arr = []
n = int(input("Enter number of elements"))
i = 0
while i< n:
    tup = tuple(map(int, input().split()))
    arr.append(tup)
    i+=1

list_to_dict(arr)