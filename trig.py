# Trigonometry Practice
import math
import matplotlib.pyplot as plt
import os
os.system('cls')
x_values=[]
for i in range(-100,101):
    x_values.append(i*2*math.pi/100)
y_sin=[]
y_cosin=[]
y_superposition=[]
for x in x_values:
    y_sin.append(2*math.sin(x))
    y_cosin.append(math.cos(3*x))
for i in range(len(y_sin)):    
    y_superposition.append(y_sin[i]+y_cosin[i])

plt.plot(x_values,y_sin,color='green')
plt.xlabel("Radian")
#plt.ylabel("Sine")
plt.plot(x_values,y_cosin,color='red')
plt.plot(x_values,y_superposition)
#plt.xlabel("Radian")
#plt.ylabel("Cosine")
plt.legend() # This displays the label box
plt.show()
