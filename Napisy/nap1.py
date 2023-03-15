# s = input()
# print(s)

# for i in s:
#   print(i)
# #lub:
# for i in range(len(s)):
#   print(s[i])

# L = [5, 7, 4]
# print(L)
# L.sort()
# print(L)

# s.sort() to jest błąd!!!]

#przechodzenie napis <-> lista (list i join)

# s = input()
# L = list(s)
# print(s, L)
# L.sort()
# print(s, L)
# s = "".join(L)
# print(s, L)

##Napis algorytm ktoy sprawdzi czy wyraz jest palindromem:

##Wer.1
# s = input()
# l = list(s)
# r = l.copy()
# r.reverse()
# if l == r:
#   print(f"{s} jest palindromem")
# else:
#   print(f"{s} nie jest palindromem")

##Wer.2
s = input()
for i in range(len(s)// 2):
  if s[i] != s[(len(s)) -1-i]:
    exit("nie")
exit("tak")