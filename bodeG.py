import control.matlab as c
import matplotlib.pyplot as p
G=c.tf([10],[1,6,5,0])
G2=c.tf([20],[1,6,5,0])
MG, MF, wf, wg=c.margin(G)
print(MG,MF)
c.bode(G,G2)
p.show()
