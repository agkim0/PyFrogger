import math
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
spriteImageList = ["Frog_Sprite.gif","Small_Fast_Car_Sprite.gif","Small_Slow_Car_Sprite.gif","Limo_Sprite.gif","18Wheeler_Sprite.gif"]
for sprite in spriteImageList:
    wn.register_shape(sprite)

#Pen setup
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

wn.register_shape("Road_Tile.gif")
pen.goto(0,300)
pen.shape("Road_Tile.gif")
pen.stamp()
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

    def is_collision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)



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
            self.x += -50
    def update(self):
            #border checking: -325 and 300
            if self.y<-325 or self.y>300:
                print("y<300")
                self.x=0
                self.y=300
            if self.y<-325:
                print("y<-325")
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
    def backToStart(self):
        self.x=0
        self.y=-325


level_1 = [
    Car(0, -220, 90, 90, "Small_Fast_Car_Sprite.gif", -0.1,1),
    Car(240, -220, 90, 90, "Small_Slow_Car_Sprite.gif", -0.1,2),

    Car(-280, -130, 105, 90, "Limo_Sprite.gif", 0.1,3),
    Car(221, -130, 90, 90, "Small_Fast_Car_Sprite.gif", 0.1,1),
    Car(0, -130, 120, 90, "18Wheeler_Sprite.gif", 0.1,1),

    #
    Car(-220, -40, 120, 90, "18Wheeler_Sprite.gif", -0.2,3),
    Car(0, -40, 90, 90, "Small_Slow_Car_Sprite.gif", -0.2,1),
    Car(220, -40, 105, 90, "Limo_Sprite.gif", -0.2,3),

    Car(-280, 50, 120, 90, "18Wheeler_Sprite.gif", 0.2,3),
    Car(-120,50, 90, 90, "Small_Slow_Car_Sprite.gif", 0.2,1),
    Car(60, 50, 105, 90, "Limo_Sprite.gif", 0.2,3),
    Car(200, 50, 105, 90, "Small_Fast_Car_Sprite.gif", 0.2,3),

    # Car(0, -175, 121, 40, "car_left.gif", -0.1),
    # Car(221, -175, 121, 40, "car_left.gif", -0.1),
    #
    # Car(0, -125, 121, 40, "car_right.gif", 0.1),
    # Car(221, -125, 121, 40, "car_right.gif", 0.1),
    #
    # Car(0, -75, 121, 40, "car_left.gif", -0.1),
    # Car(221, -75, 121, 40, "car_left.gif", -0.1),
]
player = Player(0,-325,50,50,"Frog_Sprite.gif")
sprites = level_1
sprites.append(player)




while True:
    wn.listen()
    wn.onkey(player.up, "Up")
    wn.onkey(player.down, "Down")
    wn.onkey(player.right, "Right")
    wn.onkey(player.left, "Left")

    # Render
    y=-220

    while y<140:
        x = -305
        while x < 310:
            # print(f"({x},{y}")
            pen.goto(x, y)
            pen.shape("Road_Tile.gif")
            pen.stamp()
            x += 90
        y=y+90

    for sprite in sprites:
        sprite.renderImg(pen)
        sprite.update()
        if player.is_collision(sprite):
            if isinstance(sprite, Car):
                player.lives -= 1
                player.backToStart()
                break



    wn.update()
    pen.clear()






# Helpful links
#https://github.com/wynand1004/Projects/blob/master/Frogger/frogger.py

