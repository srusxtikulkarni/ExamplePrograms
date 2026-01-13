def vow_cons_count(str1):
  count=0
  const=0
  for i in range(len(str1)):
    if str1[i]=='a' or str1[i]=='e' or str1[i]=='i' or str1[i]=='o' or str1[i]=='u':
       count+=1
    else:
       const+=1
  print("Vowels:",count)
  print("Consonants:",const)
s=input("Enter a string:")
res=vow_cons_count(s)

