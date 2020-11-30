import numpy as np
import matplotlib

# class for the bouncing balls
class Ball:
    r = 0.02
    def __init__(self, x, y, color):
        self.pos = np.array([x,y])
        self.color = color
        # create matplotlib representation
        self.artist = matplotlib.patches.Circle(xy=(self.pos[0],self.pos[1]), radius=self.r, color=self.color)
        # starting velocity
        self.v = np.array([np.random.uniform(0.5,2),0])
        rotate = lambda phi : np.array([ [np.cos(phi), -np.sin(phi)], [np.sin(phi),  np.cos(phi)] ])
        self.v = rotate(np.random.uniform(0,2*np.pi)).dot(self.v)
        

    def update(self, dt, boundary):
        self.pos += self.v*dt
        self.boundary_collision(boundary)
        self.artist.center = (self.pos[0],self.pos[1])
        self.artist.radius = self.r

    def boundary_collision(self, boundary):
        if self.pos[0]-self.r <= boundary.l:
            self.pos[0] = boundary.l + self.r
            self.v[0] *= -1
        elif self.pos[0]+self.r >= boundary.r:
            self.pos[0] = boundary.r - self.r
            self.v[0] *= -1
        if self.pos[1]-self.r <= boundary.b:
            self.pos[1] = boundary.b + self.r
            self.v[1] *= -1
        elif self.pos[1]+self.r >= boundary.t:
            self.pos[1] = boundary.t - self.r
            self.v[1] *= -1
