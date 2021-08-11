import tkinter as tk
import db

class Controls(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.create_buttons()
    
    def create_buttons(self):
        self.timesheet = tk.Button(self, text="TIMESHEET",
                        command=self.launch_timesheet)
        self.timesheet.grid(row=0, column=1)
        
        self.schedule = tk.Button(self, text="SCHEDULE",
                        command=self.launch_schedule)
        self.schedule.grid(row=0, column=2)

        self.db_app = tk.Button(self, text="DB APP",
                        command=self.launch_db_app)
        self.db_app.grid(row=0, column=3)
        
        self.quit = tk.Button(self, text="QUIT", fg="red")
        self.quit.grid(row=0,column=4)
       
    def update_window(self, window):
        self.window = window
        self.quit['command'] = self.window.destroy

    def launch_timesheet(self):
        ##open timesheet application
        print("timesheet sub application")
    def launch_schedule(self):
        print("schedule sub app")
    def launch_db_app(self):
        db_app = db.DB_App(self.window)
        print('db app')
