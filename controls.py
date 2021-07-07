import tkinter as tk

class Controls(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.create_buttons()
    
    def create_buttons(self):
        self.timesheet = tk.Button(self, text="TIMESHEET",
                        command=self.timesheet)
        self.timesheet.grid(row=0, column=1)
        self.schedule = tk.Button(self, text="SCHEDULE",
                        command=self.schedule)
        self.schedule.grid(row=0, column=2)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=0,column=3)
       
    def update_quit(self, window):
        self.window = window
        self.quit['command'] = self.window.destroy

    def timesheet(self):
        ##open timesheet application
        print("timesheet sub application")
    def schedule(self):
        print("schedule sub app")
