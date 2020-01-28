import math

print("Let's begin")


def f(x,y): #return answer of equation
    return 2*x*y #put f(x,y) here  #math.exp(-y)

def g(x): #return actual answer. To calc %error
    return math.exp(x**2-1) #put F(x,y) here

DELTA_X = 0.05  #delta x
FINAL_X = 1.5  #ultimate value of x

x=1 #initial value of x
y=1 #initial value of y
a=0
p=0

x_db = [x]
y_db = [y]
a_db = [a] #absolute error
p_db = [p] #% error

print("Delta x =" + str(DELTA_X))

#calculation
while x < FINAL_X:
    y = y + f(x,y)*DELTA_X #formula of the Euler's method
    x += DELTA_X
    y_db.append(y)
    x_db.append(x)

    a = abs(y - g(x))
    p = abs(a/g(x) *100)
    a_db.append(a)
    p_db.append(p)


print('x', x_db)
print('y', y_db)
print('absolute error', a_db)
print('percent error', p_db)
