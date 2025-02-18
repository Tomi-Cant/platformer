# By: Tomi Banjoko
# Date: 2024-01-08
# Program Details: A platformer  with multiple levels moving platforms and spikes that kill the player
#key color rgb= 15,21,47
#bg color rgb= 182,164,137                             
import manager

if __name__ == "__main__":
    manager.widget.show()
    manager.screen1.setFocus()
    manager.sys.exit(manager.app.exec())  