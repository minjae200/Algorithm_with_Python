from collections import Counter

S = list(filter(lambda x: x, input()))
counter = Counter(S)
alphabet = [0] * 26
for i in counter:
    alphabet[ord(i)-97] = counter[i]
print(*alphabet)