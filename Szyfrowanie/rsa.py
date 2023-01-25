# from math import gcd
# print(gcd(15,20))


#wybor dwoch duzych liczb pierwszych
p = 101
q = 97
print(p, q)
# funkcja Eulera
n = p * q
F = (p - 1) * (q - 1)
print(n,"\n", F)
##Klucz publiczny e, taki że NWD(F,e) = 1
from math import gcd
for i in range(2, F):
  if gcd(i, F) == 1:
    e = i
    break
print(e, n)
##Klucz prywatny d taki ze d*e%F == 1
for i in range(2, F):
  if ((i*e) % F) == 1:
    d = i
    break
print(d,n)
##Jak szyfrowac?
## m - wiadomosc
## c = m**e % n (c - tekst zaszyfrowany)
##t = c**d % n (t = tekst jawny)
m = input()
c = ""
for i in m:
  c += chr((ord(i)**e)%n)
print(m, c)
t =""
for i in c:
  t += chr((ord(i)**e)%n)