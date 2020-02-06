import math

print("Let's begin")


def f(x,y): #return answer of equation
    return (x+y-1)**2 #put f(x,y) here  #math.exp(-y)

DELTA_X = 0.1  #delta x
FINAL_X = 0.5  #ultimate value of x

x=0 #initial value of x
y=2 #initial value of y

x_db = [x]
y_db = [y]

print("Delta x =" + str(DELTA_X))
#calculation
while x < FINAL_X:
    k1 = f(x,y)
    k2 = f(x + DELTA_X/2, y + DELTA_X/2*k1)
    k3 = f(x + DELTA_X/2, y + DELTA_X/2*k2)
    k4 = f(x + DELTA_X, y + DELTA_X * k3)

    y += DELTA_X/6*(k1 + 2*k2 + 2*k3 + k4)
    x += DELTA_X

    y_db.append(round(y,5))
    x_db.append(round(x,5))

print(x_db)
print(y_db)
