total = 0
def sum(n):
    if n==0:
        return 0
    return n + sum(n-1)
    

total = sum(5)
print(total)
