import tkinter as tk
from calculator import *
from controls import *
from orders import *

class Application():
    def __init__(self):
        self.window = tk.Tk()
        self.setup()
        self.create_widgets()
        self.window.mainloop()
       
    def setup(self):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d" %(self.w, self.h))
        self.window.configure(bg='white')

        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>",self.quitFullScreen)
        

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen",self.fullScreenState)
    
    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def create_widgets(self):
        #left frame for orders and orderbook
        self.leftFrame = tk.Frame(self.window)
        self.leftFrame.pack(fill="both", side="left", expand=1)
        
        self.order_book = Orders(self.leftFrame)
        self.order_book.pack(fill="both", side='left', expand=1)
        
        #right frame for calculator, app controls, item selection
        self.rightFrame = tk.Frame(self.window)
        self.rightFrame.pack(side="right", fill="both")

        self.controlFrame = tk.Frame(self.rightFrame)
        self.controlFrame.pack(side="bottom")

        self.controls = Controls(self.controlFrame)
        self.controls.update_quit(self.window)
        self.controls.pack(side="bottom")
        
        self.calcFrame = tk.Frame(self.rightFrame)
        self.calcFrame.pack(side='bottom')
        
        self.calc = Calculator(self.calcFrame, highlightcolor='black')
        self.calc.pack(side='top')
        
        self.calcControls = CalculatorControls(self.calcFrame)
        self.calcControls.set_display_label(self.calc.display)
        self.calcControls.set_add_location(self.order_book.add_location)
        self.calcControls.set_create_order_display(self.order_book.create_display)
        self.calcControls.pack(side='bottom')
           
        self.order_book.set_add_location_update_func(self.calcControls.set_add_location)


if __name__=='__main__':
    app = Application()
'''
app['background'] = "#FFFFFF"
#app.geometry(str(app.winfo_screenwidth())+"x"+str(app.winfo_screenheight()))

self.geometry("1920x1080")
print(app.winfo_height()) 
app.mainloop()
'''
