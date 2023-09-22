

# #Zad 1
# print("Zad 1")
# a = int(input())

# def podzielnosc(a):
#     return a % 3

# if podzielnosc(a) == 0:
#     print("True")
# else:
#     print("False")
# #Zad 2
# print("Zad 2")
# b = int(input())
# def podzielnosc(b):
#     return b % 17

# if podzielnosc(b) in range(100, 999) and podzielnosc(a)== 0:
#     print("True")
# else:
#     print("False")

# #Zad 3
# print("Zad 3")
# c = int(input())
# if c >= 18:
#      print("True")
# else:
#     print("False")
    
# #Zad 4
# print("Zad 4")
# limit = 20
# d = int(input())
# if d < limit:
#     print(f"{d} / {limit}, Mozna jechac")
# else:
#     print(f"{d} / {limit}, Nie, mozna jechac")
    
#Zad 5
print("Zad 5")
e = int(input())
f = int(input())
g = int(input())
h = []
h.append(e)
h.append(f)
h.append(g)
if h[1] > h[0] and h[1] < h[2] or h[1] > h[2] and h[1] < h[0]:
    print("True")
else:
    print("False")
