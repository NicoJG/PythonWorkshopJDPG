import numpy as np
class Ball:
    
    
    
    #Hier fehlen die Parameter für dei Anfangsposition und -geschwindigkeit sowie für den Radius
    def __init__(self):
        #Diese Werte müssen gleich den Parametern gesetzt werden
        self.r = 0 
        self.x = 0
        self.y = 0
    
    def bewegen(self):
        #Hier soll der sich Ball mit Geschwindigkeit bewegen und seine Position aktualisieren. 
        pass
    
    def draw(self, ax):
        #Die Axen sind durch den Parameter gegeben. Der Ball muss nur gezeichnet werden.
        pass
    
    
    def kollision(self,other):
        #Diese Methode überprüft, ob der Ball mit einem anderen kollidiert
        pos1 = np.array([self.x,self.y])
        pos2 = np.array([other.x,other.y])
        abstand = np.linalg.norm(pos1-pos2)
        
        if abstand <= (self.r + other.r):
            return True
        else:
            return False
    
    
    def elStoss(self,other):
        #Die Bälle 'self' und 'other' stoßen sich elastisch ab
        pass
    
    