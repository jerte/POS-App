import tkinter as tk
from functools import partial
from db import *

''' item class
        represents item from db
'''
class Item():
    def __init__(self, item_id,stocked_quantity, cost, price, barcode, units, name, tax_rate, quantity=1):
        self.item_id=item_id
        self.stocked_quantity = stocked_quantity
        self.cost = cost
        self.price=price
        self.barcode = barcode
        self.units = units
        self.name = name
        self.tax_rate = tax_rate
        self.quantity = quantity
        
''' order class
        represents order which will be sent to db
'''
class Order():
    def __init__(self):
        self.items = []

    def remove_item(self, index):
        self.items.pop(index)
        self.create_display_func()
    
    def edit_item_quantity(self, item_i, quantity):
        if(self.items[item_i].quantity+quantity > 0):
            self.items[item_i].quantity += quantity
            self.create_display_func()
    
    def adjust_price(self):
        return None
    
    def set_create_display_func(self, func):
        self.create_display_func = func

''' orderbook class
        tk frame widget which displays & manages orders
'''
class Orderbook(tk.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)    
        self.setup()
        self.create_display()
        self.db_c = DB_Connector()

    def setup(self):
        self.current=0
        self.orders = []
        self.orderbook_frame = tk.Frame(self, bg ='white')
        self.orderbook_frame.pack(side='top', fill='both')
        
        self.order_frame = tk.Frame(self, bg='white')
        self.order_frame.pack(side='bottom', fill='both', expand=1)
        
        self.order_items_frame = tk.Frame(self.order_frame, bg='white')
        self.order_items_frame.pack(side='top', fill='both') 

    def create_display(self):    
        if not len(self.orders):
            order = Order()
            order.set_create_display_func(self.create_display)
            self.orders.append(order)
        
        # look into pack_forget, just removes from view but data still available
        for i in self.orderbook_frame.winfo_children():
            i.destroy()
        for i in self.order_items_frame.winfo_children():
            i.destroy()
        
        for i in range(len(self.orders)):
            tk.Button(self.orderbook_frame, text="Order "+str(i+1),
               command=partial(self.display_order,index=i),
               height=2,width=10).grid(row=0, column=(i+1), padx=5, pady=5)
        
        if(len(self.orders)<10):
            tk.Button(self.orderbook_frame, text="New Order", command=self.new_order, 
               height=2,width=10).grid( row=0,column=(len(self.orders)+1), padx=5, pady=5)
       
        try:
            self.currentLabel['text']='Current Order: '+str(self.current+1)
        except Exception:
            self.currentLabel = tk.Label(self.orderbook_frame, text='Current Order: '+str(self.current+1),
                                         font=('Arial', 36))
            self.currentLabel.grid(row=1, columnspan=5)
        
        try:
            self.closeButton.configure(text='Close Order '+str(self.current+1))
        except Exception as e: 
            self.closeButton = tk.Button(self.order_frame,text='Close Order '+str(self.current+1),
                                            command=self.close_order)
            self.closeButton.pack(side='bottom', anchor='w')
        
        for i,item_i in enumerate(self.get_current_order().items):
            tk.Label(self.order_items_frame, 
                     text=str(i+1)+'. '+item_i.name+' : $'+str(item_i.price)+' X '+str(item_i.quantity),
                     font=('Arial',24)).grid(row=i, column=0, columnspan=2, pady=5)
            
            tk.Button(self.order_items_frame, text='  +  ', font=('Arial',24),
                command=partial(self.get_current_order().edit_item_quantity, i, 1)
                ).grid(row=i, column=2)
            
            tk.Button(self.order_items_frame, text='  -  ', font=('Arial',24),
                command=partial(self.get_current_order().edit_item_quantity, i, -1)
                ).grid(row=i, column=3)
            
            tk.Button(self.order_items_frame, text='Remove Item', font=('Arial',24),
                command=partial(self.get_current_order().remove_item, i)).grid(row=i, column=4)
    
    def get_current_order(self):
        return self.orders[self.current]
    
    def new_order(self):
        order = Order()
        order.set_create_display_func(self.create_display)
        self.orders.append(order)
        self.current = len(self.orders)-1
        self.display_order(self.current)
    
    def close_order(self, paid=True):
        #if(paid):
        #    keep data
        #     send order to db
        self.orders.pop(self.current)
        self.current = 0
        self.create_display()
    
    def display_order(self, index=0):
        self.current = index 
        self.create_display()

    def link_to_calc_display(self, calc_display):
        self.calc_display=calc_display

    def add_item_to_current_order(self, item):
        barcodes = [i.barcode for i in self.get_current_order().items]
        if( item.barcode in barcodes ):
            # way too long
            self.get_current_order().items[barcodes.index(item.barcode)].quantity += 1     
        else:
            self.get_current_order().items.append(item)
        self.create_display()
    
    ''' unimplemented '''
    def send_to_db(self):
        return None
    ''' end uminplemented '''
    
