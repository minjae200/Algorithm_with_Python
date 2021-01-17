import heapq

n = int(input())
cards = []
for _ in range(n):
    card = int(input())
    heapq.heappush(cards, card)

result = 0
while len(cards) != 1:
    first_card = heapq.heappop(cards)
    second_card = heapq.heappop(cards)
    heapq.heappush(cards, first_card+second_card)
    result += (first_card + second_card)
print(result)
