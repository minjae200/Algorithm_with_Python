data = input()
mid = len(data) // 2
flag = 0
if len(data) % 2 != 0:
    flag = 1
first = data[:mid+flag]
second = data[mid:]

if first == second[::-1]:
    print(1)
else:
    print(0)
