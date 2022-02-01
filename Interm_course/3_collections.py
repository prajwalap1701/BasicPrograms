from collections import Counter

str = "hello world, good morning"
my_counter = Counter(str)
# print(my_counter)
# print(my_counter.most_common(2))

# ********************************************************
from collections import namedtuple

Point = namedtuple('Point', 'x,y,z')
pt1 = Point(5, 4, -1)
pt2 = Point(8, -5, 0)
# print(pt1, pt1.x,pt1.y, pt2,)

# ***********************************************************

from collections import defaultdict

d = defaultdict(int)

d['a'] = 1
d['b'] = 2
# print(d['d'])

# *************************************************************

from collections import deque

q = deque()

q.extend([4,5,3,2])
# print(q)
q.appendleft(8)
# print(q)
q.rotate(1)
# print(q)
