import numpy as np
import matplotlib

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

    def update(self, dt, boundary):
        self.x += self.v_x*dt
        self.y += self.v_y*dt
        self.boundary_collision(boundary)

    def boundary_collision(self, boundary):
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