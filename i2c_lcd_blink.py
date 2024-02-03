import time
import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd()

while True:
    mylcd.lcd_display_string(u"Hello world!")
    time.sleep(0.3)
    mylcd.lcd_clear()
    time.sleep(0.3)

