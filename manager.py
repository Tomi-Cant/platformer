# By: Tomi Banjoko
# Date: 2024-01-08
# Program Details: A platformer  with multiple levels moving platforms and spikes that kill the player
import sys,os,contextlib
from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QMainWindow,QStackedWidget,QApplication
)
import interface.page_1
import interface.start
import interface.page_2
import interface.page_3
import interface.page_4
import interface.page_inf
@contextlib.contextmanager
def image_gui_path():
    try:
        os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gui'))
        yield
    finally:
        os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__))))

app = QApplication(sys.argv)

with image_gui_path():
    screen1 = interface.page_1.MainWindow()
    start= interface.start.MainWindow()
    screen2= interface.page_2.MainWindow()
    screen3=interface.page_3.MainWindow()
    screen4=interface.page_4.MainWindow()
    wip= interface.page_inf.MainWindow()
level_dex=[screen1,screen2,screen3,screen4,wip]
pos1= screen1.lbl_player.pos()
pos2= screen2.lbl_player.pos()
pos3=screen3.lbl_player.pos()
pos4= screen4.lbl_player.pos()
pos_wip=wip.lbl_player.pos()
positions=[pos1,pos2,pos3,pos4,pos_wip]
widget=QStackedWidget()
widget.addWidget(screen1)
widget.addWidget(screen2)
widget.addWidget(start)
widget.addWidget(screen3)
widget.addWidget(screen4)
widget.addWidget(wip)
widget.resize(start.size())
widget.setCurrentWidget(start)
widget.setWindowTitle(start.windowTitle())