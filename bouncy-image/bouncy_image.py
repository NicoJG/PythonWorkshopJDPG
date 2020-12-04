import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import time
from PIL import Image

# import other files of this project
from constants import *
from ball import Ball
from boundary import Boundary

# TODO: collisions are kinda weird when multiple collisions happen to one ball on one frame

# init plot
fig,ax = plt.subplots()

# init_func called before the first frame
def init_animation():
    global balls, boundary, scat
    # init balls
    balls = []
    # get image pixels
    img = Image.open(image_path)
    pix = img.load()
    # set boundaries
    boundary = Boundary(-1,img.size[0]+1,-1,img.size[1]+1)
    # init balls
    # TODO: Picture is inverted in the y direction
    for col in range(img.size[0]):
        for row in range(img.size[1]):
            # TODO: don't use white/grey/transparent pixels
            if pix[col,row][3] > 0:
                x = float(col)
                y = float(row)
                color = [rgba/255 for rgba in pix[col,row]]
                ball = Ball(x,y,color)
                balls.append(ball)
    # init plot data
    x_data = []
    y_data = []
    color_data = []
    for ball in balls:
        x_data.append(ball.x[0])
        y_data.append(ball.x[1])
        color_data.append(ball.color)
    # init plot
    # TODO: fit the marker size with the ball radius
    scat = ax.scatter(x_data, y_data, c=color_data)

    # init limits
    ax.set_xlim(boundary.l, boundary.r)
    ax.set_ylim(boundary.b, boundary.t)
    return scat,

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
            dt = current_time-last_time # in seconds
        elif current_time - starting_time <= animation_start_delay + animation_time + animation_end_delay:
            dt = 0.
        else:
            break
        yield dt

# does the animation
def update_animation(dt):
    global balls, scat
    #print("dt=",dt)
    temp_time = time.time()
    # move every ball and check the boundary collision
    for ball in balls:
        ball.move(dt)
        ball.boundary_collision(boundary)
    #print("move+boundary=",time.time()-temp_time)
    temp_time = time.time()

    balls_by_sector = Ball.sort_balls_in_sectors(balls, boundary)
    #print("balls_by_sector=",time.time()-temp_time)
    temp_time = time.time()
    # check every ball pair in every sector
    for key in balls_by_sector:
        balls_in_sector = balls_by_sector[key]
        for i in range(len(balls_in_sector)-1):
            for j in range(i+1,len(balls_in_sector)):
                Ball.ball_collision(balls_in_sector[i],balls_in_sector[j])
    #print("collisions=",time.time()-temp_time)
    temp_time = time.time()
    
    # update the visuals
    x_data = []
    y_data = []
    for ball in balls:
        x_data.append(ball.x[0])
        y_data.append(ball.x[1])
    scat.set_offsets(np.column_stack((x_data,y_data)))
    
    #print("visuals=",time.time()-temp_time)
    temp_time = time.time()
    return scat,



# animate
ani = anim.FuncAnimation(fig, update_animation, frames=calc_dt, init_func=init_animation, interval=1000/fps, blit=True)

plt.show()