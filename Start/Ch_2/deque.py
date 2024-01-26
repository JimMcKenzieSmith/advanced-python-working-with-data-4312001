# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function
print("Item count:",len(d))

# TODO: deques can be iterated over
for e in d:
    print(e.upper())

# TODO: manipulate items from either end
d.pop()
d.popleft()
d.append(2)
d.appendleft(1)
print(d)

# TODO: use an index to get a particular item
d.rotate(1)
print(d)

my_list = [1,2,3,4,5,6]
d2 = collections.deque(my_list)
print(d2)