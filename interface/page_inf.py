# By: Tomi Banjoko
# Date: 2024-01-08
# Program Details: A platformer  with multiple levels moving platforms and spikes that kill the player
import manager, sys, random
from PySide6.QtGui import QPixmap, QCursor,QScreen
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QLabel, QPushButton, QWidget
from gui.page_inf_ui import Ui_MainWindow as inf
from pygame import mixer


class MainWindow(manager.QMainWindow, inf):
    first=True
    space=16
    moveX=0
    moveY=0
    double_jump=False
    opacity= 35
    follow_mouse=False
    timer= QTimer()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.function_x=-6.1
        self.screen_size= self.size()
        self.j_count=0
        self.lbl_dead.setVisible(False)
        self.stopped=True
        self.timer.timeout.connect(self.movement)
        self.current=self.lbl_plat_3
        self.platforms=[self.lbl_plat]
        self.vert_p=[]
        self.moving_p=[]
        self.speed=[]
        self.hori_p=[]
        self.kill=[]     
        self.winner=[]   
        self.mouse_active= False
        self.curr_num=0
        self.master_list=[self.platforms,self.vert_p,self.moving_p,self.speed,self.hori_p,self.kill,self.winner]
        self.lbl_winner.setVisible(False)
        mixer.init()
        mixer.music.load("success-fanfare-trumpets-6185.mp3")
        self.py=self.lbl_player.y()
        self.start_pos= self.lbl_player.pos()
        self.floor=self.lbl_plat
        self.lbl_winner.setVisible(False)
        self.img_win=    (u"images/flagpole.png")
        self.img_spikeu= (u"images/spikes_u.png")
        self.img_spiked= (u"images/spikes_d.png")
        self.img_spiker= (u"images/spikes_r.png")
        self.img_spikel= (u"images/spikes_l.png")
        self.img_floor=  (u"images/floor.png")
        self.img_ffloor= (u"images/fake_floor.png")
        self.img_moving= (u"images/moving_platform.png")
        self.img_movingr=(u"images/moving_platform_r.png")
        self.type_list=[self.lbl_win_2, self.lbl_platk,self.lbl_plat_2,self.lbl_fplat,self.lbl_plath,self.lbl_platv]
        self.btn_list=[self.btn_piece,self.btn_piece_2,self.btn_piece_3,self.btn_piece_4,self.btn_piece_5,self.btn_piece_6]
        self.pmaps=[self.img_win,self.img_spikeu,self.img_floor,self.img_ffloor,self.img_moving,self.img_moving]
        self.added=[self.lbl_plat_3]
        
    def pick_type(self):
        btn= self.sender()
        type=QLabel(self.centralwidget)
        if self.btn_list.index(btn)==0:
            type.setObjectName("lbl_win")
        else:    
            type.setObjectName(f"{str(self.type_list[self.btn_list.index(btn)].objectName())+'_'+str(len(self.added))}")
        type.setPixmap(QPixmap(self.pmaps[self.btn_list.index(btn)]))
        type.setVisible(True)
        if self.pmaps[self.btn_list.index(btn)]== self.img_moving:
            type.setScaledContents(True)
        type.resize(self.type_list[self.btn_list.index(btn)].size())
        y=random.randint(1,self.height()-50)
        x= random.randint(1, self.width()-50)
        self.added.append(type)
        type.move(x,y)
        self.current= type
        self.curr_sel.setGeometry(type.x()-2,type.y()-2,type.width()+4,type.height()+4)
        manager.wip.setFocus()
        self.curr_sel.setVisible(True)
        if self.mouse_active:
            self.follow_mouse=True
        
    def movement(self):
        if self.mouse_active:
            self.mousemove()
        if not self.red.isVisible():  
            for i in self.winner:   
                if self.collison(self.lbl_player,i):
                    mixer.music.set_volume(12)
                    mixer.music.play()
                    self.timer.stop()
                    self.pause()
                    self.lbl_winner.raise_()
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
                    if self.collison(p,i) and p!=i or p.x()+p.width() >= 1595 or p.x()<=0 or p.y()+p.height() >= 800 or p.y()<=0:
                        self.speed[n]= -self.speed[n]
            else:
                if self.lbl_player.y() > 900:
                    self.lbl_player.setVisible(False)
                    QTimer.singleShot(self.space, lambda:self.died())
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
    
    
    def mousemove(self):  
        if self.follow_mouse:  
            self.current.move(QWidget().mapFromGlobal(QCursor.pos()))
            self.curr_sel.move(QWidget().mapFromGlobal(QCursor.pos()))
            self.curr_sel.move(self.curr_sel.x()-2,self.curr_sel.y()-2)
            
    def place_current(self):    
        if self.follow_mouse:
            self.follow_mouse=False
        elif not self.follow_mouse:
            self.follow_mouse=True
            
    def keyPressEvent(self, event):
        manager.wip.setFocus()
        if self.red.isVisible():
            
            if event.key()== Qt.Key.Key_D:
                self.moveX=5
            if event.key()== Qt.Key.Key_A:
                self.moveX=-5
            if event.key()== Qt.Key.Key_S:
                self.moveY=5
            if event.key()== Qt.Key.Key_W:
                self.moveY=-5
            if event.key()== Qt.Key.Key_Right:
                self.moveX=1
            if event.key()== Qt.Key.Key_Left:
                self.moveX=-1
            if event.key()== Qt.Key.Key_Down:
                self.moveY=1
            if event.key()== Qt.Key.Key_Up:
                self.moveY=-1
            if event.key()== Qt.Key.Key_Q:
               if len(self.added):
                if self.curr_num>0: 
                    self.curr_num-=1
                else:
                    self.curr_num=len(self.added)-1
                self.current= self.added[self.curr_num]
                self.curr_sel.setGeometry(self.current.x()-2,self.current.y()-2,self.current.width()+4,self.current.height()+4)
                
            if event.key()== Qt.Key.Key_E:
               if len(self.added): 
                if self.curr_num<len(self.added)-1 :
                    self.curr_num+=1
                else:
                    self.curr_num=0
                self.current= self.added[self.curr_num]
                self.curr_sel.setGeometry(self.current.x()-2,self.current.y()-2,self.current.width()+4,self.current.height()+4)
                
            if event.key()== Qt.Key.Key_F:
                if self.current.objectName().startswith("lbl_platk"):
                    if self.current.pixmap().cacheKey()==QPixmap(self.img_spikeu).cacheKey():
                        self.current.setPixmap(QPixmap (self.img_spiked))
                    elif self.current.pixmap().cacheKey()==QPixmap(self.img_spiked).cacheKey():
                        self.current.setPixmap(QPixmap (self.img_spikeu))
                    elif self.current.pixmap().cacheKey()== QPixmap(self.img_spikel).cacheKey():
                        self.current.setPixmap(QPixmap (self.img_spiker))
                    elif self.current.pixmap().cacheKey()==QPixmap(self.img_spiker).cacheKey():
                        self.current.setPixmap(QPixmap (self.img_spikel))
                        
            if event.key()== Qt.Key.Key_R:
                if not self.current.objectName().startswith("lbl_win"):
                    if self.current.objectName().startswith("lbl_platk") and self.current.width()<self.current.height():
                        self.current.setPixmap(QPixmap (self.img_spikeu))
                    elif self.current.objectName().startswith("lbl_platk") and self.current.width()>self.current.height():
                        self.current.setPixmap(QPixmap (self.img_spikel))
                    elif self.current.objectName().startswith("lbl_plath") or self.current.objectName().startswith("lbl_platv")  and self.current.width()>self.current.height():
                        self.current.setPixmap(QPixmap (self.img_movingr))
                    elif self.current.objectName().startswith("lbl_plath") or self.current.objectName().startswith("lbl_platv")  and self.current.width()<self.current.height():
                        self.current.setPixmap(QPixmap (self.img_moving))
                    self.current.setGeometry(self.current.x(),self.current.y(),self.current.height() ,self.current.width())
                    self.curr_sel.setGeometry(self.current.x()-2,self.current.y()-2,self.current.width()+4,self.current.height()+4)
            
            if event.key()==Qt.Key.Key_Delete:
                try:
                    if len(self.added)>0:
                        self.added.remove(self.current)
                        self.current.clear()
                        self.curr_num-=1
                        if len(self.added)==0:
                            self.curr_sel.setVisible(False)
                        self.current=self.added[self.curr_num]
                        self.curr_sel.setGeometry(self.current.x()-2,self.current.y()-2,self.current.width()+4,self.current.height()+4)
                except:
                  if len(self.added)>0:
                    self.curr_num= len(self.added)-1
                    self.current=self.added[self.curr_num]
                    self.curr_sel.setGeometry(self.current.x()-2,self.current.y()-2,self.current.width()+4,self.current.height()+4)
                    
            if event.key()== Qt.Key.Key_M:
                if self.mouse_active:
                  self.mouse_active=False 
                elif not self.mouse_active:
                  self.mouse_active=True  
                
            if event.key()== Qt.Key.Key_L:
                self.home()
            if event.key()== Qt.Key.Key_P:
                if (not self.j_count or self.j_count==4):
                    self.pause()
            
            self.current.move(self.current.x()+self.moveX, self.current.y()+self.moveY)
            self.curr_sel.move(self.curr_sel.x()+self.moveX, self.curr_sel.y()+self.moveY)
            
            
        elif not self.red.isVisible():
            if event.key()== Qt.Key.Key_D:
                if event.key()== Qt.Key.Key_A:
                    self.moveX= -self.moveX
                else:
                    self.moveX=3
            if event.key()== Qt.Key.Key_A:
                if event.key()== Qt.Key.Key_D:
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
            if event.key()== Qt.Key.Key_P:
                if (not self.j_count or self.j_count==4):
                    self.pause()
                
    def keyReleaseEvent(self, event):
        if event.key()==Qt.Key.Key_D:
            self.moveX=0
        if event.key()==Qt.Key.Key_A:
            self.moveX=0
        if event.key()==Qt.Key.Key_W:
            self.moveY=0
        if event.key()==Qt.Key.Key_S:
            self.moveY=0
        
        if event.key()== Qt.Key.Key_Right:
            self.moveX=0
        if event.key()== Qt.Key.Key_Left:
            self.moveX=0
        if event.key()== Qt.Key.Key_Down:
            self.moveY=0
        if event.key()== Qt.Key.Key_Up:
            self.moveY=0
            
    def start(self):
        
        self.j_count+=1
        self.function_x=-6
        self.py=self.lbl_player.y()
        self.jump()
        
    def double(self):
        self.j_count+=1
        self.function_x=-6
        self.py=self.lbl_player.y()
    
    def djump(self):
        if not self.double_jump:
            self.double_jump=True
        self.function_x+=.1
        self.calc()
        
    def jump(self):
            for p in self.platforms:
                if self.collison(self.lbl_player,p) and p.height()>51 and self.lbl_player.x() < p.x() and abs(self.lbl_player.y()+self.lbl_player.height()-p.y() >10):
                    self.lbl_player.move(self.lbl_player.x()-self.moveX-3, self.lbl_player.y())
                elif self.collison(self.lbl_player,p) and p.height()>51 and self.lbl_player.x() > p.x():
                    self.lbl_player.move(self.lbl_player.x()-self.moveX+3, self.lbl_player.y())
                if (self.collison(self.lbl_player,p)):
                    #snaps to floor
                    self.snapping(p)
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
        self.lbl_player.move(self.start_pos)
        if self.stopped:
            self.timer.start(24)
            self.curr_sel.setVisible(False)
            self.red.setVisible(False)
            self.toobox.setVisible(False)
            self.tip.setVisible(False)
            for p in self.findChildren(QLabel):
                if p.objectName().startswith("lbl_plat_"):
                    self.platforms.append(p)
                if p.objectName().startswith("lbl_platv_"):
                    self.vert_p.append(p)
                    self.platforms.append(p)
                    self.moving_p.append(p)
                if p.objectName().startswith("lbl_plath_"):
                    self.hori_p.append(p)
                    self.platforms.append(p)
                    self.moving_p.append(p)
                if  p.objectName().startswith("lbl_platk"):
                    self.kill.append(p)
                if p.objectName().endswith("win"):
                    self.winner.append(p)
            for p in self.moving_p :
                self.speed.append(2)
            self.j_count=0
            self.stopped=False
        elif not self.stopped:
            for i in self.master_list:
                i.clear()
            self.timer.stop()
            self.j_count=4
            self.stopped=True
            self.curr_sel.setVisible(False)
            self.tip.setVisible(True)
            self.red.setVisible(True)
            self.toobox.setVisible(True)
            self.toobox.blockSignals(True)
            
    def home(self):
        if not self.stopped:
            self.pause()
        self.j_count=0
        self.current= self.lbl_plat_3
        self.timer.stop()
        for i in self.added:
            self.added.remove(i)
            i.clear()
        self.lbl_winner.setVisible(False)
        manager.widget.setCurrentWidget(manager.start)
        manager.widget.resize(705,750)
