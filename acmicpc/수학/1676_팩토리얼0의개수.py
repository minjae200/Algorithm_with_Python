import math

n = int(input())
result = 0
for i in reversed(str(math.factorial(n))):
    if int(i) != 0:
        break
    result +=1
print(result)
