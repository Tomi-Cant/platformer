# By: Tomi Banjoko
# Date: 2024-01-08
# Program Details: A platformer  with multiple levels moving platforms and spikes that kill the player

import manager, sys, random
from PySide6.QtGui import QKeyEvent, QPixmap 
from PySide6.QtCore import Qt, QTimer, QRect
from PySide6.QtWidgets import QLabel 
from gui.page_start_ui import Ui_MainWindow
class MainWindow(manager.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.num=0
        self.sel_screen.setVisible(False)
        self.buttons=[self.btn_tutorial,self.btn_lvl1,self.btn_lvl2,self.btn_lvl3,self.btn_inf]
        
    def btn_x_a(self):
        sys.exit()
    def enter_a(self):
        if len(self.txt_name.text())>0:
            self.name=self.txt_name.text()
        else:
            print("hi")
            self.name= "Friend"
        self.enter.setVisible(False)
        self.lbl_name.setText(f"Hi, {self.name}!")
    
    def level_select(self):
        btn=self.sender()
        if not self.num:
            self.num=1
            self.sel_screen.setVisible(True)
        else:
            manager.widget.resize(1530,800)
            manager.widget.setCurrentWidget(manager.level_dex[self.buttons.index(btn)])
           
            manager.level_dex[self.buttons.index(btn)].timer.start(16)
            self.sel_screen.setVisible(False)
            for label in manager.level_dex[self.buttons.index(btn)].findChildren(QLabel):
                if label.objectName().startswith("lbl_player"):
                    label.move(manager.positions[self.buttons.index(btn)])
                    self.num=0  