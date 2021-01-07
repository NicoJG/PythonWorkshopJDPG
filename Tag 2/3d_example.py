import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')



line = ax.plot([],[],[],'k-')[0]


ax.set_xlim((-4,4))
ax.set_ylim((-4,4))
ax.set_zlim((-4,4))

#Kurve
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

    
def animieren(frame):
    
    #x und y Werte hier
    line.set_data(x[:frame],y[:frame])
    
    #z Werte hier
    line.set_3d_properties(z[:frame])
    return line,
    
anim = FuncAnimation(fig, animieren, frames = 100, interval = 20, blit = True, repeat=True)


plt.show()