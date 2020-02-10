from tkinter import Label, Frame, Button, Scale, StringVar, IntVar, LEFT, RIGHT, HORIZONTAL
import pygame.mixer

class SoundPanel(Frame):

    def __init__(self, app, mixer, sound_file):
        Frame.__init__(self, app)
        
        self.sound_obj = mixer.Sound(sound_file)
        self.is_playing = False

        Label(self, text=sound_file).pack(side=LEFT)

        self.button_text = StringVar()
        self.button_text.set('Play')#see if i can use app here instead
        button = Button(self, command=self.__play_toggle__,
                        textvariable=self.button_text)
        button.pack(side=LEFT)

        self.volume = IntVar()
        self.volume.set(50)
        volume_scale = Scale(self, variable=self.volume, from_=0, to=100,
                             command=self.__change_volume__, orient=HORIZONTAL,
                             resolution=1)
        volume_scale.pack(side=RIGHT)
                        


    def __play_toggle__(self):
        if self.is_playing == False:
            self.sound_obj.play(loops=-1)
            self.is_playing = True
            self.button_text.set('Stop')
        else:
            self.sound_obj.stop()
            self.is_playing = False
            self.button_text.set('Play')

    def __change_volume__(self, v):
        self.sound_obj.set_volume(self.volume.get()/100.0)
