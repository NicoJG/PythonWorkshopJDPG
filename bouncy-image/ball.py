import numpy as np
import matplotlib

from constants import *

# class for the bouncing balls
class Ball:
    def __init__(self, x, y, color):
        # position vector x
        self.x = np.array([x,y])
        self.color = color
        # create matplotlib representation
        self.artist = matplotlib.patches.Circle(xy=(self.x[0],self.x[1]), radius=r, color=self.color)
        # starting velocity
        self.v = np.array([np.random.uniform(v_min,v_max),0])
        rotate = lambda phi : np.array([ [np.cos(phi), -np.sin(phi)], [np.sin(phi),  np.cos(phi)] ])
        self.v = rotate(np.random.uniform(0,2*np.pi)).dot(self.v)
        
    def move(self, dt):
        self.x += self.v*dt

    def update_artist(self):
        self.artist.center = (self.x[0],self.x[1])
        self.artist.radius = r

    def boundary_collision(self, boundary):
        if self.x[0]-r <= boundary.l:
            self.x[0] = boundary.l + r
            self.v[0] *= -1
        elif self.x[0]+r >= boundary.r:
            self.x[0] = boundary.r - r
            self.v[0] *= -1
        if self.x[1]-r <= boundary.b:
            self.x[1] = boundary.b + r
            self.v[1] *= -1
        elif self.x[1]+r >= boundary.t:
            self.x[1] = boundary.t - r
            self.v[1] *= -1

    @staticmethod
    def ball_collision(a, b):
        if np.linalg.norm(a.x - b.x) <= 2*r :
            # do collision (assume same masses and equal radii)
            # set the positions so that they are barely touching and not overlapping
            d = a.x - b.x
            n = (1/np.linalg.norm(d))*d
            a.x = a.x - 1/2*d + r*n
            b.x = b.x + 1/2*d - r*n
            # calc the velocities
            # Wikipedia "Elastic collision"
            # v_1' = v_1 - 2*m_2/(m_1+m_2)*<v_1-v_2,x_1-x_2>/||x_1-x_2||^2 * (x_1-x_2)
            v_a_new = a.v - np.dot(a.v-b.v,a.x-b.x)/np.linalg.norm(a.x-b.x)**2 * (a.x-b.x)
            v_b_new = b.v - np.dot(b.v-a.v,b.x-a.x)/np.linalg.norm(b.x-a.x)**2 * (b.x-a.x)
            a.v = v_a_new
            b.v = v_b_new

    @staticmethod
    def sort_balls_in_sectors(balls, boundary):
        # divide the area into different sectors
        # and only check the pairs in a given sector for collisions
        # for every ball do double binary search (so always divide the sector in half)
        # number of divisions per axis:
        n_div = [0,0]
        n_div[0] = int(np.ceil(1/np.log(2)*np.log(boundary.width/sector_max_size)))
        n_div[1] = int(np.ceil(1/np.log(2)*np.log(boundary.height/sector_max_size)))
        sector_length = [0.,0.]
        sector_length[0] = 1/2**n_div[0]*boundary.width
        sector_length[1] = 1/2**n_div[1]*boundary.height
        # fill the sectors with the balls:
        balls_by_sector = {} # key is tuple of starting coords of the sector
        for ball in balls:
            keys = [[],[]] # x and y keys for this ball
            for i_x in range(2):
                # do the x or y axis
                # bounds of the currently examined part
                if i_x == 0:
                    temp_bounds = [boundary.l,boundary.r]
                else:
                    temp_bounds = [boundary.b,boundary.t]
                # check both half for n_div[i_x] divisions
                for i in range(n_div[i_x]):
                    temp_middle = (temp_bounds[1]+temp_bounds[0])/2
                    if ball.x[i_x] < temp_middle - r:
                        # ball only is in the left/lower sector
                        temp_bounds[1] = temp_middle
                    elif ball.x[i_x] > temp_middle + r:
                        # ball only is in the right/upper sector
                        temp_bounds[0] = temp_middle
                    else:
                        # ball is intersecting both areas
                        # so it must be added to both sectors next to the middle
                        keys[i_x].append(temp_middle-sector_length[i_x])
                        temp_bounds = [temp_middle,temp_middle+sector_length[i_x]]
                        break
                keys[i_x].append(temp_bounds[0])
            # add the ball to the according sector(s)
            for x in keys[0]:
                for y in keys[1]:
                    if (x,y) not in balls_by_sector:
                        balls_by_sector[(x,y)] = []
                    balls_by_sector[(x,y)].append(ball)
        return balls_by_sector
