def simple_interest(p,t,r):
  si=p*t*r/100
  return si
p=int(input("Enter principal amount:"))
t=int(input("Enter time(in yrs)"))
r=int(input("Enter rate of interest per annum:"))
res=simple_interest(p,t,r)
print("Simple interest is:",res)
