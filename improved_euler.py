import math

print("Let's begin")

#--- You need to change the number from here ---
def f(x,y): #return answer of equation
    return x+y #CHANGE: put a function f(x,y) here  #type "math.exp(-y)" instead of e**(-y)

DELTA_X = 0.1  #CHANGE: delta x
FINAL_X = 0.3  #CHANGE: final value of x

x=0 #CHANGE: nitial value of x
y=1 #CHANGE: initial value of y
z=0 #predictor

#--- until here -----------------------------


x_db = [x]
z_db = [z]
y_db = [y]

print("Delta x =" + str(DELTA_X))
#calculation
while x < FINAL_X:
    z = y + DELTA_X*(f(x,y))
    y = y + DELTA_X/2*(f(x,y)+f(x,z))
    x += DELTA_X

    x_db.append(x)
    z_db.append(z)
    y_db.append(y)

print('x value:', x_db)
print('predictor:', z_db)
print('y value:',y_db)
