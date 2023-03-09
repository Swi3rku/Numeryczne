
#na razie zakładamy że podaliśmy poprawne argumenty
def horner(x,a,l):
    result=a[0]
    for i in range(1,l):
        result=result*x+a[i]
    return result
