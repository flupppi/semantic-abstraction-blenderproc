
def f1(x,y):
    z = 0
    while (x > y):
        x = (x + 2)
        y = (y + 3)
        z = (z + 1)
    return z

f1(5,2)
f1(3,0)
f1(3,5)

def f2(x):
    while (x>1):
        z = x
        x = 0 
        while (z>1):
            z = (z - 2)
            x = (x + 1)
        if (z>0):
            x = ((x + x) + x)
            x = ((x + x) + 4)
        # print(x)
    return 0

f2(27)
