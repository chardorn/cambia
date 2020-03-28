from PiMotor import Motor
import time
import keyboard
m1 = Motor("MOTOR1",1)
m2 = Motor("MOTOR2",1)

m1.forward(5)
m2.forward(5)
#time.sleep(15)
m1.stop()
m2.stop()

while True:#making a loop
    try: #used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):#if key 'q' is pressed 
            print('You Pressed A Key!')
            break#finishing the loop
        else:
            pass
