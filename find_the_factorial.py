print("Enter a number")
n=int(input())
factorial=1
for i in range(1,n):
    factorial=factorial*i
print("factorail of {} is ={}".format(n,factorial))
