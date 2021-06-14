# To check whether a given number is even or odd

for i in range(2,10):
    if i%2 == 0:
        print (i,'even number')
    else:
        print (i, 'odd number')

# To print fibonaci series
n0=1
print n0
n1=1
print n1
val  = n0+n1
for i in range(2,10):
   print val
   n0=n1
   n1=val
   val = n0+n1


print " another way to print fibonacci using function"

def fibn(n):
     x=0
     y=1
     while x < n:
         print x
         x,y=y,x+y # if we do this step in two lines, we will not get fib series
         #y= x+y
     

fibn(100)
print;
print "range function range(3,33,3)"
for i in range(3,33,3):
    print i


print "using array, range and len function"

a = ['complete' ,'surrender','prerequisite','for','spiritual','journey']

for i in range(len(a)):
    print(i,a[i])
    
         

