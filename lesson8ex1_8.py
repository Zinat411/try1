def hailstone(n):
    global counter
    if n == 1:
        print(n)
        counter = 1 
        return counter
    elif n % 2 == 0:
        print(n)
        hailstone(n/2)
        counter += 1
        return counter
    else:
        print(n)
        hailstone(n*3+1)
        counter += 1
        return counter
x = 0
x = hailstone(10)
print(x)
        
