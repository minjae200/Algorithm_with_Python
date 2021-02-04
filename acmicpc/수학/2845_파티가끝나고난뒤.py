l, p = map(int, input().split())
people = l*p
array = list(map(int, input().split()))
for i in range(5):
    print(array[i]-people, end=' ')