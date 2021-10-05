def cmmdc(x, y) :
    while x != y:
        if x > y :
            x = x- y
        else :
            y = y -x
    return x
def cmmmmc(x,y) :
    return (x*y)/cmmdc(x,y)

def get_cmmmc(list) :
    n=len(list)
    c=cmmmmc(list[0],list[1])
    for i in range(3,n):
        Cm=cmmmmc(c,list[i-1])

    return c

def test():
    assert get_cmmmc([5, 10, 15])==30

test()


