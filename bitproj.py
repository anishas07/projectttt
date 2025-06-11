import string
def set(set,Setsize):
    set = (int)(str.pow(2,Setsize))
    
    for outer in range(0,set):
        for inner in range(0,set):
            if((outer &(1<<inner))>0):
                print(set[inner],end="")
        print("")
input11= input("Enter a string: ")
set(input11, len(input11))