import cv2
import numpy as np
import mss

class screen_shot:
    
    def monitor_size(top,left,width,height):
        mon_size={"top":top,"left":left,"width":width,"height":height}
        return mon_size
    
    def get_screen(top,left,width,height):
        with mss.mss() as sct:
            image=np.array(sct.grab(screen_shot.monitor_size(top,left,width,height)))
            return image

    def show_image(window_name,top,left,width,height):
        cv2.imshow(window_name,screen_shot.get_screen(top,left,width,height))
        
    def show_continusly(window_name,top,left,width,height):
        while True: 
            screen_shot.show_image(window_name,top,left,width,height)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break
            
    def get_screen_continusly(top,left,width,height):
        while True:
            screen_shot.get_screen(top,left,width,height)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break
