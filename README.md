# simukeyboard
利用 win32 做的簡單的模擬鍵盤輸入

SIMUKEYBOARD()
clicks(keyNo, times = 1, ms = 100)
連擊 keyNo 次數 times 間隔 ms 

clickTwoKeys(keyNo1, keyNo2, endWaitSec = 0)
單擊 keyNo1 + keyNo2 之後等待 endWaitSec 

pressTwoKeys(self, keyNo1, keyNo2, pressSec = 1, endWaitSec = 0)
壓下 keyNo1 + keyNo2 後 pressSec 時彈起 之後等待 endWaitSec 

mouseMove(pos, endWaitSec = 0)
移動滑鼠到 pos:(x, y) 之後等待 endWaitSec 

mouseLeftClick(pos = (None, None), endWaitSec = 0)
移動滑鼠到 pos:(x, y) 點擊滑鼠左鍵 之後等待 endWaitSec 

mouseRightClick(pos = (None, None), endWaitSec = 0)
移動滑鼠到 pos:(x, y) 點擊滑鼠右鍵 之後等待 endWaitSec 

鍵盤碼參考：https://home.gamer.com.tw/creationDetail.php?sn=4106256
