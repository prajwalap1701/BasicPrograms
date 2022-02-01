add = lambda x,y: x+y
# print(add(5,6))

# ********************************

points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]
sorted_by_y = sorted(points2D, key= lambda x: x[1])
# print(sorted_by_y)

sorted_by_abs = sorted(points2D, key= lambda x: x[0] + x[1])
# print(sorted_by_abs)

# ********************************

# map(func, seq), transforms each element with the function.

a  = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x: x * 2 , a))

# However, try to prefer list comprehension
# Use map if you have an already defined function
c = [x*2 for x in a]
# print(b)
# print(c)

# ********************************

# filter(func, seq), returns all elements for which func evaluates to True.

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = list(filter(lambda x: (x%2 == 0) , a))

# However, the same can be achieved with list comprehension
c = [x for x in a if x%2 == 0]
# print(b)
# print(c)


# ********************************


# reduce(func, seq), repeatedly applies the func to the elements and returns a single value.
# func takes 2 arguments.

from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
sum_a = reduce(lambda x, y: x+y, a)
print(sum_a)