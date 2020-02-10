import sys
from sound_panel import SoundPanel

import os
import pygame.mixer
import tkinter as gui

VALIDEXTENSIONS = ['ogg', 'flac', 'wav']
SOUNDDIR = './sounds'
UNITHEIGHT = 37

def setDir(path):
    try:
        os.chdir(path)
    except:
        os.mkdir(path)
        os.chdir(path)


def filterExtensions(fileList, validExtensionsList):
    result = []
    for fileName in fileList:
        extension = fileName.split('.')[-1]
        if extension in validExtensionsList:
            result.append(fileName)
    return result

def setWindowHeight(window, height):
    window.geometry('450x%s+300+300' %str(height))


def __main__(soundDir):
    def closeWindow():
        mymixer.stop()
        window.quit()
        window.destroy()
        # sys.path.remove('./')
    #Initialize Window
    window = gui.Tk()
    window.title('Basic Pygame Music Player')
    window.protocol('WM_DELETE_WINDOW', closeWindow)
    height = UNITHEIGHT
    setWindowHeight(window, height)
    #Initialize Mixer
    mymixer = pygame.mixer
    mymixer.init()
    #Define Sound Files
    setDir(soundDir)
    #Create Sound Panels
    tracklist = filterExtensions(os.listdir(os.getcwd()), VALIDEXTENSIONS)
    for track in tracklist:
        SoundPanel(window, mymixer, track).pack()
        height += UNITHEIGHT
        setWindowHeight(window, height)
    # Run Window    
    window.mainloop()


__main__(SOUNDDIR)