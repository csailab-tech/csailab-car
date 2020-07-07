 
import web 
import LED
import headsetup
import bearingsetup
import move
import frontwheelsetup
import time
import numpy as np
import base64
import os




move.setup()
led=LED.LED()


render = web.template.render('templates/')

urls = ( 
'/', 'index' ,
'/hello','hello',
'/img','img',
'/led','led',
'/video','video'
) 

#app = web.application(urls, globals()) 

'''class index: 
    def GET(self):
        name = 'hello'
        return render.index(name)'''

class index:
    def GET(self):
        name = 'action'
        return render.index(name)
        #return u"hello"

class video:
    def GET(self):
        name = 'video'
        return render.video()
    def POST(self):
        name = web.input().name
        capture = cv2.VideoCapture(0)
        while True:
            ret, frame = capture.read()
            encoded, buffer = cv2.imencode('.jpg', frame)
            message = base64.b64encode(buffer)
            cv2.waitKey(1)
            if name == 'videoff':
                break
        #camera.framerate = 20
        #rawCapture = PiRGBArray(camera, size=(640, 480))

        '''for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        
            frame_image = frame.array
            encoded, buffer = cv2.imencode('.jpg', frame_image)
            jpg_as_text = base64.b64encode(buffer)

            rawCapture.truncate(0)
            cv2.waitKey(1)'''
        message="message"
        return render.index(message)

class hello:
    def GET(self):
        return u"hello hello"
    def POST(self):
        #return web.input()
        #speed = 45
        name = web.input().name

        if name == "start":
            speed = web.input().range
            move.move(int(speed),'forward')
        elif name == "stop":
            move.motorStop()
        elif name == "videon":
            os.system('python3 /usr/local/csailab-car/webcamera.py')
        elif name == "videoff":
            os.system('pkill -f webcamera.py')
        elif name == "ledon":
            select = web.input().select
            if select == "Rainbow":
                led.rainbow()
                led.colorWipe(0,0,0)
            elif select == "Police":
                led.police()
                led.police()
            elif select == "Green":
                led.colorWipe(0,255,0)
            elif select == "Red":
                led.colorWipe(255,0,0)
        elif name == "ledoff":
            led.colorWipe(0,0,0)
        elif name == "headup":
            headsetup.turn_ctrl('up')
        elif name == "headmiddle":
            headsetup.turn_ctrl('middle')
        elif name == "headdown":
            headsetup.turn_ctrl('down')
        elif name == "bearingleft":
            bearingsetup.turn_ctrl('left')
        elif name == "bearingmiddle":
            bearingsetup.turn_ctrl('middle')
        elif name == "bearingright":
            bearingsetup.turn_ctrl('right')
        elif name == "forward":
            speed = web.input().speed
            move.move(int(speed),'forward')
            #time.sleep(0.5)
        elif name == "backward":
            move.motorStop()
            speed = web.input().speed
            move.move(int(speed),'backward')
            time.sleep(0.5)
        elif name == "left":
            frontwheelsetup.turn_ctrl('left')
            #move.move(speed,'forward')
            #time.sleep(0.5)
        elif name == "right":
            frontwheelsetup.turn_ctrl('right')
            #move.move(speed,'forward')
            #time.sleep(0.5)
        elif name == "middle":
            frontwheelsetup.turn_ctrl('middle')
            #move.move(speed,'forward')
            #time.sleep(0.5)
        elif name == "findlineon":
            #speed = web.input().speed
            speed = web.input().range1
            os.system('python3 /usr/local/csailab-car/findline.py %s' % (speed))
        elif name == "findlineoff":
            os.system('pkill -f findline.py')
        #move.motorStop()
        return render.index(name)

if __name__ == "__main__":
    app = web.application(urls, globals()) 
    app.run() 
