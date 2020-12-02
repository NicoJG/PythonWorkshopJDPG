import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import time

# import other files of this project
from ball import Ball
from boundary import Boundary

# general constants
animation_start_delay = 2 # how many seconds the animation should stand still at the beginning
animation_time = 10 # how many seconds should the animation run
animation_end_delay = 2 # how many seconds the animation should stand still at the end
fps = 60 # frames per second
n = 100 # number of balls
boundary = Boundary(-1,1,-1,1) # ball container

# init plot
fig,ax = plt.subplots()
ln = plt.plot([],[])[0]

# init_func called before the first frame
def init_animation():
    global balls
    # init balls
    balls = []
    ax.patches = []
    for i in range(n):
        x = np.random.uniform(boundary.l,boundary.r)
        y = np.random.uniform(boundary.b,boundary.t)
        ball = Ball(x,y,(np.random.rand(),np.random.rand(),np.random.rand()))
        balls.append(ball)
        ax.add_patch(ball.artist)

    # init limits
    ax.set_xlim(boundary.l, boundary.r)
    ax.set_ylim(boundary.b, boundary.t)
    return ax.patches

# generator function for each frames delta time
def calc_dt():
    starting_time = time.time()
    current_time = starting_time-1/fps
    while True:
        last_time = current_time
        current_time = time.time()
        if current_time - starting_time <= animation_start_delay:
            dt = 0.
        elif current_time - starting_time <= animation_start_delay + animation_time:
            dt = time.time()-last_time # in seconds
        elif current_time - starting_time <= animation_start_delay + animation_time + animation_end_delay:
            dt = 0.
        else:
            break
        yield dt

# does the animation
def update_animation(dt):
    global balls

    # move every ball and check the boundary collision
    for ball in balls:
        ball.move(dt)
        ball.boundary_collision(boundary)
    
    # check every ball pair for a collision
    for i in range(len(balls)-1):
        for j in range(i+1,len(balls)):
            # TODO: check if balls are in the same part of space rather than check every pair
            Ball.ball_collision(balls[i],balls[j])
    
    # update the visuals
    for ball in balls:
        ball.update_artist()

    return ax.patches

ani = anim.FuncAnimation(fig, update_animation, frames=calc_dt, init_func=init_animation, interval=1000/fps, blit=True)

plt.show()