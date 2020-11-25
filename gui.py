from screenGrabber import *
import tkinter as tk
from tkinter import font

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        appHighlightFont = font.Font(family='Helvetica', size=20)
        lable1 = tk.Label(self , text="ScreenGrabber_GUI",font=appHighlightFont)
        lable1.pack()
        
        lable = tk.Label(self , text="",font=appHighlightFont)
        lable.pack()
        appHighlightFont = font.Font(family='Helvetica', size=13)
        label_2 = tk.Message(self, text="Lorem ipsum dolor sit amet," 
        " consectetur adipiscing elit, sed do eiusmod tempor incididunt "
        " ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis " 
        "nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"
        " consequat. Duis aute irure dolor in reprehenderit in voluptate "
        "velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "
        "occaecat cupidatat non proident, sunt in culpa qui "
        " officia deserunt mollit anim id est laborum."
        "Lorem ipsum dolor sit amet," 
        " consectetur adipiscing elit, sed do eiusmod tempor incididunt "
        " ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis " 
        "nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"
        " consequat. Duis aute irure dolor in reprehenderit in voluptate "
        "velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "
        "occaecat cupidatat non proident, sunt in culpa qui "
        " officia deserunt mollit anim id est laborum."
        "Lorem ipsum dolor sit amet," 
        " consectetur adipiscing elit, sed do eiusmod tempor incididunt "
        " ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis " 
        "nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo"
        " consequat. Duis aute irure dolor in reprehenderit in voluptate "
        "velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint "
        "occaecat cupidatat non proident, sunt in culpa qui "
        " officia deserunt mollit anim id est laborum.", width=500,font=appHighlightFont)
        label_2.pack()
        lable = tk.Label(self , text="",font=appHighlightFont)
        lable.pack()
        lable = tk.Label(self , text="",font=appHighlightFont)
        lable.pack()
        tk.Button(self, text="NEXT>>",
                  command=lambda: master.switch_frame(PageOne)).pack()

       
                 

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        appHighlightFont = font.Font(family='Helvetica', size=14)
        tk.Label(self, text="Enter Username",  font=appHighlightFont).grid(row=10,column=0)
        tk.Label(self, text="Enter Password", font=appHighlightFont).grid(row=12,column=0)
        entry_1 = tk.Entry(self, width="30")
        entry_2 = tk.Entry(self, show='*', width="30")
        for i in (0,1,2,3,4,5,6,7,8,9,11,13,14,15,16):
            tk.Label(self,text="", width=15).grid(row=i,column=0)
        entry_1.grid(row=10,column=7)
        entry_2.grid(row=12,column=7)
        tk.Button(self,font=appHighlightFont,
                          text='Continue',
                          command=lambda:[self.value(entry_1.get(),entry_2.get()),
                                          master.switch_frame(PageTwo)]).grid(row = 17,column = 3)
    def value(self,val1,val2):
        data.append(val1)
        data.append(val2)

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        appHighlightFont = font.Font(family='Helvetica', size=17)
        for i in (0,1,2,3,4,5,6,8,10,12,14,16,17,19,20):
            tk.Label(self,text="", width=15).grid(row=i,column=0)
        tk.Label(self, text="APP Working",font=appHighlightFont).grid(row=7 ,sticky=tk.W)
        appHighlightFont = font.Font(family='Helvetica', size=14)
        


    


if __name__ == "__main__":
    data = list()
    app = App()
    app.title('ScreenGrabber_GUI')
    app.geometry('600x600')
    app.mainloop()
    print(data)