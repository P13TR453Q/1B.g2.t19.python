# #Zad 1
# x = int(input())
# suma = 0
# while x > 0:
#   y = x % 10
#   suma += y
#   x //= 10
  
# print(suma)

#Zad 2
# x = int(input())
# p = 0
# for i in range(1, x+1):
#   if x % i == 0:
#     p += 1
#     break
# if p == 0:
#   print(f"{x} jest liczbą pierwszą.")
# else: 
#   print(f"{x} nie jest liczbą piewszą")

# Zad 3
# x = int(input())
# suma = 0
# for i in range(1, x+1):
#   if x % i == 0:
#     suma += 1
# if suma == i:
#   print(f"{x} jest liczbą doskonałą.")
# else: 
#   print(f"{x} nie jest liczbą doskonałą")

#Zad 4
# a = int(input())
# b = int(input())
# x = a
# y = b
# while y > 0:
#   x, y = y, x % y
# if x == 1:
#   print(f"Liczba {a} i {b} są względnie pierwsze")
# else:
#   print(f"Liczba {a} i {b} nie są względnie pierwsze")

#Zad 5

# m = int(input())
# for i in range(10, 19):
#   x = i
#   y = m
#   while m > 0:
#     x, y = y, x % y
#   if x == 1:
#      print(i)

#Zad 6


a = int(input())
b = int(input())
while b > 0:
  x = a
  y = b
  x, y = y, x % y
print(f"{a} / {b} = {a / x} / {b / x}")