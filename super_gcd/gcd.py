def gcd(a, b):
    if type(a) != int or type(b) != int:
        return "You're shocked!"
    while b > 0:
        r=a%b
        a=b
        b=r
        #(3,13), (13,3), (3,1)
    return a