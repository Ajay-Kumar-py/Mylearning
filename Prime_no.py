


def prime_no(n):
    count = 0
    for i in range(1,n+1):
        if n%i ==0:
            count = count+1

    if count ==2:
        print("{} is prime no".format(n))

    else:
        print("{} is not a prime no".format(n))

k = int(input("Enter a no"))
prime_no(k)



