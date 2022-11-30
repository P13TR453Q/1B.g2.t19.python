#Odej
# a = int(input())
# b = int(input())
# i = a * b
# while  a != b :
#   if a > b : a = a - b
#   if b > a : b = b - a
# print(i // a)
#Modulo
a, b = int(input()), int(input())
i = a * b
while b > 0:
  a, b = b, a % b
print(i // a)
    