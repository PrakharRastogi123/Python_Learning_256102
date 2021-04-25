arr = [1,2,3,4,5,6,7,1]
d = dict()
for i in arr:
    if i not in d.keys():
        d[i] = None
print(d)