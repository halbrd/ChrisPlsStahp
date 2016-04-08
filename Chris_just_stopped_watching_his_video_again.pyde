import random

class BouncingText:
   def __init__(self, nx, ny, nhVel):
       self.x = nx
       self.y = ny
       self.hVel = nhVel
       self.yVel = random.randint(0, 2)
       self.gravity = 1
       
   def update(self):
       self.x += self.hVel
       self.y += self.yVel
       if self.y > height: self.yVel = self.yVel * -0.9
       self.yVel += self.gravity
       if self.x > width or self.x < -300 or self.y > width + 100:
           self.x = random.randint(0, width/2)
           self.hVel = 0
           if self.x > width/4:
               self.x = width - self.x
               while self.hVel == 0:
                   self.hVel = random.randint(-15, -3)
           else:
               while self.hVel == 0:
                   self.hVel = random.randint(3, 15)
           self.y = 0
           self.yVel = random.randint(0, 2)
           
       r = random.randint(0, 255)
       g = random.randint(0, 255)
       b = random.randint(0, 255)
       fill(r, g, b);
       rect(self.x, self.y - 300, 200, 300)
       fill(255 - r, 255 - g, 255 - b)
       text("Chris just", self.x + 45, self.y - 220)
       text("stopped", self.x + 53, self.y - 195)
       text("watching", self.x + 50, self.y - 170)
       text("his video", self.x + 50, self.y - 145)
       text("again", self.x + 69, self.y - 120)
       fill(255)
   
bText = BouncingText(100, 0, 5)

def setup():
    size(1920, 960)
    background(0)
    textSize(24)

def draw():
    global bText
    bText.update()