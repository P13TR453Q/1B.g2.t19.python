#Zad 1
W = input("Zad 1 \n")
L = list(W)
R = L.copy()
R.reverse()
print(L[0], R[0])
#Zad2
W = input("Zad 2\n")
L = list(W)
R = L.copy()
R.pop(0)
R.pop(-1)
print("".join(R))
#Zad3
W = input("Zad 3\n")
L = list(W)
R = L.copy()
R.reverse()
print(R[0], R[1], R[2], R[3])

