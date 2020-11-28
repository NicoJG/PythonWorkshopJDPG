import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import time

# general constants
fps = 60

# init plot
fig,ax = plt.subplots()
ln = plt.plot([],[],'o')[0]

# init_func called before the first frame
def init_animation():
    global ln,x,y
    ax.set_xlim(-1,1)
    ax.set_ylim(-1, 1)
    x = 0
    y = 0 
    return ln,

# generator function for each frames delta time
def calc_dt():
    lastTime = time.time()-1/fps
    while True:
        dt = time.time()-lastTime # in seconds
        lastTime = time.time()
        yield dt

# does the animation
def update_animation(dt):
    global ln,x,y
    x += dt
    y += dt
    ln.set_data(x,y)
    return ln,

ani = anim.FuncAnimation(fig, update_animation, frames=calc_dt, init_func=init_animation, interval=1000/fps, blit=True)

plt.show()