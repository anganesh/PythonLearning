a=2
x=4
sum = 1
for i in range(2,x+1):
    n = i
    print n
    print sum
    if  n % 2 == 0:
        sum = sum - pow(a,n)
    else :
        sum = sum + pow(a,n)
print sum

