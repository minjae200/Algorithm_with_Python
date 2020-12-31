string = str(input())

group = { "0": 0, "1": 0}

prev = string[0]
for cur in string[1:]:
    if prev != cur:
        group[prev] += 1
        prev = cur
group[prev]+=1
print(min(group.values()))