import utime
import machine

led = machine.Pin("LED", machine.Pin.OUT)

while True:
    led.on()  # Turn LED on
    utime.sleep(0.5)  # Wait for 2 seconds

    led.off()  # Turn LED off
    utime.sleep(0.5)  # Wait for 2 seconds
