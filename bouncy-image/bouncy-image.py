import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import time

# class for the bouncing balls
class Ball:
    r = 0.01
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        # starting velocity
        self.v_x = np.random.uniform(0.5,2)*np.random.choice([-1,1])
        self.v_y = np.random.uniform(0.5,2)*np.random.choice([-1,1])

    def update(self, dt):
        self.x += self.v_x*dt
        self.y += self.v_y*dt
        self.boundary_collision()

    def boundary_collision(self):
        global boundary
        if self.x-self.r <= boundary.l:
            self.x = boundary.l + self.r
            self.v_x *= -1
        elif self.x+self.r >= boundary.r:
            self.x = boundary.r - self.r
            self.v_x *= -1
        if self.y-self.r <= boundary.b:
            self.y = boundary.b + self.r
            self.v_y *= -1
        elif self.y+self.r >= boundary.t:
            self.y = boundary.t - self.r
            self.v_y *= -1


# class for the boundaries in which the balls should be contained
class Boundary:
    def __init__(self, left, right, bottom, top):
        self.l = left
        self.r = right 
        self.t = top 
        self.b = bottom

# general constants
animation_time = 2 # how many seconds should the animation run
fps = 60 # frames per second
n = 5 # number of balls
boundary = Boundary(-1,1,-1,1) # ball container

# init plot
fig,ax = plt.subplots()
ln = plt.plot([],[],"o")[0]

# init_func called before the first frame
def init_animation():
    global ln,balls
    # init balls
    balls = []
    for i in range(n):
        balls.append(Ball(0,0,"blue"))

    # init limits
    ax.set_xlim(boundary.l, boundary.r)
    ax.set_ylim(boundary.b, boundary.t)
    
    return ln,

# generator function for each frames delta time
def calc_dt():
    starting_time = time.time()
    last_time = starting_time-1/fps
    while last_time-starting_time < animation_time:
        dt = time.time()-last_time # in seconds
        last_time = time.time()
        yield dt

# does the animation
def update_animation(dt):
    global ln,balls
    x_data = []
    y_data = []
    for ball in balls:
        ball.update(dt)
        x_data.append(ball.x)
        y_data.append(ball.y)
    
    ln.set_data(x_data, y_data)
    return ln,

ani = anim.FuncAnimation(fig, update_animation, frames=calc_dt, init_func=init_animation, interval=1000/fps, blit=True)

plt.show()