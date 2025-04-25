import turtle
import time
import random

wn = turtle.Screen()
wn.cv._rootwindow.resizable(False,False)
wn.title("Frogger")
wn.setup(width=600,height=800)
wn.bgcolor("green")
wn.tracer(0)

# spriteImageList = ["18Wheeler_Sprite.png","Frog_Sprite.png","Large_Log_Sprite.png","Lilypad_Sprite.png","Limo_Sprite.png",
#                     "Medium_Log_Sprite.png","Small_Fast_Car_Sprite.png","Small_Log_Sprite.png","Small_Slow_Car_Sprite.png",
#                     "Sunk_Turtle_sprite.png","Turtle_Sprite.png"]
spriteImageList = ["Frog_Sprite.gif","Small_Fast_Car_Sprite.gif"]
for sprite in spriteImageList:
    wn.register_shape(sprite)

#Pen setup
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

class Sprite():
    def __init__(self,x,y,width,height,img):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.img=img

    def renderImg(self,pen):
        pen.goto(self.x,self.y)
        pen.shape(self.img)
        pen.stamp()

    def update(self):
        pass
class Car(Sprite):
    SMALLSLOWCAR=0
    SMALLFASTCAR=1
    LIMO=2
    EIGHTEENWHEELER=4
    def __init__(self, x, y, width, height, img, dx,type):
        Sprite.__init__(self, x, y, width, height, img)
        self.dx = dx
        self.type=type

    def update(self):
        self.x += self.dx

        if self.x < -400:
            self.x = 400
        if self.x > 400:
            self.x = -400
class Player(Sprite):
    def __init__(self,x,y,width,height,img):
        Sprite.__init__(self,x,y,width,height,img)
        self.dx = 0
        self.collision=False
        self.frogsOnPad = 0
        self.timeLeft=60
        self.startTime = time.time()
        self.lives=3

        def up(self):
            self.y+=50
        def down(self):
            self.y += -50
        def right(self):
            self.x += 50
        def left(self):
            self.y += -50
        def update(self):
            #border checking: -325 and 300
            if self.y<-300 or self.y>300:
                self.x=0
                self.y=300
            if self.y<-325:
                self.y=-325

            self.timeLeft = 60 - round(time.time() - self.startTime)

            if self.timeLeft<=0:
                self.lives-=1

            def respawnAtStart(self):
                self.dx=0
                self.x=0
                self.y=-325
                self.timeLeft=60
                self.startTime=time.time()
            #Time update



level_1 = [
    Car(0, -275, 121, 40, "Small_Fast_Car_Sprite.gif", -0.1,1),
    Car(221, -275, 121, 40, "Small_Fast_Car_Sprite.gif", -0.1,1),

    # Car(0, -225, 121, 40, "car_right.gif", 0.1),
    # Car(221, -225, 121, 40, "car_right.gif", 0.1),
    #
    # Car(0, -175, 121, 40, "car_left.gif", -0.1),
    # Car(221, -175, 121, 40, "car_left.gif", -0.1),
    #
    # Car(0, -125, 121, 40, "car_right.gif", 0.1),
    # Car(221, -125, 121, 40, "car_right.gif", 0.1),
    #
    # Car(0, -75, 121, 40, "car_left.gif", -0.1),
    # Car(221, -75, 121, 40, "car_left.gif", -0.1),
]
player = Player(0,-325,40,40,"Frog_Sprite.gif")
sprites = level_1
sprites.append(player)

wn.listen()
wn.onkeypress(player.up,'Up')

while True:
    # Render
    for sprite in sprites:
        sprite.renderImg(pen)
        sprite.update()

    wn.update()
    pen.clear()






# Helpful links
#https://github.com/wynand1004/Projects/blob/master/Frogger/frogger.py

