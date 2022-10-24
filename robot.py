import time
import Jetson.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
class Robot():
 def __init__(self, *args, **kwargs):
  super(Robot, self).__init__(*args, **kwargs)
  self.left_motor = [35,36]
  self.right_motor = [37,38]
  self.left_speed = 0
  self.right_speed = 0
  GPIO.setup(32,GPIO.OUT)
  GPIO.setup(33,GPIO.OUT) 
  self.pwm=[GPIO.PWM(32,50),GPIO.PWM(33,50)]
  GPIO.setup(self.left_motor[0],GPIO.OUT,initial=GPIO.LOW)
  GPIO.setup(self.right_motor[0],GPIO.OUT,initial=GPIO.LOW) 
  GPIO.setup(self.left_motor[1],GPIO.OUT,initial=GPIO.LOW)
  GPIO.setup(self.right_motor[1],GPIO.OUT,initial=GPIO.LOW) 
  self.pwm[0].start(0)
  self.pwm[1].start(0)
def set_motors(self, left_speed=1.0, right_speed=1.0):
  GPIO.output(self.left_motor[0],GPIO.HIGH)
  GPIO.output(self.right_motor[0],GPIO.HIGH) 
  self.left_speed = ((left_speed - (-1))/2)*100
  self.right_speed = ((right_speed - (-1))/2)*100
  print()
  print()
  self.pwm[0].ChangeDutyCycle(self.left_speed)
  self.pwm[1].ChangeDutyCycle(self.right_speed)
    
 def forward(self, speed=1.0, duration=None):
  GPIO.output(self.left_motor[0],GPIO.HIGH)
  GPIO.output(self.right_motor[0],GPIO.HIGH) 
  GPIO.output(self.left_motor[1],GPIO.LOW)
  GPIO.output(self.right_motor[1],GPIO.LOW) 
  self.speed = ((speed - (-1))/2)*100
  self.pwm[0].ChangeDutyCycle(self.speed)
  self.pwm[1].ChangeDutyCycle(self.speed)
def backward(self, speed=1.0):
  GPIO.output(self.left_motor[0],GPIO.LOW)
  GPIO.output(self.right_motor[0],GPIO.LOW) 
  GPIO.output(self.left_motor[1],GPIO.HIGH)
  GPIO.output(self.right_motor[1],GPIO.HIGH) 
  self.speed = ((speed - (-1))/2)*100
  self.pwm[0].ChangeDutyCycle(self.speed)
  self.pwm[1].ChangeDutyCycle(self.speed)
def left(self, speed=1.0):
  GPIO.output(self.left_motor[0],GPIO.LOW)
  GPIO.output(self.right_motor[0],GPIO.HIGH) 
  GPIO.output(self.left_motor[1],GPIO.HIGH)
  GPIO.output(self.right_motor[1],GPIO.LOW) 
  self.speed = ((speed - (-1))/2)*100
  self.pwm[0].ChangeDutyCycle(self.speed)
  self.pwm[1].ChangeDutyCycle(self.speed)
def right(self, speed=1.0):
  GPIO.output(self.left_motor[0],GPIO.HIGH)
  GPIO.output(self.right_motor[0],GPIO.LOW) 
  GPIO.output(self.left_motor[1],GPIO.LOW)
  GPIO.output(self.right_motor[1],GPIO.HIGH) 
  self.speed = ((speed - (-1))/2)*100
  self.pwm[0].ChangeDutyCycle(self.speed)
  self.pwm[1].ChangeDutyCycle(self.speed)
def stop(self):
  GPIO.output(self.left_motor[0],GPIO.LOW)
  GPIO.output(self.right_motor[0],GPIO.LOW) 
  GPIO.output(self.left_motor[1],GPIO.LOW)
  GPIO.output(self.right_motor[1],GPIO.LOW) 
  self.left_speed = 0
  self.right_speed = 0
  self.pwm[0].ChangeDutyCycle(self.left_speed)
  self.pwm[1].ChangeDutyCycle(self.right_speed)
