array = list(map(lambda x: x*x ,list(map(int, input().split()))))
print(sum(array) % 10)