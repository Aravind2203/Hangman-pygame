import os
import pygame
import random
words=["FEBRUARY","GAURDING","JULY","PYTHON","JAVA","JUNE","OVERFLOW","EUPHORIA","DOLBY","DJANGO","TENSORFLOW","TESLA","MENTOR","DEVELOPER","FLUTTER","ANDROID","EDUCATION"]
from pygame.locals import *
pygame.init()
win=pygame.display.set_mode((800,500))
pygame.display.set_caption("HANG-MAN")
run=True
font=pygame.font.Font('freesansbold.ttf',30)
font2=pygame.font.Font('freesansbold.ttf',50)
head=font.render("HANG-MAN",True,(0,0,0))
image=pygame.image.load(os.path.join("images",'hangman0.png'))
image1=pygame.image.load(os.path.join("images","hangman1.png"))
image2=pygame.image.load(os.path.join("images","hangman2.png"))
image3=pygame.image.load(os.path.join("images","hangman3.png"))
image4=pygame.image.load(os.path.join("images","hangman4.png"))
image5=pygame.image.load(os.path.join("images","hangman5.png"))
image6=pygame.image.load(os.path.join("images","hangman6.png"))
solveimage=pygame.image.load(os.path.join("images","problem-solving.png"))
word=random.choice(words)
set_word=set(word)
guess=[]
chance=6
grey=(211,211,211)
black=(0,0,0)
red=(255,0,0)
def draw_keys():
    row_x=0
    col_y=300
    asci=65
    for row in range(0,2):
        for col in range(0,13):
            pygame.draw.rect(win,grey,(row_x,col_y,50,50))
            text=font.render(chr(asci),True,black)
            win.blit(text,(row_x+15,col_y+15))
            row_x+=62
            asci+=1
        row_x=0
        col_y+=65
def draw_man(chance):
    pygame.draw.rect(win,grey,(10,10,300,250))
    win.blit(image,(10,10))
    if chance==5:
        win.blit(image1,(10,10))
    if chance==4:
        win.blit(image2,(10,10))
    if chance==3:
        win.blit(image3,(10,10))
    if chance==2:
        win.blit(image4,(10,10))
    if chance==1:
        win.blit(image5,(10,10))
    if chance==0:
        win.blit(image6,(10,10))
        text2=font2.render("HANG-MAN!you lost the game.",True,(0,0,0))
        win.blit(text2,(10,300))
    if len(guess)==len(set_word):
        text3=font2.render("Congrats!you won the game",True,(0,0,0))
        win.blit(text3,(10,300))
def draw_line(word):
    x=420
    y=170
    for i in word:
        if i in guess:
            script=font.render(i,True,black)
            win.blit(script,(x,y-10))
        else:
            pygame.draw.rect(win,black,(x,y,30,2))
        x+=40
def clicked(char):
    global chance
    global guess

    if char=="s":
        if len(guess)==len(set_word):
            pass
        else:
            guess.extend( [chr(x) for x in range(65,91)])
    elif char in word:
        if char not in guess:
            guess.append(char)
            print(guess)
        else:
            pass
    else:
        if chance>0:
            chance-=1
        else:
            pass

def check_pos(pos):
    if 50>pos[0]>0 and 350>pos[1]>300:
        print("A is clicked")
        clicked("A")
    elif 112>pos[0]>62 and 350>pos[1]>300:
        print("B is clicked")
        clicked("B")
    elif 174>pos[0]>124 and 350>pos[1]>300:
        print("C is clicked")
        clicked("C")
    elif 236>pos[0]>186 and 350>pos[1]>300:
        print("D is clicked")
        clicked("D")
    elif 298>pos[0]>248 and 350>pos[1]>300:
        print("E is clicked")
        clicked("E")
    elif 360>pos[0]>310 and 350>pos[1]>300:
        print("F is clicked")
        clicked("F")
    elif 422>pos[0]>372 and 350>pos[1]>300:
        print("G is clicked")
        clicked("G")
    elif 484>pos[0]>434 and 350>pos[1]>300:
        print("H is clicked")
        clicked("H")
    elif 546>pos[0]>496 and 350>pos[1]>300:
        print("I is clicked")
        clicked("I")
    elif 608>pos[0]>558 and 350>pos[1]>300:
        print("J is clicked")
        clicked("J")
    elif 670>pos[0]>620 and 350>pos[1]>300:
        print("K is clicked")
        clicked("K")
    elif 732>pos[0]>682 and 350>pos[1]>300:
        print("L is clicked")
        clicked("L")
    elif 794>pos[0]>744 and 350>pos[1]>300:
        print("M is clicked")
        clicked("M")
    ##-------------------##
    #second line
    ##---------------------##
    if 50>pos[0]>0 and 410>pos[1]>365:
        print("N is clicked")
        clicked("N")
    elif 112>pos[0]>62 and 415>pos[1]>365:
        print("O is clicked")
        clicked("O")
    elif 174>pos[0]>124 and 415>pos[1]>365:
        print("P is clicked")
        clicked("P")
    elif 236>pos[0]>186 and 415>pos[1]>365:
        print("Q is clicked")
        clicked("Q")
    elif 298>pos[0]>248 and 415>pos[1]>365:
        print("R is clicked")
        clicked("R")
    elif 360>pos[0]>310 and 415>pos[1]>365:
        print("S is clicked")
        clicked("S")
    elif 422>pos[0]>372 and 415>pos[1]>365:
        print("T is clicked")
        clicked("T")
    elif 484>pos[0]>434 and 415>pos[1]>365:
        print("U is clicked")
        clicked("U")
    elif 546>pos[0]>496 and 415>pos[1]>365:
        print("V is clicked")
        clicked("V")
    elif 608>pos[0]>558 and 415>pos[1]>365:
        print("W is clicked")
        clicked("W")
    elif 670>pos[0]>620 and 415>pos[1]>365:
        print("X is clicked")
        clicked("X")
    elif 732>pos[0]>682 and 415>pos[1]>365:
        print("Y is clicked")
        clicked("Y")
    elif 794>pos[0]>744 and 415>pos[1]>365:
        print("Z is clicked")
        clicked("Z")
    elif 720>pos[0]>655 and 500>pos[1]>430:
        print("you opted to solve the game")
        clicked("s")
white=(255,255,255)
while run:
    win.fill(red)
    draw_keys()
    draw_man(chance)
    pygame.draw.rect(win,(255,255,255),(420,10,300,55))
    win.blit(head,(470,20))
    pygame.draw.rect(win,white,(655,432,70,70))
    win.blit(solveimage,(655,432))
    #win.blit(text,(500,90))
    draw_line(word)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
           # print(pos)
            check_pos(pos)
    pygame.display.update()
    if len(guess)==len(set_word):
        black=red
        grey=red
        white=red
        
    if chance==0:
        black=red
        grey=red
        white=red

pygame.quit()
