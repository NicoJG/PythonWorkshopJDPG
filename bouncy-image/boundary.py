# class for the boundaries in which the balls should be contained
class Boundary:
    def __init__(self, left, right, bottom, top):
        self.l = left
        self.r = right 
        self.t = top 
        self.b = bottom
        self.width = abs(self.r-self.l)
        self.height = abs(self.t-self.b)