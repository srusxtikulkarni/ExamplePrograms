def check_palin(num):
  rev=0
  m=0
  temp=num
  while num>0:
    m=num%10
    rev=rev*10+m
    num=num//10
  if rev==temp:
    print("Number is palindrome")
  else:
    print("Not Palindrome")
num=int(input("Enter a number to check palindrome:"))
check_palin(num)
