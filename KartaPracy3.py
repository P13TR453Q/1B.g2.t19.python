#pre
#pętla liczb od 10 do 22\
# for i in range(10, 22):
#     print(i, end=" ")

#pętla licvzb dwucyfrowych malejąco (split ujemny)

# for i in range(99, 9, -1):  print(i, end=" ")

#to same (split dodatni)

# for i in range(-99,-9,1):  print(i*(-1),end=" ")

#pętla liczb trzycyfrowych podzielnych przez 20

# for i in range(100, 1000, 20):  print(i, end=" ")

#Zad 1
# a = int(input())
# for i in range(a):  print(i, ** 3 + 3, end = " ")
#pre 2
#Pętle for liczb trzycyfrowych podzielnych przez 13
# for i in range(104, 1000, 13):
#   print(i)
#Pętle for liczb dwucyfrowych parzystych
# for i in range (8, 100, 2):
#   print(i)
#Pętle for potęg cyfr: 0, 1, 4, 9, 16, ...81
# for i in range(0, 10):
#   print(i * i, end=" ")

#Zad 3
# n = int(input(":D"))
# for i in range(n, n+1):
#    if n % i == 0:
#     print(i)

#Zad 4
# suma = 0
# for i in range(10, 100):
#   suma = (suma + i)

# print(suma)
#Zad 5
# a = int(input())
# suma = (a * (a + 1) // 2)
# for i in range(a - 1):
#    b  = int(input())
#    suma = suma - b
  
# print(suma)
# #Zad 6
# c = int(input())
# a, b = 0, 1
# for i in range(c):
#   a, b = b , a + b

#   print(a, end=" ")