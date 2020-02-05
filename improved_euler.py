import math

print("Let's begin")

#--- You need to change the number from here ---
def f(x,y): #return answer of equation
    return 4*x-3*y+3 #CHANGE: put a function f(x,y) here  #type "math.exp(-y)" instead of e**(-y)

DELTA_X = 0.1  #CHANGE: delta x
FINAL_X = 1.5  #CHANGE: final value of x

x=1 #CHANGE: nitial value of x
y=6 #CHANGE: initial value of y
z=0 #predictor

#--- until here -----------------------------


x_db = [x]
z_db = [z]
y_db = [y]

print("Delta x =" + str(DELTA_X))
#calculation
while round(x,3) < FINAL_X:
    z = y + DELTA_X*(f(x,y))
    y = y + DELTA_X/2*(f(x,y)+f(x+DELTA_X,z))
    x += DELTA_X

    x_db.append(x)
    z_db.append(z)
    y_db.append(y)

print('x value:', x_db)
print('predictor:', z_db)
print('y value:',y_db)
