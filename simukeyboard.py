import win32api
import win32con
from time import sleep

class SIMUKEYBOARD():
    def __init__(self):
        return None

    def clicks(self, keyNo, times = 1, ms = 100):
        for _ in range(times):
            win32api.keybd_event(keyNo,0,0,0) 
            win32api.keybd_event(keyNo,0,win32con.KEYEVENTF_KEYUP,0)
            sleep(ms/1000)
        return 1

    def clickEnter(self, times = 1, ms = 100):
        for _ in range(times):
            win32api.keybd_event(13,0,0,0)  #Enter鍵位碼是13
            win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
            sleep(ms/1000)
        return 1

    def clickTwoKeys(self, keyNo1, keyNo2, endWaitSec = 0):
        win32api.keybd_event(keyNo1,0,0,0)  
        win32api.keybd_event(keyNo2,0,0,0) 
        win32api.keybd_event(keyNo1,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(keyNo2,0,win32con.KEYEVENTF_KEYUP,0)
        sleep(endWaitSec)
        return 1

    def altPrtscr(self, endWaitSec = 0):
        win32api.keybd_event(18,0,0,0)  #Alt鍵位碼是18
        win32api.keybd_event(44,0,0,0)  #prtscr鍵位碼是44
        win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(44,0,win32con.KEYEVENTF_KEYUP,0) #釋放按鍵
        sleep(endWaitSec)
        return 1

    def ctrlQ(self, endWaitSec = 0):
        win32api.keybd_event(17,0,0,0)  #Ctrl鍵位碼是17
        win32api.keybd_event(81,0,0,0)  #q鍵位碼是81
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(81,0,win32con.KEYEVENTF_KEYUP,0) #釋放按鍵
        sleep(endWaitSec)
        return 1

    def ctrlW(self, endWaitSec = 0):
        win32api.keybd_event(17,0,0,0)  #Ctrl鍵位碼是17
        win32api.keybd_event(87,0,0,0)  #W鍵位碼是87
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(87,0,win32con.KEYEVENTF_KEYUP,0) #釋放按鍵
        sleep(endWaitSec)
        return 1

    def ctrlE(self, endWaitSec = 0):
        win32api.keybd_event(17,0,0,0)  #Ctrl鍵位碼是17
        win32api.keybd_event(69,0,0,0)  #E鍵位碼是69
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(69,0,win32con.KEYEVENTF_KEYUP,0) #釋放按鍵
        sleep(endWaitSec)
        return 1

    def mouseRightClick(self, pos = (None, None), endWaitSec = 0):
        """
        按下右鍵，如果有給位置，則先移動滑鼠。
        """
        if not(pos[0] is None and pos[1] is None): win32api.SetCursorPos(pos)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
        sleep(endWaitSec)
        return 1

    def mouseLeftClick(self, pos = (None, None), endWaitSec = 0):
        """
        按下右鍵，如果有給位置，則先移動滑鼠。
        """
        if not(pos[0] is None and pos[1] is None): win32api.SetCursorPos(pos)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        sleep(endWaitSec)
        return 1

    def mouseMove(self, pos, endWaitSec = 0):
        win32api.SetCursorPos(pos)
        sleep(endWaitSec)
        return 1



