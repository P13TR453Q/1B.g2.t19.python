from random import randint
P = [50, 20, 10, 5, 2, 1]
P.sort(reverse = True)
print(f"Kasa: {P}")
W = []
K = randint(1, 100)
print("Reszta:", K)
P.sort(reverse = True)
for i in P:
  I = (K // i)
  if I > 0:
    K = K - I * i
    for y in range(I):
      W.append(i)
print(W)
      
  


