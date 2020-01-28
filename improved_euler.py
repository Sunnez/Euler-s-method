import math

print("Let's begin")


def f(x,y): #return answer of equation
    return x+y #put f(x,y) here  #math.exp(-y)

DELTA_X = 0.1  #delta x
FINAL_X = 0.3  #ultimate value of x

x=0 #initial value of x
z=0 #predictor
y=1 #initial value of y


x_db = [x]
z_db = [z]
y_db = [y]

print("Delta x =" + str(DELTA_X))
#calculation
while x < FINAL_X:
    z = y + DELTA_X*(x+y)
    y = y + DELTA_X/2*((x+y)+(z+x+DELTA_X))
    x += DELTA_X

    x_db.append(x)
    z_db.append(z)
    y_db.append(y)

print('x value:', x_db)
print('predictor:', z_db)
print('y value:',y_db)
