import cmath

a=1
b=2
c=3

x1=int
x2=int
D=b**2-4*a*c
if D>=0:
    r1 = (-b - cmath.sqrt(D)) / (2 * a)
    r2 = (-b + cmath.sqrt(D)) / (2 * a)
    print("Roots are {} and {}".format(r1,r2))
else:
    rp=b/(2*a)
    ip=cmath.sqrt(-D)/(2*a)
    print("Roots are {}+j{} and {}-j{}".format(rp,ip,rp,ip))