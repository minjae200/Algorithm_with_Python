n = int(input())
number = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_value, min_value = -1e11, 1e11
def dfs(index, total):
    global min_value, max_value, add, sub, mul, div
    if index == n:
        min_value = min(min_value, total)
        max_value = max(max_value, total)
    else:
        if add > 0:
            add -= 1
            dfs(index+1, total+number[index])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(index+1, total-number[index])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(index+1, total*number[index])
            mul += 1
        if div > 0:
            div -= 1
            dfs(index+1, int(total/number[index]))
            div += 1
dfs(1, number[0])        
print(max_value)
print(min_value)