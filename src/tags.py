import tkinter as tk
import tkinter.font as tkFont
from tkinter import *

class App:
    def __init__(self, root):
        #setting title
        root.title("Nasan Inventory Prediction")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_380=tk.Entry(root)
        GLineEdit_380["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_380["font"] = ft
        GLineEdit_380["fg"] = "#333333"
        GLineEdit_380["justify"] = "center"
        GLineEdit_380["text"] = "Select Data File"
        GLineEdit_380.place(x=120,y=80,width=320,height=30)

        GButton_40=tk.Button(root)
        GButton_40["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_40["font"] = ft
        GButton_40["fg"] = "#000000"
        GButton_40["justify"] = "center"
        GButton_40["text"] = "Load Data"
        GButton_40.place(x=470,y=80,width=84,height=30)
        GButton_40["command"] = self.GButton_40_command

        GLabel_857=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_857["font"] = ft
        GLabel_857["fg"] = "#333333"
        GLabel_857["justify"] = "center"
        GLabel_857["text"] = "Generate Reports"
        GLabel_857.place(x=200,y=140,width=162,height=30)

        GButton_553=tk.Button(root)
        GButton_553["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_553["font"] = ft
        GButton_553["fg"] = "#000000"
        GButton_553["justify"] = "center"
        GButton_553["text"] = "Dead Inventory"
        GButton_553.place(x=150,y=190,width=104,height=33)
        GButton_553["command"] = self.GButton_553_command

        GButton_737=tk.Button(root)
        GButton_737["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#000000"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "Zero Inventory"
        GButton_737.place(x=350,y=190,width=104,height=35)
        GButton_737["command"] = self.GButton_737_command

        options = [
            # "102701010",
            # "220101070",
            # "315001015",
            # "810401043",
            # "810401044",
            # "830101003",
            # "830101291",
            "Load Data File"
        ]
        clicked = StringVar()
  
        # initial menu text
        clicked.set( "Load Data File" )
  
        GListBox_665=tk.OptionMenu( root , clicked , *options )
        GListBox_665["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_665["font"] = ft
        GListBox_665["fg"] = "#333333"
        GListBox_665["justify"] = "center"
        GListBox_665.place(x=120,y=270,width=321,height=30)

        GLineEdit_418=tk.Entry(root)
        GLineEdit_418["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_418["font"] = ft
        GLineEdit_418["fg"] = "#333333"
        GLineEdit_418["justify"] = "center"
        GLineEdit_418["text"] = "Enter Date"
        GLineEdit_418.place(x=120,y=320,width=320,height=30)

        GButton_679=tk.Button(root)
        GButton_679["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_679["font"] = ft
        GButton_679["fg"] = "#000000"
        GButton_679["justify"] = "center"
        GButton_679["text"] = "Ideal Stock"
        GButton_679.place(x=460,y=270,width=103,height=34)
        GButton_679["command"] = self.GButton_679_command

        GLabel_301=tk.Label(root)
        ft = tkFont.Font(family='Times',size=12)
        GLabel_301["font"] = ft
        GLabel_301["fg"] = "#333333"
        GLabel_301["justify"] = "center"
        GLabel_301["text"] = "Ideal Stock is: NA"
        GLabel_301.place(x=140,y=370,width=272,height=30)

        GButton_101=tk.Button(root)
        GButton_101["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_101["font"] = ft
        GButton_101["fg"] = "#000000"
        GButton_101["justify"] = "center"
        GButton_101["text"] = "Generate All Stock"
        GButton_101.place(x=460,y=320,width=103,height=34)
        GButton_101["command"] = self.GButton_101_command

    def GButton_40_command(self):
        print("command")


    def GButton_553_command(self):
        print("command")


    def GButton_737_command(self):
        print("command")


    def GButton_679_command(self):
        print("command")


    def GButton_101_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
