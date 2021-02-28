s = set()
m = int(input())
for _ in range(m):
    command = input().split()
    operation = command[0]
    if operation == 'add':
        value = command[1]
        s.add(value)
    elif operation == 'check':
        value = command[1]
        print(1 if value in s else 0)
    elif operation == 'remove':
        value = command[1]
        s.discard(value)
    elif operation == 'toggle':
        value = command[1]
        if value in s:
            s.remove(value)
        else:
            s.add(value)
    elif operation == 'all':
        s = set([data for data in(1,21)])
    elif operation == 'empty':
        s.clear()