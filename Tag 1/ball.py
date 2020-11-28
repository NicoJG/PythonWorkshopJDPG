#Aufgabe:
 
#a) Erstelle einen Kreis der sich in eine zufällige Richtung bewegt

#b) Bonus: Erstelle einen Abprallmechanismus an den Rändern des Plots

#c) Extra Bonus: Erstelle 10 Kreise, die sich in zufällige Richtungen bewegen und an den Wänden abprallen

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig,ax = plt.subplots()
lines, = plt.plot([],[], 'o')

ax.axis("scaled")
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)

fps = 60

x = 0
y = 0

v_x = np.random.choice([-1,1])*np.random.uniform(0.5,2)
v_y = np.random.choice([-1,1])*np.random.uniform(0.5,2)

def animieren(frame):
    global x,y,v_x,v_y
    #t = frame/fps
    x += v_x/fps
    y += v_y/fps
    if (x < -1) or (x > 1):
        v_x = -v_x
    if (y < -1) or (y > 1):
        v_y = -v_y
    
    lines.set_data(x,y)
    return lines,

#Hier darfst du natürlich frames und interval so einstellen, wie du möchtest
anim = animation.FuncAnimation(fig, animieren, interval = 1000/fps, blit=True)

plt.show()

#Willst du es speichern?
speichern = False
if(speichern):
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=fps, bitrate=1800)
    anim.save('video.mp4', writer=writer)