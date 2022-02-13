from tkinter import *
import pygame
import time
from PIL import ImageTk,Image
import os

path=os.getcwd()
os.chdir(path)

bg=pygame.image.load('airport.png')
p=pygame.image.load('k3.png')
pr=pygame.image.load('k3r.png')
m=pygame.image.load('pok.PNG')
b=pygame.image.load('b.png')
pt=pygame.image.load('kt.png')
bl=pygame.image.load('blast.png')
f1=pygame.image.load('f1.png')
f2=pygame.image.load('f2.png')
bf=pygame.image.load('bf.png')

def drop():
    global bx
    global by
    global x
    global y
    global drop_count
    global i
    drop_count+=1
    bx=x+15
    by=y+50
    t=0
    while by<=331:
        pygame.time.delay(100)
        x-=speed
        pw.blit(m,(0,0))
        pw.blit(p,(x,y))
        try:
            for i in range(1,drop_count+1):
                pw.blit(f2,(fcount[i]))
        except:
            pass
        bx-=(speed*2)
        by+=12*t
        pw.blit(b,(bx,by))
        pw.blit(p,(x,y))
        t+=1
        pygame.display.update()
    pw.blit(bl,(bx,by))
    
    fcount.update({drop_count:(bx,by)})

def back():
    global won
    global x
    global y
    global i
    global speed
    global fcount
    global drop_count
    global i
    global w2
    
    pw.blit(m,(0,0))
    
    pw.blit(pr,(x,y))
    while x<=1580:
        x+=10
        pw.blit(m,(0,0))
        pw.blit(pr,(x,y))
        if won==True:
            pw.blit(bf,(107,402))
        try:
            for i in range(1,drop_count+1):
                pw.blit(f2,(fcount[i]))
        except:
            pass
        pygame.display.update()
    pygame.quit()

    w2=Tk()
    w2.configure(bg='black')
    w2.title('Status')
    if won==True:
        Label(w2,text='Mission Accomplished.You Won!!!',bg='black',fg='green',font=('comic sans ms',30,'bold')).pack()
        Label(w2,text='You completed the mission in '+str(drop_count)+' drop(s).',bg='black',fg='white',font=('df gothic eb',30,'bold')).pack()
    else:
        Label(w2,text='Mission Failed.You Lost!!!',bg='black',fg='red',font=('comic sans ms',30,'bold')).pack()
        Label(w2,text='You did '+str(drop_count)+' drop(s).',bg='black',fg='white',font=('df gothic eb',30,'bold')).pack()
    Button(w2,text='Play Again',bg='black',fg='yellow',font=('mistral',20,'bold'),command=play).pack()  
    w2.mainloop()
        
def st():
    hs=speed*60                                                         #converting pixel speed to knots
    t=round((800)**(1/2),3)                                             #calculating time by root of 2h/g (h = 4 km)
    hd=round((hs/1.944)*t,3)                                            #calculating dist by dist = speed x time
    
    stats=Tk()
    stats.title('Statistics')
    stats.configure(bg='black')
    Label(stats,text='Current Statistics',font=('cooper black',40,'underline'),bg='black',fg='white').pack()
    Label(stats,text='',bg='black').pack()
    Label(stats,text='Horizontal Velocity: '+str(hs)+' knots',font=('microsoft yi baiti',30,'bold'),bg='black',fg='white').pack()
    Label(stats,text='Time for payload to touch ground if released: '+str(t)+' seconds',font=('microsoft yi baiti',30,'bold'),bg='blacK',fg='white').pack()
    Label(stats,text='Horizontal Distance covered by payload if released: '+str(hd)+' metres',font=('microsoft yi baiti',30,'bold'),bg='blacK',fg='white').pack()
    Label(stats,text='',bg='black').pack()
    Button(stats,text='OK',font=('modern',20),command=lambda :stats.destroy()).pack()
    stats.mainloop()


def pok():
    global won
    global x
    global y
    global bx
    global by
    global pw
    global speed
    global drop_count
    global fcount
    global i

    controls.destroy()
    pygame.init()
    pw=pygame.display.set_mode((1564,688))
    pygame.display.set_caption('Airstrike')

    drop_count=0
    fcount=dict()
    speed=5
    x=1400
    y=100
    
    playing=True
    won=False
    while playing:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                playing=False
        pw.blit(m,(0,0))

        keys=pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            speed+=3
        if keys[pygame.K_RIGHT] and speed>=5:
            speed-=3
        if keys[pygame.K_SPACE]:
            drop()
        if keys[pygame.K_BACKSPACE]:
            back()
            break
        if keys[pygame.K_s]:
            st()
        x-=speed
        pw.blit(p,(x,y))

        if x<105:
            back()
            break
        
        for i in range(1,drop_count+1):
            pw.blit(f1,fcount[i])

        try:
            if bx>=106 and bx<=145 and by==402:
                pw.blit(bf,(107,402))
                won=True
        except:
            pass
        
        pygame.display.update()
        
    pygame.quit()
    

def contr():
    pygame.quit()
    global controls
    controls=Tk()
    controls.title('Controls')
    controls.configure(bg='black')
    Label(controls,text='Controls',font=('dfpop1-w9',35,'bold','underline'),bg='black',fg='yellow').pack()
    Label(controls,text='',bg='black').pack()
    Label(controls,text='',bg='black').pack()
    Label(controls,text='Press Left arrow key to increase speed.',bg='black',fg='white',font=('cooper std black',20)).pack()
    Label(controls,text='',bg='black').pack()
    Label(controls,text='Press Right arrow key to decrease speed.',bg='black',fg='white',font=('cooper std black',20)).pack()
    Label(controls,text='',bg='black').pack()
    Label(controls,text='Press Space Bar key to drop payload.',bg='black',fg='white',font=('cooper std black',20)).pack()
    Label(controls,text='',bg='black').pack()
    Label(controls,text='Press Backspace key to return to airbase.',bg='black',fg='white',font=('cooper std black',20)).pack()
    Label(controls,text='',bg='black').pack()
    Label(controls,text="Press 'S' key to see Current Statistics.",bg='black',fg='white',font=('cooper std black',20)).pack()
    Label(controls,text='',bg='black').pack()
    Label(controls,text='---YOU ARE NOT ALLOWED TO CROSS THE BORDER(RED LINE)---',fg='red',font=('courier',25,'bold','underline'),bg='black').pack()
    Label(controls,text='',bg='black').pack()
    Button(controls,text='GO',font=('Ravie',20),command=pok).pack()
    
    controls.mainloop()

def takeoff():
    global x
    global win

    for event in pygame.event.get():
        if event.type==pygame.QUIT():
            pygame.quit()
    while x>=280:
        x-=1
        win.blit(p,(x,470))
        pygame.display.update()
    y=470

    while x>=-200:
        x-=7
        y-=7
        win.blit(bg,(0,0))
        win.blit(pt,(x,y))
        pygame.display.update()
    contr()
    
        
def redraw():
    win.blit(bg,(0,0))
    global x
    x=1410
    win.blit(p,(1410,470))
    pygame.display.update()

def play():
    global x
    global i
    global win
    global w2
    global d
    try:
        d.destroy()
    except:
        pass
    try:
        root.destroy()
    except:
        pass
    try:
        w2.destroy()
    except:
        pass
    pygame.init()
    pygame.font.init()
    myfont=pygame.font.SysFont('comic sans ms',30)
    ts=myfont.render('Hit the Space Bar to Start Game',False,(0,0,0))
    win=pygame.display.set_mode((1564,688))
    pygame.display.set_caption('Airstrike')
            
    close=False
    i=False
    
    while close==False:
        
        win.blit(ts,(500,0))
            
        pygame.time.delay(100)
                
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True
                
        keys=pygame.key.get_pressed()
                        
        if keys[pygame.K_SPACE]:
            takeoff()
            break
                
        pygame.display.update()    
        redraw()
                
    pygame.quit()
        
def describe():
    global d
    root.destroy()
    d=Tk()
    d.title('Airstrike')
    d.configure(bg='Black')
    Label(d,text='MISSION',font=('dfpop1-w9',50,'bold'),bg='black',fg='yellow').pack()
    Label(d,text='',bg='black').pack()
    Label(d,text='The Intelligence has detected terrorists launch pads in POK.',bg='black',fg='white',font=('cooper std black',20)).pack()
    Label(d,text='Your mission should you choose to accept it is to destroy them...',bg='black',fg='white',font=('cooper std black',20)).pack()
    Label(d,text='',bg='black').pack()
    Button(d,text='Accept Mission',command=play).pack()
    Label(d,text='',bg='black').pack()
    Label(d,text='',bg='black').pack()
    Label(d,text='Objective',font=('dfpop1-w9',35,'bold'),bg='black',fg='yellow').pack()
    Label(d,text='',bg='black').pack()
    Label(d,text='Physics project TO SHOW APPLICATION OF PROJECTILE MOTION in real life.',bg='black',fg='red',font=('cooper std black',20)).pack()
    Label(d,text='Military Airplanes use projectile motion to attack enemies.',bg='black',fg='white',font=('cooper std black',20)).pack()
    Label(d,text='',bg='black').pack()
    Label(d,text='',bg='black').pack()
            
root=Tk()
root.title('Airstrike')
root.state('zoomed')
cv=Canvas(root,width=2000,height=2000)
cv.pack()
img=ImageTk.PhotoImage(Image.open('wallpaper.jpg'))
cv.create_image(0,0,anchor=NW,image=img)
Label(cv,text='Airstrike',font=('bauhaus 93',70),fg='red',bg='sky blue').place(relx=0.37,rely=0.05)
Label(cv,text='Developed by Gautam Mehta',font=('copperplate gothic light',20)).place(relx=0.7,rely=0.9)
Button(cv,text='Play',font=('cooper black',20),bg='cyan',command=describe).place(relx=0.45,rely=0.45)

root.mainloop()
