A = [1, 2, 3,3]

li = list(set(A))
li.sort()
li2 = []
for i in li:
    li2.append(A.count(i))
print(li2)