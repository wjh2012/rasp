from RPLCD.i2c import CharLCD
import time
import datetime
lcd = CharLCD('PCF8574', 0x27)

try:
    while True:
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')
        nowTime = now.strftime('%H:%M:%S')
        print(now, nowDate, nowTime)
        time.sleep(1)
        lcd.clear()
        lcd.cursor_pos = (0,3)
        lcd.write_string(nowDate)
        lcd.crlf()
        lcd.cursor_pos = (1,4)
        lcd.write_string(nowTime)
    
except KeyboardInterrupt:
    lcd.clear()
        