from machine import Pin, I2C
import ssd1306

i2c = I2C(1, sda=Pin(18), scl=Pin(19))
display = ssd1306.SSD1306_I2C(128, 32, i2c)
display.text('Hello World', 0, 16)
#display.text(5 + 5, 0, 16)
display.show()