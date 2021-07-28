import tkinter
import random

# Initiliaze the main window
root = tkinter.Tk()
root.geometry('800x500')
root.title('Just Rolling the Dice')

# A label which displays the dice
label = tkinter.Label(root, text='', font=('Courier', 260))

# This function is activated whenever the button is pressed
def roll_dice():
    # unicode character strings for the dice
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685'] # These are the unicodes
    label.configure(text=f'{random.choice(dice)} {random.choice(dice)}') # Display all the photos of dice randomly
    label.pack()

# button
button = tkinter.Button(root, text='roll dice', foreground='red', command=roll_dice) # Creating a button


button.pack() # Keep the Button in the main Window

# call the mainloop of Tk
# keeps window open i.e the program running
root.mainloop()
