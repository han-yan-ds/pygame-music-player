import sys
from sound_panel import *

import os
import pygame.mixer
import tkinter as gui

def set_dir(path):
    try:
        os.chdir(path)
    except:
        os.mkdir(path)
        os.chdir(path)

def close_window():
    mymixer.stop()
    window.quit()
    window.destroy()
    # sys.path.remove('./')

#Initialize Window
window = gui.Tk()
window.title('Basic Pygame Music Player')
window.protocol('WM_DELETE_WINDOW', close_window)
height = 37
window.geometry('450x%s+300+300' %str(height))
#Define Sound Files
set_dir('./sounds')
#Initialize Mixer
mymixer = pygame.mixer
mymixer.init()
#Create Sound Panels
track_list = os.listdir(os.getcwd())
for track_name in track_list:
    if track_name[-4:]=='.ogg':
        SoundPanel(window, mymixer, track_name).pack()
        height += 37
        window.geometry('450x%s+300+300' %str(height))
    
window.mainloop()
