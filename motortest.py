from PiMotor import Motor
from PiMotor import LinkedMotors
import time

mset = LinkedMotors (Motor ("MOTOR1",1), Motor ("MOTOR2", 1))
mset.forward(100)
time.sleep(5)
mset.stop()
time.sleep(1)
mset.reverse(100)
time.sleep(5)
mset.stop()
