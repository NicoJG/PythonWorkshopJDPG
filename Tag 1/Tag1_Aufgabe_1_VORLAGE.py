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

def animieren(frames):
    #Gebe hier die Änderung der Koordinaten an
    x = 0
    y = 0
    ball.set_data(x,y)

#Hier darfst du natürlich frames und interval so einstellen, wie du möchtest
anim = animation.FuncAnimation(fig, animieren,frames = 100, interval = 20)

plt.show()

#Willst du es speichern?
speichern = False
if(speichern):
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=60, bitrate=1800)
    anim.save('video.mp4', writer=writer)