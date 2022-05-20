import psycopg2
import os
from typing import *
import tkinter as tk
from functools import partial

class DB_Connector:
    def __init__(self):
        self.conn = psycopg2.connect(str(os.environ['CONN']))
        self.cur = self.conn.cursor()
    
    ''' items '''
    ''' getters '''
    def get_all_items(self):
        self.cur.execute("SELECT * FROM ITEMS;")
        return self.cur.fetchall()

    def get_item(self, item_id: int):
        self.cur.execute("SELECT * FROM ITEMS WHERE ITEM_ID="+str(item_id)+";")
        return self.cur.fetchone()

    def get_item_by_barcode(self, barcode: str):
        # in gui, if barcode not found, prompt for price & update db accordingly. Update as event or soemthing
        self.cur.execute("SELECT * FROM ITEMS WHERE BARCODE='"+barcode+"';")
        item = self.cur.fetchone()
        if( item ):
            return (int(item[0]), float(item[1]), float(item[2]), float(item[3]),
                    str(item[4]), str(item[5]), str(item[6]), float(item[7]))
        else:
            return None
    
    ''' unimplemented 
    def get_item_stock(self, item_id):
    def get_item_cost(self, item_id):
    def get_item_price(self, item_id):
    def get_item_barcode(self, item_id):
    def get_item_units(self, item_id):
    def get_item_name(self, item_id):
    def get_item_tax(self, item_id):
    def get_items_where_name_like(self, partial_name:str):
        end inimplemented '''
    ''' end getters '''

    ''' insert '''
    def add_item(self, stocked_quantity:float, cost:float, price:float, 
                    barcode:str, units:str, name:str, tax:float):
        self.cur.execute("INSERT INTO ITEMS(stocked_quantity, cost, price, barcode,"+
                         "units, name, tax_rate) VALUES ('"+str(stocked_quantity)+"',"+
                         str(cost)+","+str(price)+",'"+barcode+"','"+units+"','"+name+"',"+
                         str(tax)+");")
        self.conn.commit()

    def alert_new_item(self):
        return None

    ''' end insert '''
    ''' end items '''

    ''' orders '''
    def get_order(self, order_id):
        return None
    def add_order(self, item_ids: List, item_quantities: List, pay_method: int):
        #update stocked item quantities also
        #date
        return None
    
    def get_order_items(self, order_id):
        return 
    ''' end orders '''

    def get_price_history(self, item_id):
        return None

class DB_App:
    
    def __init__(self, window=None):
        self.db_c = DB_Connector()
        self.is_sub_app = bool(window)
        if window:
            self.window = window
            for i in self.window.pack_slaves():
                i.forget()
        else:    
            self.window = tk.Tk()
            self.setup()
        
        self.app_frame = tk.Frame(self.window)
        self.app_frame.pack(fill="both",expand=1)
        self.create_widgets()
        # will this break main app? also how 2 fix
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

    def create_widget(self, name, row_, col):
        label = tk.Label(self.data_entry_frame, text=name)
        text_box = tk.Entry(self.data_entry_frame)
        text_box.config(state='normal')
        label.grid(row=row_,column=col)
        text_box.grid(row=row_+1,column=col)
        self.entries[name] = text_box

    def create_widgets(self):
        self.header = tk.Label(self.app_frame,text='DB APP', font=('Arial',36))
        
        self.data_entry_frame_outer = tk.Frame(self.app_frame)
        self.data_entry_frame = tk.Frame(self.data_entry_frame_outer)

        self.entries = {'name':None, 'stocked quantity':None, 'cost':None, 'price':None,
                 'barcode':None, 'units':None, 'tax rate':None}
        r = c = 1
        for key in self.entries.keys():
            if r%2==0:
                self.create_widget(key, r-1, c)
            else:
                self.create_widget(key, r, c)
            r += 1
            c = c*-1 + 3 # :)

        # submit button
        self.add_button = tk.Button(self.data_entry_frame, text='add item',
                        command=self.add_item)
        '''
        stocked_quantity:float, cost:float, price:float, 
                    barcode:str, units:str, name:str, tax:float)
        '''
        self.add_button.grid(row=9, column=1)
        self.quit_button = tk.Button(self.data_entry_frame, text='quit', fg='RED',
                            command=self.quit)
        self.quit_button.grid(row=9,column=2)
           

        self.header.pack(fill="x")
        self.data_entry_frame.place(relx=.5,rely=.5, anchor=tk.CENTER)
        self.data_entry_frame_outer.pack(fill="both", expand=1)
        
    
    #add item
    def add_item(self):
        self.db_c.add_item(float(self.entries['stocked quantity'].get()),
             float(self.entries['cost'].get()), float(self.entries['price'].get()),
             self.entries['barcode'].get(), self.entries['units'].get(),
             self.entries['name'].get(), float(self.entries['tax rate'].get()))

    def print_entries(self):
        for k,v in self.entries.items():
            print(k, v.get())

    def quit(self): 
        if self.is_sub_app:
            self.app_frame.destroy()
            self.window.children['!frame'].pack(fill='both', expand=1)
        else:
            self.window.destroy()
    

    ''' 
        reports, maybe add construct & view methods
        item quantity sold, type of item sold, profit by item,
        total profit, total tax, total profit by payment method, 
        total tax by payment method
    
    unimplemented
       
    def daily_report(self):
    def weekly_report(self):
    def monthly_report(self):
    def quarterly_report(self):
    def annual_report(self):
    
    end unimplemented '''
    '''end reports '''

if __name__=='__main__':
    dba = DB_App()
    #db_c = DB_Connector()
    #test = input()
    #print(test)
    #print(db_c.get_item_by_barcode(test))
