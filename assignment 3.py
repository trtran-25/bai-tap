#bài 1
n = int(input("Nhập số nguyên n: "))
print(int(str(n)[::-1]))

#bài 2
a, b = map(int, input("Nhập 2 số: ").split())
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

#bài 3
n = int(input("Nhập số n: "))
if n > 0 and (n & (n - 1)) == 0:
    print("True")
else:
    print("False")

#bài 4
m, n = map(int, input("Nhập m và n: ").split())
print(m // n)

#bài 5
m, n = map(int, input("Nhập m và n: ").split())
print(-(-m // n))

#bài 6
x = int(input("Nhập số x: "))
print("Even" if x % 2 == 0 else "Odd")

#bài 7
a, b = map(int, input("Nhập a và b: ").split())
print("Yes" if a < 0 and b < 0 else "No")

#bài 8
a = input("Nhập chuỗi a: ")
b = input("Nhập chuỗi b: ")
print("True" if len(a) > len(b) else "False")

#bài 9
a, b, c = map(int, input("Nhập 3 cạnh: ").split())
if a + b > c and a + c > b and b + c > a:
    print("Yes")
else:
    print("No")

#bài 10
a, b, c, d = map(int, input("Nhập 4 số: ").split())
print(max(a, b, c, d))

#bài 11
a, b, c = map(int, input("Nhập 3 cạnh: ").split())

if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
    print("Không phải tam giác")
elif a == b == c:
    print("Tam giác đều")
elif a == b or b == c or a == c:
    print("Tam giác cân")
else:
    print("Tam giác thường")


#bài 12
n = int(input("Nhập năm: "))
if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
    print("Yes")
else:
    print("No")


#bài 13
kwh = int(input("Nhập số kWh: "))

if kwh <= 50:
    tien_dien = kwh * 1500
elif kwh <= 100:
    tien_dien = 50 * 1500 + (kwh - 50) * 2000
else:
    tien_dien = 50 * 1500 + 50 * 2000 + (kwh - 100) * 3000

print(tien_dien)

#bài 14
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

if a == 0:
    if b == 0:
        print("Vô số nghiệm")
    else:
        print("Vô nghiệm")
else:
    x = -b / a
    print(round(x, 2))

#bài 15
score = float(input("Nhập điểm: "))

if score >= 8.0:
    print("Giỏi")
elif score >= 6.5:
    print("Khá")
elif score >= 5.0:
    print("Trung bình")
else:
    print("Yếu")


#bài 16
x = float(input("Nhập số thực: "))

ltx = int(x) if x >= 0 else int(x) - (x != int(x))

if x > 0:
    ltl = int(x) if x == int(x) else int(x) + 1
else:
    ltl = int(x)

gn = down if abs(x - ltx) < abs(ltl - x) else ltl

print(ltx, ltl, gn)



