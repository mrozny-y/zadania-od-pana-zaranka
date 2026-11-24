n=int(input("podaj n"))
i = 1
fact = 1

if n < 0:
    print(f"there is no factiral of  negative number")
else:
    while i <= n:
          fact = fact * i
          i+=1
    print(f"factorial of {n} is {fact}")
    
