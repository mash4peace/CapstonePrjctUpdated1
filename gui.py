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

        self.options = {1:"Twitter", 2:"Not Twitter"}

        self.rb1 = tkinter.Radiobutton(self.mid_frame, text = self.options[1], variable = self.radio_var, value = 1, command=self.doThing)
        self.rb2 = tkinter.Radiobutton(self.mid_frame, text = self.options[2], variable = self.radio_var, value = 2, command=self.doThing)

    #Pack the top fram's widget
        self.promptLable.pack(side = 'left')
        self.textEntry.pack(side = 'left')
        #pack the radiobox
        self.rb1.pack(side = 'left')
        self.rb2.pack()
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


    def doThing(self):
        print('use a better method name')
        print(self.radio_var.get())
        print(self.options[self.radio_var.get()])


    def display(self):

        print(self.radio_var.get())



        info = self.textEntry.get()

        if info is None or len(info) == 0:
            print("enter a name")


        output = tweeterInFO.gettingTweetInfo(info)
        #print(output)

        self.value.set(str(output))



Search_frame()
