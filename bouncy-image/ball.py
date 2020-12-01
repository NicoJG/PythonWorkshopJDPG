import numpy as np
import matplotlib

# class for the bouncing balls
class Ball:
    r = 0.01
    def __init__(self, x, y, color):
        # position vector x
        self.x = np.array([x,y])
        self.color = color
        # create matplotlib representation
        self.artist = matplotlib.patches.Circle(xy=(self.x[0],self.x[1]), radius=self.r, color=self.color)
        # starting velocity
        self.v = np.array([np.random.uniform(0.5,2),0])
        rotate = lambda phi : np.array([ [np.cos(phi), -np.sin(phi)], [np.sin(phi),  np.cos(phi)] ])
        self.v = rotate(np.random.uniform(0,2*np.pi)).dot(self.v)
        
    def move(self, dt):
        self.x += self.v*dt

    def update_artist(self):
        self.artist.center = (self.x[0],self.x[1])
        self.artist.radius = self.r

    def boundary_collision(self, boundary):
        if self.x[0]-self.r <= boundary.l:
            self.x[0] = boundary.l + self.r
            self.v[0] *= -1
        elif self.x[0]+self.r >= boundary.r:
            self.x[0] = boundary.r - self.r
            self.v[0] *= -1
        if self.x[1]-self.r <= boundary.b:
            self.x[1] = boundary.b + self.r
            self.v[1] *= -1
        elif self.x[1]+self.r >= boundary.t:
            self.x[1] = boundary.t - self.r
            self.v[1] *= -1

    @staticmethod
    def ball_collision(a, b):
        if np.linalg.norm(a.x - b.x) <= 2*a.r :
            # do collision (assume same masses and equal radii)
            # set the positions so that they are barely touching and not overlapping
            d = a.x - b.x
            n = (1/np.linalg.norm(d))*d
            a.x = a.x - 1/2*d + a.r*n
            b.x = b.x + 1/2*d - a.r*n
            # calc the velocities
            # Wikipedia "Elastic collision"
            # v_1' = v_1 - 2*m_2/(m_1+m_2)*<v_1-v_2,x_1-x_2>/||x_1-x_2||^2 * (x_1-x_2)
            a.v = a.v - np.dot(a.v-b.v,a.x-b.x)/np.linalg.norm(a.x-b.x)**2 * (a.x-b.x)
            b.v = b.v - np.dot(b.v-a.v,b.x-a.x)/np.linalg.norm(b.x-a.x)**2 * (b.x-a.x)

