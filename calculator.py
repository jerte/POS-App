import tkinter as tk
from orders import Item

class CalculatorControls(tk.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.create_buttons()

    def create_buttons(self):
        #add, clear, tax buttons
        self.add = tk.Button(self, text='add', command=self.add_func)
        self.clear = tk.Button(self, text='clear', command=self.clear_func)
        self.pack()
        self.add.pack(side="left")
        self.clear.pack(side="right")
    
    def set_display_label(self, label):
        self.display_label = label

    def set_add_location(self, order):
        self.order = order
    
    def add_func(self):
        try:
            self.order.items.append(self.display_label['text'])
            self.create_order_display()
        except Exception:
            print('error logged')
    
    def clear_func(self):
        try:
            self.display_label['text'] = '0.00'
        except Exception as e:
            print('error logged')
    
    def set_create_order_display(self, create_order_display):
        self.create_order_display = create_order_display


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
                          command=self.add_num_to_display(b),
                          height=5,
                          width=10).grid(row=i,column=j, padx=5,pady=5)
                #self.num_button_func(b))

    
    def add_num_to_display_helper(self,num):
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

    def add_num_to_display(self, i):
        return lambda:self.add_num_to_display_helper(i)


    def num_button_func(self, i):
        return lambda:self.display_var.set(str(self.display_var)[:-2] + str(self.display_var)[-2]+ "." + str(self.display_var)[-1] + str(i))
       
    def create_display(self):
        self.display = tk.Label(self, text="0.00", bg='white', font=("Arial",24))
        self.display.grid(row=0, columnspan=3)
