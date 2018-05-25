a = 1

while a < 10:
  if a % 2 == 0:
    print(a)
  a += 1

lst = [5, 4, 8, 1, 7, 2]
l = 6
# To sort the list
for i in range(6):
  for j in range(6):
    if lst[i] > lst[j]:
      x = lst[i]
      lst[i] = lst[j]
      lst[j] = x
      
      
      
      
