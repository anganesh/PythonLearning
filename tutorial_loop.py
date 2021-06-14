# String list
months = ['january','feburary','march','april']
newmonths = []
for m in months:
    print (m, "length is " ,len(m))
    newmonths.append(m)
print newmonths


# Example for range function
# range functions print values from 0 by default

for i in range(5):
    print i
print " another range example range(3,8)"
for a in range(3,8):
    print a

print "Range example with step of 4 range (4,21,4)"

for b in range(4,21,4):
    print b


print "Example to get the indices of a list  ['hey', 'r','you','there']"
newlist = ['hey', 'r','you','there']
for i in newlist:
    print i

for i in range(len(newlist)):
    print (i,newlist[i])


print "Example for printing a range"
print range(4)
print sum(range(4))
print list(range(4))


# example for breaking from a loop
newlist = ['hey', 'r','you','there']
for i in range(len(newlist)):
    print "  List Element: ", newlist[i]
    if i == 10 :
        print "  I am going to break"
        break
    else:
        print "   I am continuning in loop"
    print "    Outside if"
print "outside for loop"


# print only odd number

for i in range(10):
    if i%2 == 1:
        print (i ,'odd')
    else:
        pass # An example for pass where no action is performed.
        

