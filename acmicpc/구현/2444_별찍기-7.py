n = int(input())

array = []
for i in range(1, n+1):
    
    prefix = ' '*(n-i)
    print(prefix, end='')
    data = '*'*(i*2-1)
    print(data)
    array.append(prefix+data)

for i in reversed(array[:-1]):
    print(i)
