#This program takes text as an iput and then displays information from Twitter , Google, and Wikipedia
import tkinter
from tkinter import ttk
import tweeterInFO
import sys


class Search_frame():
    def __init__(self):
        #Create main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Encyclopedia program ")
        #tkinter.Frame.__init__(self, padding = '10, 10, 10,10')

        #Create three Frames to group widgets
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()



    #Create the widgets for the top frame
        self.promptLable = tkinter.Label(self.top_frame, text = "Enter text to search : ")
        self.textEntry = tkinter.Entry(self.top_frame, width = 30)
    #Create an InVar objects to use with the Radiobuttons
        self.radio_var = tkinter.IntVar()
        #set the IntVar object to 1
        self.radio_var.set(1)
        #Creat the Radiobuttons widgets in the top_frame
        self.rb1 = tkinter.Radiobutton(self.mid_frame, text = 'Twitter', variable = self.radio_var, value = 1)

    #Pack the top fram's widget
        self.promptLable.pack(side = 'left')
        self.textEntry.pack(side = 'left')
        #pack the radiobox
        self.rb1.pack(side = 'left')
    #Create the widget for the middle fram
        self.desc_lable = tkinter.Label(self.mid_frame, text = "Displayed Information ")
    #We need a StringVar objects to associate with an output lable. Use the object's set method to store
    #a string of blank characters
        self.value = tkinter.StringVar()


    #Create a Label and associate it with the StringVar object. Any value stored in the
        #  StroingVar object will automatically  displayed in the label

        self.output_lable = tkinter.Label(self.mid_frame, textvariable = self.value)
        #Pack the middle frame's widget
        self.desc_lable.pack(side = 'left')
        self.output_lable.pack(side = 'left')
    #Create the botton widgets for the botton frame.
        self.submit_button = tkinter.Button(self.bottom_frame, text = "Submit", command = self.display)

        #pack the botton
        self.submit_button.pack(side = 'left')


        #Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # = tkinter.Tk()

        tkinter.mainloop()


    def display(self):

        info = self.textEntry.get()
        output = tweeterInFO.gettingTweetInfo(info)
        #print(output)

        self.value.set(str(output))



Search_frame()

