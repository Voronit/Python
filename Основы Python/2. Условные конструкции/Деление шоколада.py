n = int(input ("Enter the length of the chocolate: "))
m = int(input ("Enter the width of the chocolate: "))
k = int(input ("How many slices do you want to take? "))

if (k <= n * m) and ((k % n == 0) or (k % m == 0)):
  print("YES")
else:
  print("NO")