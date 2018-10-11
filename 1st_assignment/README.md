     def car_startup(self):
         # Implement the assignment code here.
 
         direction_controller = front_wheels.Front_Wheels()
  	 direction_controller.center_alignment()
 	 time.sleep(1)
 	 driving_controller = rear_wheels.Rear_Wheels()
 	 driving_controller.ready()
 	 detector = Supersonic_Sensor.Supersonic_Sensor(35)
 

코드를 실행하면, 차의 앞 바퀴가 앞을 바라보도록 한 뒤, 뒷 바퀴가 대기 상태로 머무르도록 했습니다.

또한, 거리를 측정하기 위해 SR02에서 SR02_Supersonic을 Supersonic_Sensor로 import 했었는데, 핀 번호를 35번으로 정해줬습니다.

본격적으로 차를 움직이는 코드를 설명하겠습니다.

우선, 다음과 같이 변수를 선언하였습니다.

     done = False
     limit = 15
     speed = 30
     a = limit
     count = 0

done이라는 변수는 나중에 while문을 빠져나가도록 하기 위한 장치이고, limit는 차의 멈추는 제한 거리, speed는 차의 속도입니다.
a라는 변수에는 limit의 값을 저장해두었고, count는 루프가 돌 때 그 횟수를 측정하기 위해 0의 값을 저장해두었습니다.

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


done이 "False"이면 while문이 계속 실행되도록 하였습니다. 먼저 새로운 제한거리와 속도로 주행을 시작할 때마다 앞 바퀴의 방향을 조정하기 위해 front_wheels.Front_Wheels().center_alignment()를 사용했습니다.

다음으로 초음파 센서로부터 얻은 거리인 detector.get_distance()가 제한거리를 저장해 둔 a보다 크다면 계속 앞으로 주행을 이어가도록 driving_controller.go_forward(speed)가 실행되도록 했습니다.

detector.get_distance()가 a보다 작은 경우에는 일단 음수인 경우에는 초음파 센서가 음수의 값을 측정한 경우는 오류이기 때문에 continue를 통해 while루프가 다시 실행되도록 했습니다. 

음수인 경우를 제외하고 detector.get_distance()가 a보다 작은 경우에는 뒷 바퀴의 움직임을 2초동안 멈추게 했고, 앞으로 주행했을 때와 같은 속도로 4초동안 뒤로 주행을 하도록 했습니다.

이 과정이 끝나면 speed의 값에 +20을, limit의 값에 +5를, count에 +1을 하였습니다.

a = limit + 5*count 를 한 이유는, 관성 때문입니다. 차가 정확히 15cm, 20cm, 25cm에 멈추지 않고 제한거리가 증가할 때마다 속도도 증가해서 그 거리보다 더 많이 움직이는 경우가 많습니다. 루프가 돌 때마다 속도가 증가하는 것을 생각하여 실험적으로 관성을 조절하려고 하다보니 멈추기 시작하는 거리를 기존에  설정해야하는 제한 거리보다 좀 더 길게 해야 했습니다.

시행착오를 통해 limit + 5*count 정도를 하면 얼추 15, 20, 25cm에서 멈추는 것을 발견하게 되었기에 이와 같이 만들었습니다.

그리고 limit가 25를 초과하면, 차가 아예 멈추도록 하였고, done에 "True"를 저장하여 while루프가 끝나도록 만들었습니다.

이런 방식으로 이번 과제를 수행했습니다.
