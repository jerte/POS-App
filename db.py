import psycopg2
import os
from typing import *

class DB_Connector:
    def __init__(self):
        self.conn = psycopg2.connect(str(os.environ['CONN']))
        self.cur = self.conn.cursor()
    ''' items '''
    def get_all_items(self):
        self.cur.execute("SELECT * FROM ITEMS;")
        return self.cur.fetchall()

    def get_item(self, item_id: int):
        self.cur.execute("SELECT * FROM ITEMS WHERE ITEM_ID="+str(item_id)+";")
		return self.cur.fetchone()

    def get_item(self, barcode: str):
        # in gui, if barcode not found, prompt for price & update db accordingly. Update as event or soemthing
        self.cur.execute("SELECT * FROM ITEMS WHERE BARCODE="+barcode+";")
		return self.cur.fetchone()

    def add_item(self, stocked_quantity:float, cost:float, price:float, 
                    barcode:str, units:str, name:str, tax:float):
        self.cur.execute("INSERT INTO ITEMS(stocked_quantity, cost, price, barcode,"+
						 "units, name, tax_rate) VALUES ("+str(stocked_quantity)+","+
						 str(cost)+","+str(price)+","+barcode+","+units+","+name+","+
						 str(tax_rate)+");")
		self.cur.commit()

    def add_item(self, price:float, barcode:str):
        return None
    def alert_new_item(self):
        return None

    def get_item_stock(self, item_id):
        return self.get_item()
    def get_item_cost(self, item_id):
        return self.get_item()
    def get_item_price(self, item_id):
        return self.get_item()
    def get_item_barcode(self, item_id):
        return self.get_item()
    def get_item_units(self, item_id):
        return None
    def get_item_name(self, item_id):
        return None
    def get_item_tax(self, item_id):
        return None
    def get_items_where_name_like(self, partial_name:str):
        return None
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
    def get_price_history(self, item_id):
        return None
    ''' end orders '''

class DB_App:
    def __init__(self):
        self.db_c = DB_Connector()

    ''' 
        reports, maybe add construct & view methods
        item quantity sold, type of item sold, profit by item,
        total profit, total tax, total profit by payment method, 
        total tax by payment method
    '''
    def daily_report(self):
        return None
    def weekly_report(self):
        return None
    def monthly_report(self):
        return None
    def quarterly_report(self):
        return None
    def annual_report(self):
        return None
    ''' end reports '''

if(__name__=='__main__'):
    db = DB_Connector()
    print(db.get_all_items())
