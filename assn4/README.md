    from car import Car
    import time
    from SR02 import SR02_Supersonic as Supersonic_Sensor
    
위의 3줄의 코드에서 마지막 한 줄을 추가한 이유는 car.py를 통해서 초음파센서를 제어하는 것이 잘 안 됐기 때문입니다.
그래서 직접 import하는 방법을 선택했습니다.

--------------------------------------------------------------------------------------------------------------------------------------
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

위의 drive_back() 함수는 차가 트랙에 머물 수 있도록 하는 함수입니다.
적외선 센서의 인식 값이 [0,0,0,0,0]일 경우에 145도만큼 앞바퀴를 회전하여 차가 90의 속도로 0.01초동안 후진하도록 했습니다.

[0,0,0,0,0]이 아니라 검은 줄을 인식하게 되면 35도만큼 앞바퀴를 회전하여 95의 속도로 차가 0.2초 동안 전진하도록 했습니다.

drive_back()에서 많은 시행착오를 겪었습니다.
전진하는 시간과 후진하는 시간의 비율을 어느 정도로 해야 여러 번 왔다갔다 하지 않을 지에 대해 많이 고민했습니다.
그 결과 제 차에는 위의 코드와 같이 설정하는 게 적합하다고 결론을 내렸습니다.

--------------------------------------------------------------------------------------------------------------------------------------

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

위의 코드는 함수의 이름에서 알 수 있듯이 라인트레이스(linetrace)를 하는 함수입니다.
적외선 센서로부터 오는 리스트의 값에 따라 회전 각과 후진 여부를 정해줬습니다.

마지막의 [1,1,1,1,1]인 경우(정지선을 만난 경우)에 self.count += 1이라는 부분이 있는데, 밑에서 나올 car_startup()에서 self.count = 0이라고 선언을 했습니다.

그리고 뒤의 코드에서 나올 내용이지만 미리 설명을 하자면 self.count의 값이 2가 되면 차가 정지하도록 했습니다.
2바퀴를 도는 것이 이번 과제의 목표이기 때문입니다.

--------------------------------------------------------------------------------------------------------------------------------------

    def car_startup(self)

        # implement the assignment code here
        
        self.car.steering.turn(90)
        
        distance_detector = Supersonic_Sensor.Supersonic_Sensor(35)

시작할 때는 앞바퀴가 90도로 회전하도록 했습니다.
distance_detector = Supersonic_Sensor.Supersonic_Sensor(35) <- 이 코드는 앞서 말했듯이 직접 Supersonic_Sensor를 import해왔기 때문에 사용한 것입니다.


        self.count = 0
        
self.count에 0을 저장하였습니다.


        try:
            while True:
                track = self.car.line_detector.read_digital()
            
                if distance_detector.get_distance() > 23:
                    self.car.accelerator.go_forward(50)
                    time.sleep(0.01)
                    self.linetrace()
                    time.sleep(0.05)
                    
거리가 23cm를 초과할 때는 50의 속도로 전진하고 linetrace()를 통해 트랙을 따라가도록 했습니다.
50의 속도로 해야 트랙을 심하게 벗어나지 않으면서 오히려 속도를 더 빠르게 했을 때보다 트랙을 더 빨리 도는 효과가 나타나서 50으로 했습니다.

                
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
                            
장애물을 인식하여 거리가 0을 초과하고 23 이하일 경우에는 차의 앞바퀴를 35도로 회전하여 1초동안 45의 속도로 전진하도록 하였고,
그 다음에는 90도로 회전하여 앞으로 일직선으로 55의 속도로 진행하도록 했습니다.

그 다음 적외선 센서로 인식했을 때, 리스트 안에 1이라는 값이 들어가게 되면 검은 줄을 인식했다는 뜻이므로 멈추도록 했습니다.
멈추도록 한 이유는 바로 그 다음으로 넘어가게 하면 관성 때문에 가이드 라인을 넘어서 지나가는 경우도 있었기 때문입니다.

이 다음에는 오른쪽으로 이동하여 트랙을 다시 찾으러 가야하므로 앞바퀴를 145도 회전하도록 하여 60의 속도로 1.2초동안 전진하도록 했습니다.

1.2초동안 전진한 이후에는 아까와 똑같이 검은 줄을 인식할 때까지 앞으로 직진을 하도록 while문을 선언했습니다.


                else:
                    pass
                    
가끔 초음파 센서에서 -1의 값을 출력할 때가 있어서 그런 경우는 pass하도록 했습니다.


                if self.count == 2:
                    self.car.accelerator.stop()
                    break

앞서 설명드렸던 내용입니다. self.count가 2가 되면 차가 멈추도록 했습니다. 그리고 전체 큰 while문을 종료하도록 break문을 썼습니다.

        except:
            self.car.accelerator.stop()
            time.sleep(0.3)
            self.car_startup()
            
전체적으로 보면 try, except문을 사용했는데, 그 이유는 I/O Error때문입니다.
I/O Error가 발생하면 차가 원하는 대로 움직이지 않습니다.
그래서 I/O Error가 발생하면 차를 잠시 멈추고 car_startup() 함수를 다시 실행시켰습니다.

하지만 이는 트랙 중간에서 I/O Error가 발생하면 잘 작동하지만, 가이드라인을 따라가다가 I/O Error가 발생하면 잘 작동하지 않습니다.

가이드라인을 따라가다가 에러가 발생하면 car_startup()의 처음 부분인 트랙을 따라가는 부분부터 다시 실행되므로 
가이드라인을 향해 움직이도록 만든 코드까지 오지 않습니다.

그래서 이후에는 I/O Error를 raise하는 코드를 다른 모듈 쪽에서 찾아 그것 코드 한 줄을 없애서 I/O Error가 발생해도 주행에 아무런 문제 없도록 했습니다.

--------------------------------------------------------------------------------------------------------------------------------------
이번 과제를 하면서 I/O Error 때문에도 많은 고생을 하고, time.sleep을 활용하는 데에도 많은 시간을 투자하였고, 여러모로 힘들었습니다.
주행을 많이 하느라 배터리도 부족한 현상이 많았기에 배터리 충전하는 시간 때문에도 시간이 걸렸습니다. (밤을 새가면서 했던..)

그래도 이 과제를 통해 함수를 다양히 다룰 수 있게 되었고, 실력도 좀 늘었습니다.

또한, 최적화 작업이 꽤나 어렵다는 것을 크게 느끼게 된 것 같습니다.

여러모로 많은 것을 깨닫게 되었습니다.
