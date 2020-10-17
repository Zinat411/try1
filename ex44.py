def print_stars(x):
    str = ""
    for y in range(x):
        str += "*"
    print(str)

def print_triangle():
    for x in range(10):
        print_stars(x)

def print_trapeze():
    for x in range(4,10):
        print_stars(x)

print_triangle()
print_trapeze()

