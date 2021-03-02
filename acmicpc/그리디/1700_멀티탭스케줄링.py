import heapq

n, k = map(int, input().split())
array = list(map(int, input().split()))

plug = []
ans = 0

for i in range(k):
    if array[i] in plug:
        continue
    if len(plug) < n:
        plug.append(array[i])
        continue

    idxs = []
    for j in range(n):
        try:
            index = array[i:].index(plug[j])
        except:
            index = 101
        idxs.append(index)
    del plug[idxs.index(max(idxs))]
    plug.append(array[i])
    ans += 1

print(ans)
