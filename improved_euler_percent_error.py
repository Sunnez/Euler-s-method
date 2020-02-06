import math


print("Let's begin")

#--- You need to change the number from here ---
def f(x,y): #return answer of equation
    return (x+y-1)**2 #CHANGE: put a function f(x,y) here  #type "math.exp(-y)" instead of e**(-y)

def g(x): #return actual answer. To calc %error
    return math.tan(x + math.atan(1))-x+1 #CHANGE: put F(x,y): integral of the original function f(x,y), here

DELTA_X = 0.05  #CHANGE: delta x
FINAL_X = 0.5  #CHANGE: final value of x

x=0 #CHANGE: nitial value of x
y=2 #CHANGE: initial value of y
z=0 #predictor

#--- until here -----------------------------

a=0 #dev: valiable for an Actual value
p=0 #dev: valiable for a Percent error
v=0

x_db = [x]
z_db = [z]
y_db = [y]

v_db = [v] #actual value
a_db = [a] #absolute error
p_db = [p] #% error

print("Delta x =" + str(DELTA_X))

#calculation
while round(x,5) < FINAL_X:
    z = y + DELTA_X*(f(x,y))
    y = y + DELTA_X/2*(f(x,y)+f(x+DELTA_X,z))
    x += DELTA_X

    x_db.append(round(x,5))
    z_db.append(round(z,5))
    y_db.append(round(y,5))

    v = g(x)
    a = abs(y - v)
    p = abs(a/v *100)
    v_db.append(round(v,5))
    a_db.append(round(a,5))
    p_db.append(round(p,5))

print('x value:', x_db)
print('predictor:', z_db)
print('y value:',y_db)
print('---------------------')
print('Actual Value: ', v_db)
print('absolute error', a_db)
print('percent error', p_db)
