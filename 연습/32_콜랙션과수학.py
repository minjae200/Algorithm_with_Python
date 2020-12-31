from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print (data)
print(list(data))

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))


import math
print(math.factorial(5))
print(math.sqrt(7))
print(math.gcd(21,14))
print(21*14 // math.gcd(21,14))
print(math.pi)
print(math.e)