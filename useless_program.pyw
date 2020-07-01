import tkinter
from tkinter import messagebox
from time import sleep

def PositiveSelection () :

	tkinter.messagebox.showerror (title='F for Fool', message='You fool! You\'ll die alone! ')

def NegativeSelection () :

	tkinter.messagebox.showerror (title='F for Fool', message='You\'re a miserable bastard and you know it.')

window = tkinter.Tk()
window.title ('Useless Program')
window.geometry ("264x124")

window_text = tkinter.Label (text="\n- You want a good life?\n")
window_text.pack ()

window_button_1 = tkinter.Button (window, text='   Yes   ', command = PositiveSelection)
window_button_1.pack ()

window_button_2 = tkinter.Button (window, text='   No   ', command = NegativeSelection)
window_button_2.pack ()

window.mainloop ()
