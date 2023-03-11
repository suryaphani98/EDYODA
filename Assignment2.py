#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

tuple1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

List2 =[]
List3 =[]

for t in tuple1:
    List2.append(t[1])

List2.sort()
print(List2)

for l in List2:
    for q in tuple1:
        if l == int(q[1]):
            List3.append(q)

print(List3)

#Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

ASCII = dict()
for i in range(97,123):
    ASCII[chr(i)] = i
print(ASCII)