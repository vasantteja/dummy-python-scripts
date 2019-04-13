#2.Find all such numbers divisible by 7, but not a multiple of 5, between 2000 and 3200 (inclusive). The numbers obtained should be printed on a single line in a comma-separated sequence.
"""
ipadress = input()
nodes = ipadress.split(".")
nodes.pop(0)
print(nodes)

"""

"""
l = []
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))
"""


"""
values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)

"""
"""
y = input("Enter the words> ")
y = y.split(",")
y = sorted(y)
#map(lambda x:x.lower(),y)
print(",".join(y))\
"""

"""
words = [x for x in input().split(',')]
words.sort()
print(','.join(words))
"""
"""
s = input()
words = [word for word in s.split(" ")]
words = map(lambda x:x.lower(),words)
print(" ".join(sorted(list(set(words)))))
"""
"""
words = [x for x in input().split(',')]
#words = map(lambda x:x.lower(),words)
words = list(map(lambda x:x.lower(),words))
words.sort()
print(','.join(words))
"""

"""
words = input("Enter sequence of words separated by whitespace: ").split(' ')
words_set = set(words)
print(' '.join(sorted(words_set)))
#print(words_set)
"""
