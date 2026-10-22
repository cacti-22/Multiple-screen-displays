from colour_detection import *
from screen_shot import *
import threading
class threads:
    def create_threads_show(window_name,top,left,width,height):
        t1=threading.Thread(target=screen_shot.show_continusly,args=(window_name,top,left,width,height))
        return t1
    
    def start_threads_show(amount_of_threads):
        thread=[]
        for i in range(amount_of_threads):
            window_name=input("Enter the window name ")
            top=int(input("Enter the top starting point "))
            left=int(input("Enter the left starting point "))
            width=int(input("Enter the width of the screen "))
            height=int(input("Enter the height of the screen "))
            t=threads.create_threads_show(window_name,top,left,width,height)
            thread.append(t)
            print("\n")
        for t in thread:
            t.start()
        for t in thread:
            t.join()
        
    def create_threads_red():
        t1=threading.Thread(target=colour_detection.red,args=(1800,1500,300,50))
        return t1
    
    def create_threads_green():
        t1=threading.Thread(target=colour_detection.green,args=(1800,1300,200,50))
        return t1
    
    def create_threads_yellow():
        t1=threading.Thread(target=colour_detection.yellow,args=(1700,1800,300,50))
        return t1
    
    def start_threads():
        t1=threads.create_threads_red()
        t2=threads.create_threads_green()
        t3=threads.create_threads_yellow()
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
