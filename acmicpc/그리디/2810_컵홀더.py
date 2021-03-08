n = int(input())
data = input()

ans = len(data.replace('S', '@').replace('LL', '@')) + 1
print(n if ans >= n else ans)
