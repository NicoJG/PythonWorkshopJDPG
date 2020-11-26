#Aufgabe:
 
#a) Erstelle einen Kreis der sich in eine zufällige Richtung bewegt

#b) Bonus: Erstelle einen Abprallmechanismus an den Rändern des Plots

#c) Extra Bonus: Erstelle 10 Kreise, die sich in zufällige Richtungen bewegen und an den Wänden abprallen

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig = plt.figure()
lines = plt.plot([], 'o')
ball = lines[0]

plt.axis("scaled")
plt.xlim(-1,1)
plt.ylim(-1,1)

fps = 60

v_x = np.random.rand()*2-1
v_y = np.random.rand()*2-1

x = 0
y = 0

def animieren(frames):
    global x,y,v_x,v_y
    #Gebe hier die Änderung der Koordinaten an
    t = frames/fps
    x = x + v_x/fps
    y = y + v_y/fps
    if (x < -1) or (x > 1):
        v_x = -v_x
    if (y < -1) or (y > 1):
        v_y = -v_y
    
    ball.set_data(x,y)
    return ball

#Hier darfst du natürlich frames und interval so einstellen, wie du möchtest
anim = animation.FuncAnimation(fig, animieren,frames=1000, interval = 1000/fps, blit=True)

plt.show()

#Willst du es speichern?
speichern = False
if(speichern):
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=fps, bitrate=1800)
    anim.save('video.mp4', writer=writer)