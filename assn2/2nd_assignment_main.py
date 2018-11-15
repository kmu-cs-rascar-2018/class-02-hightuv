#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time

class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    
    def car_startup(self):
        # implement the assignment code here
        while True:
            self.car.accelerator.go_forward(70)
            current = self.car.line_detector.read_digital()
            if current == [0,0,0,0,0] or current == [1,1,1,1,1]:
                self.car.accelerator.stop()
                time.sleep(1)
                self.car.accelerator.power_down()
                
                break
            elif current[0] == 1:
                self.car.steering.turn(60)
                time.sleep(0.01)
            elif current[1] == 1:
                self.car.steering.turn(75)
                time.sleep(0.01)
            elif current[3] == 1:
                self.car.steering.turn(105)
                time.sleep(0.01)
            elif current[4] == 1:
                self.car.steering.turn(120)
                time.sleep(0.01)
            elif current[2] == 1:
                self.car.steering.center_alignment()
                time.sleep(0.01)
                
        
	

if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
