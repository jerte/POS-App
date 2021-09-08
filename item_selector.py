import tkinter as tk

class Item_Selector(tk.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.create_buttons()
    
    def create_buttons(self):
        self.button = tk.Button(self, text='item')
        self.button.pack()
        return None
    
    def set_dbc(self, dbc):
        self.dbc = dbc


