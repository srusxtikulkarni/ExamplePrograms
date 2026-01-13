def check_prime(a):
  count=0
  for i in range(1,a+1):
    if a%i==0:
      count+=1
  if count==2:
    print("Number is prime")
  else:
    print("Number is  not prime")
a=int(input("Enter a number to check if it is prime or not:"))
check_prime(a)
