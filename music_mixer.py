import sys
from sound_panel import SoundPanel

import os
import pygame.mixer
import tkinter as gui

VALIDEXTENSIONS = ['ogg', 'flac', 'wav']

def set_dir(path):
    try:
        os.chdir(path)
    except:
        os.mkdir(path)
        os.chdir(path)


def __main__(soundDir):
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
    #Initialize Mixer
    mymixer = pygame.mixer
    mymixer.init()
    #Define Sound Files
    set_dir(soundDir)
    #Create Sound Panels
    track_list = os.listdir(os.getcwd())
    for track_name in track_list:
        extension = track_name.split('.')[-1]
        if  extension in VALIDEXTENSIONS:
            SoundPanel(window, mymixer, track_name).pack()
            height += 37
            window.geometry('450x%s+300+300' %str(height))
    # Run Window    
    window.mainloop()

__main__('./sounds')