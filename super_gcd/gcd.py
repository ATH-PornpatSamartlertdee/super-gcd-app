def gcd(a, b):
    if type(a) != int or type(b) != int:
        return "You're shocked!"
    else:
        if a < 0:
            a = abs(a)
        if b < 0:
            b = abs(b)
        while b > 0:
            r=a%b
            a=b
            b=r
        return a