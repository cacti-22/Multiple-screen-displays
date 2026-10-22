import keyboard
from screen_shot import *

class colour_detection:
    
    def red(top,left,width,height):
        lower_red=np.array([0,120,20])
        upper_red=np.array([10,255,255])
        first_mask=None
        while True:
            image = screen_shot.get_screen(top,left,width,height)
            image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
            mask= cv2.inRange(image,lower_red,upper_red)
            if first_mask is not None:
                diff=cv2.absdiff(mask,first_mask)
                diff=cv2.countNonZero(diff)
                if diff>500:
                    keyboard.press_and_release("s+up")
                    ptint("red")
            first_mask=mask.copy()
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break
            
    def green(top,left,width,height):
        lower_green=np.array([40, 52, 20])
        upper_green=np.array([102, 255, 255])
        first_mask=None
        while True:
            image = screen_shot.get_screen(top,left,width,height)
            image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
            mask= cv2.inRange(image,lower_green,upper_green)
            if first_mask is not None:
                diff=cv2.absdiff(mask,first_mask)
                diff=cv2.countNonZero(diff)
                if diff>500:
                    keyboard.press_and_release("a+up")
                    print("green")
            first_mask=mask.copy()
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break
            
    def yellow(top,left,width,height):
        lower_yellow=np.array([20, 100, 20])
        upper_yellow=np.array([35, 255, 255])
        first_mask=None
        while True:
            image = screen_shot.get_screen(top,left,width,height)
            image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
            mask= cv2.inRange(image,lower_yellow,upper_yellow)
            if first_mask is not None:
                diff=cv2.absdiff(mask,first_mask)
                diff=cv2.countNonZero(diff)
                if diff>500:
                    keyboard.press_and_release("d+up")
                    print("yellow")
            first_mask=mask.copy()
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break
