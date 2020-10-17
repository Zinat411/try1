class Rational():
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def print_rational(self):
        print(repr(self.p + "/" + self.q))
    def gcd(self):
        if(self.p == 0):
            return 0
        else:
            
