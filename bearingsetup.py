#!/usr/bin/env python3
# File name   : bearingsetup.py
# Description : Setup bearing base
# Author      : Koki GU
# Date        : 2019/12/13
import time
import Adafruit_PCA9685

pwm1_direction = 1

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#pwm1_init = 300
#pwm1_max  = 500
#pwm1_min  = 100
#pwm1_pos  = pwm1_init
pwm1_init = 320
pwm1_max  = 500
pwm1_min  = 100
pwm1_pos  = pwm1_init

turn_range = 120

def turn_ctrl(direction):
	if direction == 'left':
		pwm.set_pwm(1, 0, pwm1_pos + turn_range*pwm1_direction)
	elif direction == 'right':
		pwm.set_pwm(1, 0, pwm1_pos - turn_range*pwm1_direction)
	elif direction == 'middle':
		pwm.set_pwm(1, 0, pwm1_pos)

def clean_all():
	global pwm
	pwm = Adafruit_PCA9685.PCA9685()
	pwm.set_pwm_freq(50)
	pwm.set_all_pwm(0, 0)

if __name__ == '__main__':
    #init
    clean_all()
    turn_ctrl('left')
    print(pwm1_pos + turn_range*pwm1_direction)
    time.sleep(1)
    turn_ctrl('middle')
    print(pwm1_pos)
    time.sleep(1)
    turn_ctrl('right')
    print(pwm1_pos - turn_range*pwm1_direction)
    time.sleep(1)
    turn_ctrl('middle')
    print(pwm1_pos)
    time.sleep(1)
    clean_all()
    #first time, comment the line above, and run the line below to get the middle, left max, right max value
    #print(pwm1_pos)
    #pwm.set_pwm(1, 0, 330)
    pass


