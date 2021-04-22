#Longest Word
#Given a text as input, find and output the longest word.

#Sample Input
#this is an awesome text

#Sample Output
#awesome


txt = input()
k=txt.split(' ')
l=max(len(t) for t in k)
for p in k:
    if l==len(p):
        print(p)
        break

