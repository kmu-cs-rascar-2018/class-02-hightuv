#########################################################################
# Date: 2018/10/02
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################

from car import Car
import time
import front_wheels
import rear_wheels
from SR02 import SR02_Supersonic as Supersonic_Sensor

class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        # Implement the assignment code here.
        direction_controller = front_wheels.Front_Wheels()
        direction_controller.center_alignment()
        time.sleep(1)
        driving_controller = rear_wheels.Rear_Wheels()
        driving_controller.ready()
        detector = Supersonic_Sensor.Supersonic_Sensor(35)
                
        done = False
        limit = 15
        speed = 30
        a = limit
        count = 0

        while done == False:
            front_wheels.Front_Wheels().center_alignment()
            while detector.get_distance() > a:
                driving_controller.go_forward(speed)
            if detector.get_distance() <= a:
                if detector.get_distance() < 0:
                    continue
                driving_controller.stop()
                time.sleep(2)
                driving_controller.go_backward(speed)
                time.sleep(4)
                driving_controller.stop()
                time.sleep(1)
                speed += 20
                limit += 5
                count += 1
                a = limit + 5*count
                
            if limit > 25:
                driving_controller.stop()
                done = True

if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
