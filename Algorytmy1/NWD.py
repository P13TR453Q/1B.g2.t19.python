#Odej
# a = int(input())
# b = int(input())
# while a != b:
#   if a > b : a = a - b
#   if b < a : b = b - a
# print(a)
#Modulo
a = int(input())
b = int(input())
while b > 0:
  a , b = b, a % b
print(a)