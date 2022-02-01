def tri_recursion(k):
  if(k == 1):
    return 1
  else:
    return k * tri_recursion(k - 1)

print(tri_recursion(6))
