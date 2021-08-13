import random as r
import string

class Rule:
    def __init__(self,initial, final):
        self.i = initial
        self.f = final    

def nextString(current,ruleSet):
    next = ''
    for i in range(len(current)):
        for j in range(len(ruleSet)):
            if current[i] == ruleSet[j].i:
                next += ruleSet[j].f
    return next

def randomReset(axiom):
    next = ''
    for i in range(len(axiom)):
        rr = random(0,1)
        if rr > .99 and axiom[i] != '[' and axiom[i] != ']':
            next += 'X'
        else:
            next += axiom[i]
    return next

axiom = ''

def setup():
    global axiom
    size(1920,1080)
    background(0)
    r1 = Rule('A','BAC')
    r2 = Rule('B','C')
    r3 = Rule('C','-[+ACB]')
    r4 = Rule('[','B[A]C')
    r5 = Rule(']','A')
    r6 = Rule('+','ABA')
    r7 = Rule('-','ABA')
    ruleSet = [r1,r2,r3,r4,r5,r6,r7]
    axiom = 'AABC'
    #while len(axiom) <= 100:
    #    axiom = nextString(axiom,ruleSet)
    for i in range(7):
        axiom = nextString(axiom,ruleSet)
    print(axiom)
    axiom = randomReset(axiom)
    stroke(255,255,255,15)
    strokeWeight(1)
    translate(width/2,height/2)
    r = 255
    g = 50
    b = 0
    o = 20
    s = 8
    fill(r,g,b,o)
    for i in range(len(axiom)):
        fill(r,g,b,o)
        if axiom[i] == 'A':
            #line(0,0,60*cos(i*PI/180),0)
            translate(60*cos(i*PI/180),0)
            rr = random(0,10)
            if rr < 1:
                pushStyle()
                fill(r,g,b,random(20,100))
                circle(0,0,s*random(1,3))
                popStyle()
            else:
                circle(0,0,s)
        elif axiom[i] == 'B':
            line(0,0,10,0)
            translate(10,0)
            #circle(0,0,s/2)
        elif axiom[i] == 'C':
            #line(0,0,80,0)
            translate(80,0)
            circle(0,0,s*2)
        elif axiom[i] == '[':
            pushMatrix()
        elif axiom[i] == ']':
            popMatrix()
        elif axiom[i] == '+':
            rotate(random(.9,1.1)*PI/2)
        elif axiom[i] == '-':
            rotate(random(.9,1.1)*-PI/2)
        elif axiom[i] == 'X':
            resetMatrix()
            translate(width/2,height/2)
            rotate(i*PI/180)
            r = random(220,255)
            g = random(0,100)
            #circle(0,0,s)
    #noStroke()
    resetMatrix()
    translate(width/2,height/2)
    fill(100,0,255,10)
    #circle(0,0,3000)
    #circle(0,0,10)

def draw():
    x = 0
            
def mousePressed():
    niceone = randomString()
    save(niceone + ".png")
    
def randomString(stringLength=4):
    letters = string.ascii_lowercase
    return ''.join(r.choice(letters) for i in range(stringLength))
        
        
