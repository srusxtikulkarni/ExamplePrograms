def largest(a,b,c):
  if a>b:
    if a>c:
     return a
    else:
      return c
  else:
    if b>c:
      return b
    else:
      return c
a=int(input("Enter value a:"))
b=int(input("Enter value b:"))
c=int(input("Enter value c:"))
res=largest(a,b,c)
print("Largest number is:",res)
