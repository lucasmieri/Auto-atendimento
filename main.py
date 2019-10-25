""" A project by: Future Club members
*******************************************************
*************** We started at:12/10/2019 **************
********************* Developers: *********************
********************* Muriel Costa ********************
**********************            ********************* #put your name here
**********************            *********************
**********************            *********************  
**********************            *********************
*******************************************************
*******************************************************
"""

#testinhuuuu
import lcd
import time
import keyboard




def deposit(): #to do
    lcd.lcd_write("FLUXOGRAMA DE", "DEPOSITO")
    time.sleep(2)       # wait 2 seconds

def main():
    while True: #infinite loop
        last_time = 0
        if (time.time() - last_time) > 500:  # 500 milliseconds == 1/2 second.  1000 milliseconds == 1 second.
            last_time = time.time()
            lcd.lcd_write("FUTURE CLUB!", "APERTE ENTER")

        if keyboard.is_pressed("enter"):
            deposit()


if __name__ == "__main__":  #if program was executed by user.
    main()
