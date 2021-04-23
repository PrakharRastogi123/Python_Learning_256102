def find_repeated(tup):
    hash = dict()
    for i in tup:
        if i in hash.keys():
            hash[i] += 1
            print("{} is repeated".format(i))
        else:
            hash[i] = 1

a = tuple(map(int, input().split()))
find_repeated(a)



