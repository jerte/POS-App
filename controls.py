import tkinter as tk
import db
from calculator import *

class Controls(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        
        # app controls
        self.create_app_controls()
        
        # calculator
        self.create_calculator()
        
        # item selection (this might be a fullscreen thing)
        
        #self.create_buttons()
    
    def create_app_controls(self):
        self.app_controls_outer_frame = tk.Frame(self)
        self.app_controls_inner_frame = tk.Frame(self.app_controls_outer_frame)

        self.timesheet = tk.Button(self.app_controls_inner_frame, text="TIMESHEET",
                                       command=self.launch_timesheet)
        self.schedule = tk.Button(self.app_controls_inner_frame, text="SCHEDULE",
                                    command=self.launch_schedule)
        self.db_app = tk.Button(self.app_controls_inner_frame, text="DB APP",
                                    command=self.launch_db_app)
        self.quit = tk.Button(self.app_controls_inner_frame, text="QUIT", fg="red",
                                    command=self.master.destroy)
        
        self.timesheet.grid(row=0, column=1)    
        self.schedule.grid(row=0, column=2)    
        self.db_app.grid(row=0, column=3)
        self.quit.grid(row=0,column=4)
        
        self.app_controls_inner_frame.grid() #pack here?
        self.app_controls_outer_frame.pack(side='bottom')
       
    def create_calculator(self):
        self.calc_frame = tk.Frame(self)
        # calculator
        self.calc = Calculator(self.calc_frame, highlightcolor='black')
        self.calc.pack(side='top')
        # calculator controls
        self.calc_controls = CalculatorControls(self.calc_frame)
        #link calc and calc controls
        self.calc_controls.set_display_label(self.calc.display)
        #link calc controls & orderbook 
        
        self.calc_controls.pack(side='bottom') 
        self.calc_frame.pack(side='bottom')
    
    ''' partially implemented '''
    def launch_db_app(self):
        ''' not meant to be launched from here atm, better to run db.py directly'''
        db_app = db.DB_App(self.master)
    ''' end partially implemented '''
     
    ''' unimplemented '''
    def launch_timesheet(self):
        ##open timesheet application
        print("timesheet sub application")
    def launch_schedule(self):
        print("schedule sub app")
    ''' end unimplemented '''

    
