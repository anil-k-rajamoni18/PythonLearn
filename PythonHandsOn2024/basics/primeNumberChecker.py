import math 

n = int(input("Enter N Value: "))

if n <= 1:
    print("Not a Prime")
else:
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            print("not a prime")
            break
    else:
        print(f"{n} is a Prime")

