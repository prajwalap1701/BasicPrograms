from itertools import product

prod = product([1, 2], [3, 4])
# print(list(prod)) # note that we convert the iterator to a list for printing

# to allow the product of an iterable with itself, specify the number of repetitions
prod = product([1, 2], [3], repeat=2)
# print(list(prod)) # note that we convert the iterator to a list for printing

# *****************************************************************

from itertools import permutations

perm = permutations([1, 2, 3])
# print(list(perm))

# optional: the length of the permutation tuples
perm = permutations([1, 2, 3], 2)
# print(list(perm))

# *****************************************************************
from itertools import combinations, combinations_with_replacement

# the second argument is mandatory and specifies the length of the output tuples.
comb = combinations([1, 2, 3, 4], 2)
# print(list(comb))

comb = combinations_with_replacement([1, 2, 3, 4], 2)
# print(list(comb))

# *****************************************************************

from itertools import accumulate

# return accumulated sums
acc = accumulate([1,2,3,4])
# print(list(acc))

# other possible functions are possible
import operator
acc = accumulate([1,2,3,4], func=operator.mul)
# print(list(acc))

acc = accumulate([1,5,2,6,3,4], func=max)
# print(list(acc))

# *****************************************************************

from itertools import groupby


# use a function as key
def smaller_than_3(x):
    return x < 3


group_obj = groupby([1, 2, 3, 4], key=smaller_than_3)
for key, group in group_obj:
    print(key, list(group))

# or use a lamda expression, e.g. words with an 'i':
group_obj = groupby(["hi", "nice", "hello", "cool"], key=lambda x: "i" in x)
for key, group in group_obj:
    print(key, list(group))

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

for key, group in groupby(persons, key=lambda x: x['age']):
    print(key, list(group))