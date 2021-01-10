import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint
from matplotlib.figure import Figure

# Daten initialisieren
def lorenz_ableitung(xyz, t0, sigma=10., beta=8./3., rho=28.):
    x,y,z= xyz
    xpunkt = sigma*(y-x)
    ypunkt = x*(rho-z)-y
    zpunkt = x*y-beta*z

    return [xpunkt,ypunkt,zpunkt]

N = 30
x0 = -15 + 15*2*np.random.random((N,3))

t = np.linspace(0,20,10000)
x_t = np.array([odeint(lorenz_ableitung, x0[i], t) for i in range(N)])
# Figure initialisieren
fig:Figure = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim((-25,25))
ax.set_ylim((-35,35))
ax.set_zlim((5,55))

lines = [ax.plot([],[],[],'-',color=f'C{i}')[0] for i in range(N)]
points = [ax.plot([],[],[],'o',color=f'C{i}')[0] for i in range(N)]


def init():
    # for line, point in zip(lines,points):
    #     line.set_data(np.array([]),np.array([]))
    #     line.set_3d_properties([])
    #     point.set_data(np.array([]),np.array([]))
    #     point.set_3d_properties([])
    return lines + points

def animieren(frame):
    for line,point,x_i in zip(lines,points,x_t):
        x,y,z = x_i[:frame].T
        line.set_data(x,y)
        line.set_3d_properties(z)

        point.set_data(x[-1:],y[-1:])
        point.set_3d_properties(z[-1:])
    return lines+points

anim = FuncAnimation(fig, animieren, init_func=init, frames=1000, interval=20, blit=True)

plt.show()