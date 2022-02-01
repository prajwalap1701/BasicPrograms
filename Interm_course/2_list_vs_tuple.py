import sys
import timeit

li = ["hello", 4, "good"]
tup = ("hello", 4, "good")

# Memory efficiency
print(sys.getsizeof(li))
print(sys.getsizeof(tup))

# Time efficiency
print(timeit.timeit(stmt="[1,2,3,4,5]", number=10000000))
print(timeit.timeit(stmt="(1,2,3,4,5)", number=10000000))