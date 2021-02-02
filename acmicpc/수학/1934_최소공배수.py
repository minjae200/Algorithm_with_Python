import math

for _ in range(int(input())):
    A, B = map(int, input().split())
    gcd = math.gcd(A, B)
    lcd = (A*B)//gcd
    print(lcd)