def print_primes(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)
s=int(input("Enter start range:"))
e=int(input("Enter end range:"))
print_primes(s,e)
