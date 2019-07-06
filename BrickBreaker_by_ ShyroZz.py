#-*- coding: utf-8 -*-

from tkinter import *
from time import sleep

import random,struct,threading

def create_rect():
    rgb = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    col = "#{}".format(struct.pack('BBB',*rgb).encode('hex'))
    return can.create_rectangle(0,0,random.randint(0,200),random.randint(0,200),fill=col)

def create_ova():
    rgb = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    col = "#{}".format(struct.pack('BBB',*rgb).encode('hex'))
    return can.create_oval(0,0,random.randint(0,200),random.randint(0,200),fill=col)

def move(obj,direction,scale):
    xy = can.coords(obj)
    ec = scale

    if direction == 'haut'and xy[1] > 0:
        can.coords(obj,xy[0],xy[1]-ec,xy[2],xy[3]-ec)
    elif direction == 'bas'and xy[3] < he:
        can.coords(obj,xy[0],xy[1]+ec,xy[2],xy[3]+ec)
    elif direction == 'gauche'and xy[0] > 0:
        can.coords(obj,xy[0]-ec,xy[1],xy[2]-ec,xy[3])
    elif direction == 'droite'and xy[2] < wi:
        can.coords(obj,xy[0]+ec,xy[1],xy[2]+ec,xy[3])

    #print "{},{},{},{}".format(xy[0],xy[1],xy[2],xy[3])

def left(event):
    global direction
    direction = 'gauche'
    move(obj,direction,(wi*0.02))

def right(event):
    global direction
    direction = 'droite'
    move(obj,direction,(wi*0.02))

def space(event):
    global key
    key = 'espace'
    if len(balles) > 0:
        can.coords(balles[0].balle,0,0,0,0)
        del balles[0]

def create_balls(nb_balles):
    balls = []
    espx = wi*0.001
    taillex = wi*0.04
    tailley = he*0.04
    for i in range(nb_balles):
        y1 = he - tailley
        y2 = he
        x1 = taillex*i + espx
        x2 = x1 + taillex

        ball = balle(x1,y1,x2,y2)
        balls.append(ball)

    return balls

def create_brique(x1,y1,x2,y2):
    rgb = (random.randint(20,255),random.randint(20,255),random.randint(20,255))
    col = "#{}".format(struct.pack('BBB',*rgb).encode('hex'))
    return can.create_rectangle(x1,y1,x2,y2,fill=col)

def level_generation(width,height,lignes,briques):
    level = []

    tailley = height/20
    espy = height/100
    espx= width/100
    taillex = width/briques

    for ligne in range(lignes):
        for brique in range(briques):
            y1 = tailley*ligne + espy
            y2 = y1 + tailley - espy
            x1 = taillex*brique + espx
            x2 = x1 + taillex - espx
            level.append(create_brique(x1,y1,x2,y2))

    return level

class balle(threading.Thread):
    def __init__(self,x1,y1,x2,y2):
        threading.Thread.__init__(self)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = "red"
        self.balle = can.create_oval(self.x1,self.y1,self.x2,self.y2,fill=self.color)
        self.running = True

    def run(self):
        #while self.running:
        pass

if __name__ == "__main__":
    fen = Tk()
    global wi
    global he
    global diff
    if len(sys.argv) == 4:
        wi =  int(sys.argv[1])
        he =  int(sys.argv[2])
        diff = int(sys.argv[3])
    else:
        wi = 620
        he = 480
        diff = 1

    can = Canvas(fen, width=wi, height=he, bg='black')
    can.pack(side=TOP, padx=2, pady=2)
    espb = he*0.04
    x1= (wi/2) - (wi*0.1)
    y2= he - espb*2
    x2= (wi/2) + (wi*0.1)
    y1= y2 + espb

    try:
        global obj
        global balles
        obj = can.create_rectangle(x1,y1,x2,y2,fill="#fff")

        level_generation(wi,he,3*diff,random.randint(6,12)*diff)
        balles = create_balls(3)

        fen.bind('<d>', right)
        fen.bind('<q>', left)
        fen.bind('<space>' , space)

        fen.mainloop()
    except:
        pass
