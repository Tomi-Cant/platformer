# By: Tomi Banjoko
# Date: 2024-01-08
# Program Details: A platformer  with multiple levels moving platforms and spikes that kill the player
import manager, sys, random
from PySide6.QtGui import QPixmap 
from PySide6.QtCore import Qt, QTimer, QRect
from PySide6.QtWidgets import QLabel 
from gui.page_1_ui import Ui_MainWindow as world1
from pygame import mixer


class MainWindow(manager.QMainWindow, world1):
    first=True
    space=12
    moveX=0
    opacity= 35
    timer= QTimer()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.function_x=-6.1
        self.screen_size= self.size()
        self.j_count=0
        self.lbl_dead.setVisible(False)
        self.stopped=False
        self.timer.timeout.connect(self.movement)
        self.platforms=[]
        self.vert_p=[]
        self.moving_p=[]
        self.speed=[]
        self.hori_p=[]
        mixer.init()
        mixer.music.load("success-fanfare-trumpets-6185.mp3")
        self.lbl_winner.setVisible(False)
        self.kill=[]
        self.dead=False
        r_int=random.randrange(1,2)
        for p in self.findChildren(QLabel):
            if p.objectName().startswith("lbl_plat"):
                self.platforms.append(p)
            
            if p.objectName().startswith("lbl_platv"):
                self.vert_p.append(p)
                self.moving_p.append(p)
            if p.objectName().startswith("lbl_plath"):
                self.hori_p.append(p)
                self.moving_p.append(p)
            if  p.objectName().startswith("lbl_platk"):
                self.kill.append(p)
        for p in self.moving_p :
            self.speed.append(r_int)
        
        self.py=self.lbl_player.y()
        self.start_pos= self.lbl_player.pos()
        self.floor=self.lbl_plat
        self.lbl_player.move(self.lbl_player.x(),self.floor.y()-self.lbl_player.height()-1)
        self.lbl_winner.setVisible(False)
        self.setStyleSheet("border-image: url(\"images/sky.jpg\") 0 0 0 0 stretch stretch;")
    def movement(self):
        if self.collison(self.lbl_player,self.lbl_win):
            mixer.music.set_volume(12)
            mixer.music.play()
            self.timer.stop()
            self.pause()
            self.lbl_winner.setVisible(True)
        for p in self.kill:
            if self.collison(self.lbl_player,p) and not self.dead:
               self.dead=True
               self.lbl_player.setVisible(False)
               QTimer.singleShot(20, lambda:self.died())
        for n,p in enumerate(self.moving_p):
            for i in self.platforms:
                if p in self.hori_p:
                    p.move(p.x()+self.speed[n],p.y())
                if p in self.vert_p:
                    p.move(p.x(),p.y()+self.speed[n])
                if self.collison(p,i) and p!=i or p.x()+p.width() >= 1595 or p.x()<=0 or p.y()+p.height() >= 1000 or p.y()<=0:
                    self.speed[n]= -self.speed[n]
        else:
            if self.lbl_player.y() > 800:
                QTimer.singleShot(self.space, lambda:self.died())
                self.lbl_player.setVisible(False)
                self.lbl_player.move(self.start_pos)
                self.j_count=0 
            #walking off the side
            if self.j_count!=0:
                pass
             
            elif self.collison(self.lbl_player, self.floor)and abs(self.lbl_player.y()+self.lbl_player.height()-self.floor.y() >10):
                self.lbl_player.move(self.lbl_player.x(),self.floor.y()-self.lbl_player.height())
                
            elif ((self.floor.x()>self.lbl_player.x()+self.lbl_player.width() or self.lbl_player.x()>self.floor.x()+self.floor.width())
            or self.lbl_player.y()>= self.floor.y() and self.floor.x()-self.lbl_player.width()<=self.lbl_player.x()<self.floor.x()+self.floor.width()): 
                self.lbl_player.move(self.lbl_player.x(),self.lbl_player.y()+4)
                self.function_x=2.5
                self.jump()
                
            elif (self.floor in self.vert_p and not ((self.floor.x()>self.lbl_player.x()+self.lbl_player.width() or self.lbl_player.x()>self.floor.x()+self.floor.width()) 
                or abs(self.lbl_player.y()+self.lbl_player.height()-self.floor.y() >12) and self.floor.x()-self.lbl_player.width()<=self.lbl_player.x()<self.floor.x()+self.floor.width())):
                self.lbl_player.move(self.lbl_player.x(),self.floor.y()-self.lbl_player.height())
                
            elif (self.floor in self.hori_p and not ((self.floor.x()>self.lbl_player.x()+self.lbl_player.width() or self.lbl_player.x()>self.floor.x()+self.floor.width()) 
                or abs(self.lbl_player.y()+self.lbl_player.height()-self.floor.y() >12) and self.floor.x()-self.lbl_player.width()<=self.lbl_player.x()<self.floor.x()+self.floor.width())):   
                
                self.lbl_player.move(self.lbl_player.x()+self.speed[self.moving_p.index(self.floor)]*8.5,self.floor.y()-self.lbl_player.height())
                self.function_x=2.5
        self.lbl_player.move(self.lbl_player.x()+self.moveX,self.lbl_player.y())            
                
    def collison(self,o1,o2):
        
        return o1.geometry().intersects(o2.geometry())
    
    def keyPressEvent(self, event):
        if event.key()== Qt.Key.Key_D:
            if event.key()== Qt.Key.Key_A: #!trying to make it so the player can flip directions a little easier
                self.moveX= -self.moveX
            else:
                self.moveX=3
        if event.key()== Qt.Key.Key_A:
            if event.key()== Qt.Key.Key_D:#!
                self.moveX= -self.moveX
            else:
                self.moveX=-3
        if event.key()== Qt.Key.Key_Space:
            if self.j_count==0:
                self.start()
            elif self.j_count==1:
                self.double()
        if event.key()== Qt.Key.Key_L:
            self.home()
        
        if  event.key()== Qt.Key.Key_P and (not self.j_count or self.j_count==4) and not self.collison(self.lbl_player,self.lbl_win):
            self.pause()
                
    def keyReleaseEvent(self, event):
        if event.key()==Qt.Key.Key_D:
            self.moveX=0
        if event.key()==Qt.Key.Key_A:
            self.moveX=0
            
    def start(self):
        
        self.j_count+=1
        self.function_x=-6
        self.py=self.lbl_player.y()
        self.jump()
        
    def double(self):
        self.j_count+=1
        self.function_x=-6
        self.py=self.lbl_player.y()
   
    def jump(self):
            self.py=self.lbl_player.y()
            for p in self.platforms:
                if (self.collison(self.lbl_player,p) and (self.floor not in self.moving_p and .4<=self.function_x or self.floor in self.moving_p and -6<=self.function_x)):
                    #snaps to floor
                    QTimer.singleShot(5, lambda: self.snapping(p))
                    return False
                 
            if self.j_count!=0:
                self.calc()
                self.lbl_player.move(self.lbl_player.x(), self.py)
                return self.timer.singleShot(self.space, lambda: self.jump())

    def snapping(self,platform):
        self.floor=platform
        if (self.collison(self.lbl_player,platform) and abs(self.lbl_player.y()+self.lbl_player.height()-platform.y()) <15):
            #if lands close enough
            self.lbl_player.move(self.lbl_player.x(),platform.y()-self.lbl_player.height()-1)
            self.function_x=-6
            self.space=12
            self.py= self.lbl_player.y()
            self.j_count=0
        elif self.lbl_player.y()<= platform.y() <= self.lbl_player.y()+self.lbl_player.height() and self.lbl_player.x()-10<=platform.x()+platform.width() and self.lbl_player.x() +self.lbl_player.width()>= platform.x()+platform.width():
            #right side bounce
            self.lbl_player.move(platform.x()+platform.width(),self.lbl_player.y())
            self.moveX-=1.2*self.moveX
            self.j_count=3 
        elif ( self.lbl_player.y()<= platform.y() <= self.lbl_player.y()+self.lbl_player.height() and self.lbl_player.x() <= platform.x() and platform.x()<=self.lbl_player.x()+self.lbl_player.width()):
            #left side bounce
            self.lbl_player.move(platform.x()-self.lbl_player.width(),self.lbl_player.y()-2)
            self.moveX-=1.2*self.moveX
            self.j_count=3 
        
        else:
            #if too low
            self.lbl_player.move(self.lbl_player.x(),platform.y()+platform.height())
        self.function_x+=.1
        self.jump() 
        
    def died(self):
        
        if self.opacity<= 245:
            self.lbl_player.move(self.start_pos)
            self.lbl_dead.setVisible(True)
            self.opacity+=3
            self.lbl_dead.setStyleSheet(f"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(200, 6, 0, {self.opacity}), stop:1 rgba(200, 6, 0, {self.opacity}));\nfont: 36pt \'Matura MT Script Capitals\';")
            return QTimer.singleShot(self.space, lambda: self.died())
        else:
            self.start()
            self.lbl_player.move(self.start_pos)
            self.j_count=0
            self.lbl_player.setVisible(True)
            self.lbl_dead.setVisible(False)
            self.dead=False
            self.opacity=-1
            
    def calc(self):
        self.function_x+=.1
        if self.j_count==4:
            pass
        elif self.j_count==3:
            self.py -= (.35*((self.function_x**2)+(.8**2))) - (.4*(((self.function_x)+.8)**2))
        else:   
           self.py -= (1.2*((self.function_x**2)+(.4**2))) - ((1.2*((self.function_x-.1)+.4)**2))
            
    def pause(self):
        if self.stopped:
            self.timer.start(16)
            self.j_count=0
            self.stopped=False
        elif not self.stopped:
            self.timer.stop()
            self.j_count=4
            self.stopped=True
            
    def home(self):
            self.j_count=0
            self.timer.stop()
            self.lbl_winner.setVisible(False)
            manager.widget.setCurrentWidget(manager.start)
            manager.widget.resize(705,750)
