"""
Learning..
1.a function can be assigned to a variable and the variable can be used
2. keyword global helps to access the variable outside the function where it's defined
3. Variable length arguments refer to *fav_actors
"""



def diff(x,y):
    return x-y
k=30
l=22
operation=diff  # function name assigned to a variable
print(operation(k,l)) # funcation called using variable name



def loopprint():
    for i in range(4):
        print("hi")
loopprint()


var1 = "Hello"
def disp():
    global var2 # This statement makes the variable var2 global
    var2 = " r u there "
    print(var1)
disp()    
print(var2)

#variable length arguments

def func(name,*fav_actors):
    print("\n", name, " favourite actors are ")
    for actors in fav_actors:
        print(actors)

func("ganesh"  ,"kamal","rajini","ajith")
func("ashish"  ,"amitabh","amir khan")


