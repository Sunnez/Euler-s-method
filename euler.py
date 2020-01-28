import math

print("Let's begin")


def f(x,y): #return answer of equation
    return 2*x*y #put f(x,y) here  #math.exp(-y)

DELTA_X = 0.1  #delta x
FINAL_X = 1.5  #ultimate value of x

x=1 #initial value of x
y=1 #initial value of y

x_db = [x]
y_db = [y]

print("Delta x =" + str(DELTA_X))
#calculation
while x < FINAL_X:
    y = y + f(x,y)*DELTA_X #formula of the Euler's method
    x += DELTA_X
    y_db.append(y)
    x_db.append(x)

print(x_db)
print(y_db)
