# Euler-s-method
Euler's method and Improved Euler's method wrote with Python.
Your computer should be prepared to run those codes.

## Steps
### 1. Install Python
You can install the latest steable version from this link.

https://www.python.org/downloads/

### 2. Open Python IDLE


### 3. Download the code avobe and open with the IDLE

click the green botton above says "clone or download."
Download ZIP and open at your computer.

### 4. Change the codes to fit with your equation
 
Example

y' = 4x-2y^2

y(1) = 0; y(5)

h = 0.1

```
improved_euler_method.py

def f(x,y):
    return 4*x-2*y**2
    
DELTA_X = 0.1
FINAL_X = 5

x=1 #initial value of x
y=6 #initial value of y

z=0 #Don't touch this one. This is just a predictor
```
For e^(-y), type math.exp(-y). NOT e**(-y).

### 5. Save and Run the code
ctrl + S to Save, F5 to Run.
