#bài 3
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(round(a / b, 2))

#bài 4
a1, b1, c1, a2, b2, a3 = map(float, input().split())
tb = ((a1 + b1 + c1) + (a2 + b2) * 2 + a3 * 3) / 10
print(round(tb, 1))

#bài 5
a, b = map(int, input().split())
print(a ** b)

#bài 6
ch = input().strip()
print(ord(ch))
print(ch.upper())

#bài 7
A = ((13 ** 2) * 3) + 5
B = 13 ** 2 * 3 + 5
print(A)
print(B)

#bài 8
C = float(input())
F = 9/5 * C + 32
print(round(F, 2))

#bài 9
x = float(input())
total = (x + 10) * 1.3 * 1.1
print(round(total, 2))

#bài 11
h, m = map(int, input().split())
print(h * 3600 + m * 60)

#bài 12
n = int(input())
print(6 * n * n)

#bài 13
a, b = map(int, input().split())
print((a * b) % 10)

#bài 14
a, b = map(int, input().split())
a, b = b, a
print(a, b)

#bài 15
n = int(input())
print(6 * (n - 1))



