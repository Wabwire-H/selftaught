def square(x):
    return x*x

def fxy(f,x,y):
    return f(x) + f(y)
print(fxy(square,2,3))

x=1
y=0
def inc(x):
    y=x+1
    return y
inc(5)
print(x,y)