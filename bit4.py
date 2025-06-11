import math
def pow_set(set,Setsize):
    pow_set = (int)(math.pow(2,Setsize))
    outer=0
    inner=0
    for outer in range(0, pow_set):
        for inner in range(0, pow_set):
            if((outer &(1<<inner))>0):
                print(set[inner],end="")
        print("")
input1 =int(input("Enter an array size:"))
set=[]
for i in range(0,input1):
    n = int(input("Enter element:"))
    set.append(n)
pow_set(set, len(set))
    
            


