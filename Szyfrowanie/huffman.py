W = "MMMMMAAARRRRRECCZZZEKK."
W = W + "."
c = 1
H = ""
for i in range(len(W) - 1):
  if W[i] == W[i+1]:
    c+=1
  else:
    if c > 1:
      H += str(c)
    H += W[i]
    c = 1
print(H)