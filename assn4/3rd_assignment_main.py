#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time
from SR02 import SR02_Supersonic as Supersonic_Sensor

class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================
    def drive_back(self):
        while self.car.line_detector.read_digital() == [0,0,0,0,0]:
            self.car.steering.turn(145)
            time.sleep(0.01)
            self.car.accelerator.go_backward(90)
            time.sleep(0.01)
        self.car.steering.turn(35)
        time.sleep(0.01)
        self.car.accelerator.go_forward(95)
        time.sleep(0.2)


    def linetrace(self):
        track = self.car.line_detector.read_digital()
       
        if track == [1,0,0,0,0]:
            self.car.steering.turn(60)
            
        elif track == [0,1,0,0,0]:
            self.car.steering.turn(75)
            
        elif track == [0,0,1,0,0]:
            self.car.steering.turn(90)
            
        elif track == [0,0,0,1,0]:
            self.car.steering.turn(105)
            
        elif track == [0,0,0,0,1]:
            self.car.steering.turn(110)
            
        elif track == [1,1,0,0,0]:
            self.car.steering.turn(60)
            
        elif track == [0,1,1,0,0]:
            self.car.steering.turn(75)
            
        elif track == [0,0,1,1,0]:
            self.car.steering.turn(105)
            
        elif track == [0,0,0,1,1]:
            self.car.steering.turn(120)
            
        elif track == [0,0,0,0,0]:
            self.drive_back()
        elif track == [1,1,1,1,1]:
            self.count += 1
            time.sleep(0.3)

    def car_startup(self):

        # implement the assignment code here
        
        self.car.steering.turn(90)
        
        distance_detector = Supersonic_Sensor.Supersonic_Sensor(35)

        self.count = 0
        try:
            while True:
                track = self.car.line_detector.read_digital()
            
                if distance_detector.get_distance() > 23:
                    self.car.accelerator.go_forward(50)
                    time.sleep(0.01)
                    self.linetrace()
                    time.sleep(0.05)
                
                elif distance_detector.get_distance() <= 23 and distance_detector.get_distance() > 0:
                    self.car.steering.turn(35)
                    time.sleep(0.01)
                    self.car.accelerator.go_forward(45)
                    time.sleep(1)
                    while True:
                        self.car.steering.turn(90)
                        time.sleep(0.01)
                        self.car.accelerator.go_forward(55)
                        if 1 in self.car.line_detector.read_digital():
                            self.car.accelerator.stop()
                            break
                    self.car.steering.turn(145)
                    time.sleep(0.01)
                    self.car.accelerator.go_forward(60)
                    time.sleep(1.2)
                    while True:
                        self.car.steering.turn(90)
                        time.sleep(0.01)
                        self.car.accelerator.go_forward(50)
                        if 1 in self.car.line_detector.read_digital():
                            self.car.accelerator.stop()
                            break
                else:
                    pass


                if self.count == 2:
                    self.car.accelerator.stop()
                    break
        except:
            self.car.accelerator.stop()
            time.sleep(0.3)
            self.car_startup()
            
if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.accelerator.stop()
        myCar.drive_parking()
