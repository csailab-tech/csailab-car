#!/usr/bin/env python3
# File name   : headsetup.py
# Description : Setup robot head
# Author      : Koki GU
# Date        : 2019/12/13
import time
import Adafruit_PCA9685

pwm2_direction = 1

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#pwm2_init = 300
#pwm2_max  = 500
#pwm2_min  = 100
#pwm2_pos  = pwm2_init
pwm2_init = 200
pwm2_max  = 500
pwm2_min  = 100
pwm2_pos  = pwm2_init

turn_range = 100
findline = 45

def turn_ctrl(direction):
    if direction == 'up':
        pwm.set_pwm(2, 0, pwm2_pos + turn_range*pwm2_direction)
    elif direction == 'down':
        pwm.set_pwm(2, 0, pwm2_pos - turn_range*pwm2_direction)
    elif direction == 'middle':
        pwm.set_pwm(2, 0, pwm2_pos)
    elif direction == 'findline_up':
        pwm.set_pwm(2, 0, pwm2_pos - findline*pwm2_direction)

def clean_all():
    global pwm
    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)
    pwm.set_all_pwm(0, 0)

if __name__ == '__main__':
    #init
    clean_all()
    '''turn_ctrl('findline_up')
    print(pwm2_pos - findline*pwm2_direction)
    time.sleep(1)'''
    turn_ctrl('down')
    time.sleep(1)
    print(pwm2_pos - turn_range*pwm2_direction)
    turn_ctrl('middle')
    print(pwm2_pos)
    time.sleep(1)
    turn_ctrl('up')
    time.sleep(1)
    print(pwm2_pos - turn_range*pwm2_direction)
    turn_ctrl('middle')
    print(pwm2_pos)
    time.sleep(1)
    clean_all()
    #first time, comment the line above, and run the line below to get the middle, up max, down max value
   # pwm.set_pwm(2, 0, 350)
#    clean_all()
    pass



