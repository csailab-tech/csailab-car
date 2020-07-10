#!/usr/bin/python3
# File name   : findline.py
# Description : line tracking 
# Website     : www.adeept.com
# Author      : William
# Date        : 2019/11/21
import RPi.GPIO as GPIO
import time
import sys
import move
import frontwheelsetup

line_pin_right = 19
line_pin_middle = 16
line_pin_left = 20

turn_status = 0
speed=int(sys.argv[1])
#speed = 65
black = 0
left = 0
right = 0
cover =0
i = 0

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(line_pin_right,GPIO.IN)
    GPIO.setup(line_pin_middle,GPIO.IN)
    GPIO.setup(line_pin_left,GPIO.IN)
    #motor.setup()

def actue_angle():
    frontwheelsetup.turn_ctrl('right')
    move.move(speed, 'backward')
    time.sleep(1)
    frontwheelsetup.turn_ctrl('left')
    move.move(speed, 'forward')
    time.sleep(0.2)
    frontwheelsetup.turn_ctrl('right')
    move.move(speed, 'backward')
    time.sleep(1)
    frontwheelsetup.turn_ctrl('left')
    move.move(speed, 'forward')
    time.sleep(1)
    frontwheelsetup.turn_ctrl('right')
    move.move(speed, 'backward')
    time.sleep(1)
    frontwheelsetup.turn_ctrl('left')
    move.move(speed, 'forward')
    time.sleep(1)
    print('aa down')

def run(speed):
    global turn_status, black, left, right , i, cover 
    status_right = GPIO.input(line_pin_right)
    status_middle = GPIO.input(line_pin_middle)
    status_left = GPIO.input(line_pin_left)
    print('R%d   M%d   L%d'%(status_right,status_middle,status_left))
    print(turn_status,left,right)
    
    if status_middle == 1:
        print('middle')
        #led.colorWipe(255,255,255)
        if turn_status != 0:
            frontwheelsetup.turn_ctrl('middle')
            turn_status = 1
        if status_left == 1 and status_right == 1:
            if cover == 1:
                i = i + 1
            else:
                i = 1;
            print('i :', i)
            #10 80
            if i > 80:
                sys.exit()
            cover = 1
        move.move(speed, 'forward')
        # time.sleep(0.2)
    elif status_left == 1:
        print('right')
        #led.colorWipe(0,0,255)
        if black == 1 or turn_status != 2:
            right =1
        if right > 100:
            frontwheelsetup.turn_n(130)
            move.move(speed, 'backward')
            time.sleep(0.5)
            print('big right')
            right = 0
        else:
            frontwheelsetup.turn_ctrl('right')
            move.move(speed, 'forward')
        right = right + 1
        turn_status = 2
        back = 0

    elif status_right == 1:
        print('left')
        #led.colorWipe(0,255,0)
        if black == 1 or turn_status != 3:
            left = 1
        if left >100:
            frontwheelsetup.turn_n(-145)
            move.move(speed, 'backward')
            time.sleep(0.5)
            print('big left')
            left = 0
        else:
            frontwheelsetup.turn_ctrl('left')
            move.move(speed, 'forward')
        left = left + 1
        turn_status = 3
        back = 0
    
    else:
        print('none')
        #led.colorWipe(255,0,0)
        if turn_status == 2:
            frontwheelsetup.turn_ctrl('left')
            move.move(speed, 'backward')
            time.sleep(0.6)
            frontwheelsetup.turn_ctrl('right')
            move.move(speed, 'forward')
            time.sleep(0.6)
        elif turn_status == 3:
            #actue_angle()
            frontwheelsetup.turn_ctrl('right')
            move.move(speed, 'backward')
            time.sleep(0.6)
            frontwheelsetup.turn_ctrl('left')
            move.move(speed, 'forward')
            time.sleep(0.6)
        else:
            move.move(speed, 'backward')
            time.sleep(0.5)
        '''print('backward start :')
        while 1:
            move.move(speed, 'backward')
            black = 1
            status_right = GPIO.input(line_pin_right)
            status_middle = GPIO.input(line_pin_middle)
            status_left = GPIO.input(line_pin_left)
            print('R%d   M%d   L%d'%(status_right,status_middle,status_left))
            if status_middle == 1:
                print('backward over')
                break'''
        black = 1



if __name__ == '__main__':
    try:
        setup()
        move.setup()
        
        while 1:
            run(speed)
            pass
    except KeyboardInterrupt:
        move.destroy()


