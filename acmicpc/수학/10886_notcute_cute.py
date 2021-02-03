n = int(input())
cute = 0
notcute = 0
for _ in range(n):
    data = int(input())
    if data == 1:
        cute += 1
    else:
        notcute += 1

print("Junhee is not cute!") if cute < notcute else print("Junhee is cute!")