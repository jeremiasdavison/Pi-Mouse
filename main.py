import board
import digitalio
import usb_hid
import time as t
from adafruit_hid.mouse import Mouse

#print(dir(board))
button0 = digitalio.DigitalInOut(board.GP10)
button0.direction = digitalio.Direction.INPUT
button0.pull = digitalio.Pull.UP

button1 = digitalio.DigitalInOut(board.GP20)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

LEFT_BUTTON = 1
m = Mouse(usb_hid.devices) #creamos un objeto de mouse, para luego utilizarlo en el main() 
#print(button0.value())
def main():
    if not button0.value or not button1.value:
        print('Button pressed!')
        m.click(Mouse.LEFT_BUTTON)
        t.sleep(0.5)
    else:
        led.value = True
        
while True:
    main()
