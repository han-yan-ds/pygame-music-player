import sys
from sound_panel import SoundPanel

import os
import pygame.mixer
import tkinter as gui

VALIDEXTENSIONS = ['ogg', 'flac', 'wav']
SOUNDDIR = './sounds'

def set_dir(path):
    try:
        os.chdir(path)
    except:
        os.mkdir(path)
        os.chdir(path)


def filterExtensions(fileList, validExtensionsList):
    result = []
    for filename in fileList:
        extension = filename.split('.')[-1]
        if extension in validExtensionsList:
            result.append(filename)
    return result


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
    tracklist = filterExtensions(os.listdir(os.getcwd()), VALIDEXTENSIONS)
    for track in tracklist:
        SoundPanel(window, mymixer, track).pack()
        height += 37
        window.geometry('450x%s+300+300' %str(height))
    # Run Window    
    window.mainloop()


__main__(SOUNDDIR)