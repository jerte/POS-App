''' 
to do
1) clean up code
    - delete unnecessary comments & functions
    - rewrite into cleaner & clearer code
    - standardize conventions, review python style guide & rewrite
    - review imports for all files
    - fix redundancies (kb input i'm looking at you)
2) change from pack to grid -> better for adding & removing widgets
3) add item selection app
    - sort items so that most sold appear first
    - maybe alphabetical option too
4) fine tune app appearance
5) documentation
'''
import tkinter as tk
from calculator import *
from controls import *
from orders import *
from keyboard_logger import *
from item_selector import *

''' Application class
        collects & interconnects widgets to run app
'''
class Application():
    def __init__(self):
        self.setup()
        self.create_widgets()
        self.readScanner()
        self.window.mainloop()

    ''' declare variables and create window '''
    def setup(self): 
        self.window = tk.Tk() 
        self.app_frame = tk.Frame(self.window)
        self.app_frame.pack(fill="both", expand=1)

        self.db_c = DB_Connector()
        
        self.keyboard_logger = KeyboardLogger(interval=1,report_method='app') 
        self.keyboard_logger.start()
        
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

    ''' method to read keyboard input for barcodes every .5 seconds 
        (.5s is not set in stone. may change)
    '''
    def readScanner(self):
        if(self.keyboard_logger.log):
            # [:-8] because '[ENTER]' @ end of barcode
            item_tup = self.db_c.get_item_by_barcode(self.keyboard_logger.log[:-8])
            if( item_tup ):
                new_item = Item(*item_tup)
                self.order_book.add_item_to_current_order(new_item)
            else:
                # handling this will come later
                print('item not found')
                #print('do you want to add this item now?')
            
            self.keyboard_logger.log = ''

        # call readScanner again after .5 seconds (not set on this time)
        self.window.after(500,self.readScanner)
    
    def create_widgets(self):
        self.order_book = Orderbook(self.app_frame)
           
        #self.order_book.grid(row=0, column=0)
        self.order_book.pack(fill="both", side='left', expand=1)
        # app controls
        # calculator
        # item selection
        
        self.controlFrame = Controls(self.app_frame, self.window)
        self.controlFrame.pack(fill='both', side='right')
           
        self.controlFrame.calc_controls.link_get_current_order(self.order_book.get_current_order)
        self.controlFrame.calc_controls.link_order_create_display(self.order_book.create_display)

        self.order_book.link_to_calc_display(self.controlFrame.calc.display)

if __name__=='__main__':
    app = Application()
