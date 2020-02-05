import math

print("Let's begin")

#----- CHANGE FROM HERE -----
def f(x,y): #dev: return answer of equation
    return 2*x*y #CHANGE: put function here  #for the equation e^(-y), type math.exp(-y) instead.

def g(x): #return actual answer. To calc %error
    return math.exp(x**2-1) #CHANGE: put F(x,y): integral of the original function f(x,y), here

DELTA_X = 0.05  #CHANGE: delta x
FINAL_X = 1.5  #CHANGE: final value of x
x=1 #CHANGE: initial value of x
y=1 #CHANGE: initial value of y
#----- CHANGE UNTIL HERE -----

a=0 #dev: valiable for an Actual value
p=0 #dev: valiable for a Percent error

#Arrays to print at last
x_db = [x]
y_db = [y]
a_db = [a] #absolute error
p_db = [p] #% error

print("Delta x =" + str(DELTA_X))

#dev: calculation
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
