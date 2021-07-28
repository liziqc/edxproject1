import control as c
import matplotlib.pyplot as p
import numpy as np

G=c.tf([1.06],[1,3,2,0])

Gc=c.tf([1,0.001],[1,1.06e-4])

Glc1=G/(1+G)

Glc2=(G*Gc)/(1+G*Gc)

t=np.linspace(0,50,1000)

t,y1=c.step_response(Glc1,t)

t,y2=c.step_response(Glc2,t)

p.plot(t,y1,t,y2)

p.show()
