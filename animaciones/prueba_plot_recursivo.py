#/home/alumno/anaconda3/bin/python3
from matplotlib.pylab import *
#import time
close('all')
"""
fig, sub = subplots(2)
line1, = sub[0].plot([],[])
line2, = sub[1].plot([],[])
sub[0].axis((0,10,-1,1))
sub[1].axis((0,10,-1,1))
x = linspace(0,10,1e3)
y = []
z = []

for i in range(1000):
    y.append(sin(x[i]))
    z.append(sin(3*x[i]))
    if i%20 == 0:
        #sub[0].plot(x[:i],y[:i],'-')
        #sub[1].plot(x[:i],z[:i],'-')
        line1.set_data(x[:i],y[:i])
        line2.set_data(x[:i],z[:i])
        #sub[0].gca()
        #sub[1].gca()
        '''
        sub[0].relim()
        sub[1].relim()    
        sub[0].autoscale_view()
        sub[1].autoscale_view()
        '''
        fig.canvas.draw()
        waitforbuttonpress(0.001)
"""
a1 = array([1,1,1,1,1,1,1])
a2 = a1 + 1
a3 = a2 + 1
a4 = a3 + 1
a5 = a4 + 1
d = [a1,a2,a3,a4,a5]

fig, sub = subplots(1)
line, = sub.plot([],[])
sub.axis((0,9,-1,7))
h = 0
for i in range(5):
    line.set_data(range(len(d[i])),d[i])
    sub.relim()
    sub.autoscale_view()
    fig.canvas.draw()
    if waitforbuttonpress(10):
        h += 1
print(h)