import tkinter as tk
from functools import partial

#DB too
class Item():
    def __init__(self):
        self.id=1
        self.price=1
        self.units = "EA" # Dz, ea
        self.name = 'test item'
        self.quantity = 1
    
#this will eventually sent to DB
class Order():
    def __init__(self):
        self.items = []
    def add_item(self):
        return None
    def remove_item(self, index):
        self.items.pop(index)
        self.create_display_func()
    def edit_item_quantity(self, item_i, quantity):
        if(self.items[item_i].quantity+quantity > 0):
            self.items[item_i].quantity += quantity
            self.create_display_func()
    def adjust_price(self):
        return None
    def send_to_db(self):
        return None
    def set_create_display_func(self, func):
        self.create_display_func = func

class Orders(tk.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)    
        self.setup()
        self.create_display()
        self.add_location = self.orders[self.current]
    
    def setup(self):
        self.current=0
        self.orders = []
        self.orderBookFrame = tk.Frame(self, bg ='white')
        self.orderBookFrame.pack(side='top', fill='both')
        
        self.orderFrame = tk.Frame(self, bg='white')
        self.orderFrame.pack(side='bottom', fill='both', expand=1)
        
        self.orderItemsFrame = tk.Frame(self.orderFrame, bg='white')
        self.orderItemsFrame.pack(side='top', fill='both') 

    def create_display(self):    
        if not len(self.orders):
            order = Order()
            order.set_create_display_func(self.create_display)
            self.orders.append(order)
        
        # look into pack_forget, just removes from view but data still available
        for i in self.orderBookFrame.winfo_children():
            i.destroy()
        for i in self.orderItemsFrame.winfo_children():
            i.destroy()
        
        for i in range(len(self.orders)):
            tk.Button(self.orderBookFrame, text="Order "+str(i+1),
               command=partial(self.display_order,index=i),
               height=2,width=10).grid(row=0, column=(i+1), padx=5, pady=5)
        
        if(len(self.orders)<10):
            tk.Button(self.orderBookFrame, text="New Order", command=self.new_order, 
               height=2,width=10).grid( row=0,column=(len(self.orders)+1), padx=5, pady=5)
       
        try:
            self.currentLabel['text']='Current Order: '+str(self.current+1)
        except Exception:
            self.currentLabel = tk.Label(self.orderBookFrame, text='Current Order: '+str(self.current+1),
                                         font=('Arial', 36))
            self.currentLabel.grid(row=1, columnspan=5)
        
        try:
            self.closeButton.configure(text='Close Order '+str(self.current+1))
        except Exception as e: 
            self.closeButton = tk.Button(self.orderFrame,text='Close Order '+str(self.current+1),
                                            command=self.close_order)
            self.closeButton.pack(side='bottom', anchor='w')
        
        for i,item_i in enumerate(self.orders[self.current].items):
            tk.Label(self.orderItemsFrame, 
                     text=str(i+1)+'. '+item_i.name+' : $'+str(item_i.price)+' X '+str(item_i.quantity),
                     font=('Arial',24)).grid(row=i, column=0, columnspan=2, pady=5)
            tk.Button(self.orderItemsFrame, text='  +  ', font=('Arial',24),
                command=partial(self.orders[self.current].edit_item_quantity, i, 1)
                ).grid(row=i, column=2)
            tk.Button(self.orderItemsFrame, text='  -  ', font=('Arial',24),
                command=partial(self.orders[self.current].edit_item_quantity, i, -1)
                ).grid(row=i, column=3)
            tk.Button(self.orderItemsFrame, text='Remove Item', font=('Arial',24),
                command=partial(self.orders[self.current].remove_item, i)).grid(row=i, column=4)
        
    def new_order(self):
        order = Order()
        order.set_create_display_func(self.create_display)
        self.orders.append(order)
        self.current = len(self.orders)-1
        self.display_order(self.current)
    
    def close_order(self):
        #keep data
        self.orders.pop(self.current)
        self.current = 0
        self.create_display()
        # send order to db
    
    def display_order(self, index=0):
        self.current = index 
        self.add_location = self.orders[self.current]
        self.add_location_update_func(self.add_location)
        self.create_display()

    def set_add_location_update_func(self, add_location_update_func):
        self.add_location_update_func = add_location_update_func
