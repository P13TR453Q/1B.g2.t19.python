from random import randint
L = [randint(1,20) for i in range(20)]
print(f"Lista: {L}")
print(f"{(max(L))}")
print(min(L))
print(L.count(max(L)))
print(L.count(min(L)))
print(f"{max(L)}-{min(L)}")
print(sum(L))