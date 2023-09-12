ch = "True"
while ch=="True":
    n = int(input("Enter the n = "))
    i = 2
    while i<n:
        if n%i == 0:
            print(n, " is not prime")
            break
        i = i+1
    else:
        print(n, " is prime ")
    ch = input("Enter True to continue")