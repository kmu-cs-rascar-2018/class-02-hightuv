#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import vlc
import time
from SR02 import SR02_Supersonic as Supersonic_Sensor

class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        self.track_last = [0,0,0,0,0]
        # 음원 재생을 위한 처리
        self.instance = vlc.Instance()
        # 플레이어 생성
        self.player = self.instance.media_player_new()
        # 음량 설정
        self.player.audio_set_volume(100)
        # 오디오 파일 로드
        self.sounds = [self.instance.media_new_path('smb_1-up.wav'), self.instance.media_new_path('smb2_bonus_chance_start.wav'),
                       self.instance.media_new_path('smb_coin.wav'), self.instance.media_new_path('smb_flagpole.wav'),
                       self.instance.media_new_path('smb_powerup.wav'), self.instance.media_new_path('smb_world_clear.wav'),
                       self.instance.media_new_path('smb_stomp.wav')]

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================
    def t_parking(self):
        self.player.stop()
        self.player.set_media(self.sounds[5])
        self.player.play()
        self.car.steering.turn(90)
        self.car.accelerator.go_forward(60)
        time.sleep(1.8)
        self.car.accelerator.stop()
        time.sleep(0.1)
        self.car.steering.turn(35)
        self.car.accelerator.go_backward(55)
        time.sleep(0.4)
        while self.car.line_detector.read_digital() != [0,0,1,0,0]:
            self.car.steering.turn(35)
            self.car.accelerator.go_backward(60)
        self.car.steering.turn(90)
        self.car.accelerator.stop()

    
    def drive_back(self):
        while self.car.line_detector.read_digital() == [0,0,0,0,0]:
            self.car.steering.turn(145)
            time.sleep(0.01)
            self.car.accelerator.go_backward(80)
            time.sleep(0.01)
        self.car.steering.turn(35)
        time.sleep(0.01)
        self.car.accelerator.go_forward(80)
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
            pass

    def colordiff(self):
        color_list = self.car.color_getter.get_raw_data()
        print(color_list)
        #Yellow
        if color_list[0] > 1000 and color_list[1] > 1000 and 400 < color_list[2] < 750:
            print("Yellow")
            if self.player.get_media() == self.sounds[2]:
                return
            # 음원 정지후 재생
            self.player.stop()
            self.player.set_media(self.sounds[2])
            self.player.play()

        #Red
        elif 500 < color_list[0] < 1024 and 140 < color_list[1] < 280 and 150 < color_list[2] < 320:
            print("Red")
            self.count += 1
            time.sleep(0.2)
            self.player.stop()
            self.player.set_media(self.sounds[4])
            self.player.play()
        #Green
        elif 250 < color_list[0] < 480 and 690 < color_list[1] <= 1024 and 350 < color_list[2] < 670:
            print("Green")
            if self.player.get_media() == self.sounds[0]:
                return
            self.player.stop()
            self.player.set_media(self.sounds[0])
            self.player.play()

        #Blue
        elif 130 < color_list[0] < 700 and 450 < color_list[1] < 900 and 800 < color_list[2] <= 1024:
            print("Blue")
            if self.player.get_media() == self.sounds[3]:
                return
            self.player.stop()
            self.player.set_media(self.sounds[3])
            self.player.play()

        #Orange
        elif 900 < color_list[0] <= 1024 and 500 < color_list[1] < 800 and 250 < color_list[2] < 510:
            print("Orange")
            if self.player.get_media() == self.sounds[6]:
                return
            self.player.stop()
            self.player.set_media(self.sounds[6])
            self.player.play()


    def car_startup(self):

        # implement the assignment code here
        
        self.car.steering.turn(90)
        
        distance_detector = Supersonic_Sensor.Supersonic_Sensor(35)

        self.count = 0
        self.player.set_media(self.sounds[1])
        self.player.play()
        is_stop = False
        try:
            while True:
                track = self.car.line_detector.read_digital()
                color = self.car.color_getter.get_raw_data()
                if distance_detector.get_distance() > 10:
                    self.colordiff()
                    self.car.accelerator.go_forward(45)
                    if is_stop:
                        is_stop = False
                        self.player.play()
                        self.car.accelerator.go_forward(50)
                    time.sleep(0.01)
                    self.linetrace()
                    time.sleep(0.05)
                elif distance_detector.get_distance() <= 10 and distance_detector.get_distance() > 0:
                    self.car.accelerator.stop()
                    time.sleep(0.1)
                    if not is_stop:
                        is_stop = True
                        self.player.stop()
                else:
                    pass


                if self.count == 2:
                    self.car.accelerator.stop()
                    break
            self.t_parking()
            self.car.drive_parking()
        except:
            self.car.accelerator.stop()
            time.sleep(0.3)
            
            
if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()
    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.accelerator.stop()
        myCar.drive_parking()
