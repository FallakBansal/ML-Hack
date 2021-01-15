import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

time_ =[]
value = []

def area(n):
    r=n*n

for x in range(0,1000,1):
    t0=time.time()
    area(x)
    t1 = time.time() - t0
    value.append(x)
    time_.append(t1)
    
    
plt.plot(value,time_) 
plt.xlabel('N moves from 1 - 100') 
plt.ylabel('y - axis - Time') 
plt.title('Order O(1)') 
plt.show() 

colors = np.random.rand(1000)
# area = (30 * 2)**2  # 0 to 15 point radii
plt.scatter(value, time_, c=colors, alpha=0.5)
plt.show()