import math
from bisect import bisect_right

MAX = 1000000 + 1
prime = [True] * MAX

for i in range(2, int(math.sqrt(MAX))+1):
    if prime[i]:
        j = 2
        while i*j < MAX:
            prime[i*j] = False
            j += 1

prime[0] = prime[1] = prime[2] = False
array = []
for i, d in enumerate(prime):
    if d: array.append(i)
while True:
    num = int(input())
    if num == 0:
        break

    start = 0
    end = bisect_right(array, num) - 1
    while True:
        a = array[start]    
        b = array[end]
        temp = a + b
        if temp == num:
            break
        elif temp > num:
            end -= 1
        else:
            start += 1

    print("{} = {} + {}".format(num, a, b))