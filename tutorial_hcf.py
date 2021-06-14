n1 = 19
n2 = 11

bool = "true"

print n1,n2

while bool == "true" :
    n3 = n1 % n2
    n1 = n2
    n2 = n3
    if n3 == 0 :
        print n1
        bool = "false"
