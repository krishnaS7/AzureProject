def fibo(fib):
    fib1 = 0
    fib2 = 1
    x = 0
    if (fib == 1):
        print (1)
    elif (fib > 1):
        
        while ( x < fib):
             print(fib1,end=' , ')
             nth = fib1 + fib2
       # update values
             fib1 = fib2
             fib2 = nth
             x += 1

#num = int(input("enter a number : " ))
fibo(9)
