#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#File: HomeTemp.py
#Author: Ville Rytinki 
# 
#Description: This file is the main interface for the HomeTemp system.  
# 
# Version 1.0


import sys
sys.path.append("/home/pi/Documents") 
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd
import time
import datetime
from temp_sensor import TempSensor as tmp

#setup the Rasberry Pi pins
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D27)
lcd_d6 = digitalio.DigitalInOut(board.D22)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_backlight = digitalio.DigitalInOut(board.D20)

#Determine the rows and columns for 1602 LCD display
lcd_colums = 16
lcd_rows = 2

#create the LCD element
lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5,
                                lcd_d6, lcd_d7, lcd_colums, lcd_rows, 
                                lcd_backlight)
    
    
'''This function prints Goodbye to the screen and
 clears the display when called, finally display LED backlight is turned off'''
def exitProgram():
        lcd.clear()
        lcd.message = "Goodbye."
        time.sleep(2)
        lcd.clear()
        lcd.backlight = False
        print("\nProgram closed.") 

def main():
    #setup the display and the required variables
    lcd.clear()
    lcd.backlight = True

    time.sleep(3)

    previous_minute = 0 
          
    while (True):
        try:
        
            date = datetime.datetime.now()
        
            current_minute = date.strftime("%M")
        
            if current_minute != previous_minute:
    
                temperature = tmp.read_temp()
                lcd.message = "{}\nTemperature:{} C".format(date, "%2.f" % temperature)
                previous_minute = current_minute

        
        except KeyboardInterrupt:
            exitProgram()
            break;
    
if __name__=="__main__":
    main()
