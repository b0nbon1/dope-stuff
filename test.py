
def count(n, unique):
  if n < 1:
    return 0
  if n == 0:
    return 0
  if n in unique:
    return 0
  unique.add(n)
  print(n)
  return 1+count(n-2, unique)+count(n-4, unique)

unique = set()
print(count(6,unique))
