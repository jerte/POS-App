import tkinter as tk
from orders import Item
from functools import partial

class CalculatorControls(tk.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.create_buttons()

    def create_buttons(self):
        #add, clear, tax (necessary?) buttons
        self.add = tk.Button(self, text='add', command=self.add_func)
        self.clear = tk.Button(self, text='clear', command=self.clear_func)
        self.add.pack(side="left")
        self.clear.pack(side="right")
    
    def set_display_label(self, label):
        self.display_label = label

    def add_func(self):
        try:
            #depreciated lol
            item = Item()
            
            #should be self.get_current_order().append(item)
            self.order.items.append(item)
            
            self.order_create_display()
        except Exception:
            print('error logged - add func')
    
    def clear_func(self):
        try:
            self.display_label['text'] = '0.00'
        except Exception as e:
            print('error logged - clear func')
   
    def link_get_current_order(self, get_current_order):
        self.get_current_order = get_current_order

    def link_order_create_display(self, create_display):
        self.order_create_display = create_display

class Calculator(tk.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.create_display()
        self.create_buttons()

    def create_buttons(self):
        b = 0
        for i in range(1,4):
            for j in range(3):
                b += 1
                tk.Button(self, 
                          text=str(b),
                          command=partial(self.add_num_to_display,b),
                          height=5,
                          width=10).grid(row=i,column=j, padx=5,pady=5)
    
    def add_num_to_display(self,num):
        temp = self.display["text"]
        #while zero, get last zero, replace with new value or shifted value
        i = 0
        while(i < len(temp) and (temp[i]=="0" or temp[i]==".")):
            i += 1
        if(i>0):
            #0.00
            if(i==len(temp)):
                self.display["text"] = temp[:-1] + str(num)
            #0.0x"
            elif(i==len(temp)-1):
                self.display["text"] = temp[:-2] + temp[-1] + str(num)
            #0.xx"
            elif(i==2):
                self.display["text"] = temp[-2] + "." + temp[-1] + str(num)
        elif(len(temp)<10):
            self.display["text"] = temp[:-3] + temp[-2] + "." + temp[-1] + str(num)

    def create_display(self):
        self.display = tk.Label(self, text="0.00", bg='white', font=("Arial",24))
        self.display.grid(row=0, columnspan=3)
