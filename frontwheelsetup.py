#!/usr/bin/env python3
# File name   : frontwheelsetup.py
# Description : Setup front wheel
# Author      : Koki GU
# Date        : 2019/12/13
import time
import Adafruit_PCA9685

pwm0_direction = -1

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#pwm0_init = 300
#pwm0_max  = 450
#pwm0_min  = 150
pwm0_init = 300
pwm0_max  = 450
pwm0_min  = 150
pwm0_pos  = pwm0_init

turn_range = 80

def turn_ctrl(direction):
    if direction == 'left':
        pwm.set_pwm(0, 0, pwm0_pos + 100*pwm0_direction)
    elif direction == 'right':
        pwm.set_pwm(0, 0, pwm0_pos - turn_range*pwm0_direction)
    elif direction == 'middle':
        pwm.set_pwm(0, 0, pwm0_pos)
def turn_n(turn_range):
    pwm.set_pwm(0, 0, pwm0_pos + turn_range*pwm0_direction)

def clean_all():
	global pwm
	pwm = Adafruit_PCA9685.PCA9685()
	pwm.set_pwm_freq(50)
	pwm.set_all_pwm(0, 0)

if __name__ == '__main__':
    #init
    clean_all()
    turn_ctrl('left')
    print(pwm0_pos + turn_range*pwm0_direction)
    time.sleep(1)
    turn_ctrl('middle')
    print(pwm0_pos)
    time.sleep(1)
    turn_ctrl('right')
    print(pwm0_pos - turn_range*pwm0_direction)
    time.sleep(1)
    turn_ctrl('middle')
    print(pwm0_pos)
    time.sleep(1)
    '''turn_n(50)
    time.sleep(1)
    turn_n(20)
    time.sleep(1)'''

#    turn_ctrl('left')
    
    
    #first time, comment the line above, and run the line below to get the middle, left max, right max value
    #pwm.set_pwm(0, 0, 300)
    clean_all()
    pass

