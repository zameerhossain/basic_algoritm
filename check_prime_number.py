n=int(input())
flag=1
for i in range(2,n):
    if n%i==0:
        flag=0
if flag==0:
    print(n,"is not prime")
else:
    print(n,"is prime")