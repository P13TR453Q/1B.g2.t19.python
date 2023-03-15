from random import randint
m = None
n = 10
L = [randint(1,30) for i in range(n)]
print(L)

for i in range(n):
 for j in range(i+1, n):
    m = i
    if L[j] < L[m]:
      m = j
  L[i], L[m] = L[m], L[i]
print(L)