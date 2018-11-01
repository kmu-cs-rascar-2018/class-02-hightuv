        while True:
        self.car.accelerator.go_forward(70)

#while문을 사용하여 구현을 했습니다. 뒷바퀴가 70의 속도로 앞으로 계속 굴러가도록 했습니다.

	current = self.car.line_detector.read_digital()

#current라는 변수에 적외선 센서를 통해 얻은 리스트를 저장하였습니다. 반복문이 실행되면서 차가 앞으로 가면서 current에 저장되는 값은 계속 바뀌게 될 것입니다.

	if current == [0,0,0,0,0] or current == [1,1,1,1,1]:
	self.car.accelerator.stop()
	time.sleep(1)
	self.car.accelerator.power_down()
	break

#만약 current에 [0,0,0,0,0] 또는 [1,1,1,1,1]과 같다면 차가 멈추고 파워가 다운되도록 하였고 반복문을 빠져나오도록 break를 썼습니다.

	elif current[0] == 1:
	self.car.steering.turn(60)
	time.sleep(0.01)

#맨 왼쪽에서 검은 줄은 인식하는 경우에는 current의 0번째 원소가 1의 값을 가지게 될 것입니다.

#이 경우에는 왼쪽으로 많이 꺾어야하므로 self.car.steering.turn()의 인자를 60으로 설정했습니다.

#그리고 이 행위가 0.01초동안 지속되도록 했습니다.

	elif current[1] == 1:
	self.car.steering.turn(75)
	time.sleep(0.01)

#왼쪽에서 두 번째 센서가 검은 줄을 인식하는 경우에는 current의 2번째 원소가 1의 값을 가지게 될 것입니다.

#이 경우에는 current의 1번째 원소가 1의 값을 가지게 되는데 0번째 원소가 1일 때보다는 덜 꺾여야합니다.

#그래서 self.car.steering.turn()의 인자를 75로 설정했고 이 또한 0.01초동안 지속되도록 했습니다.

	elif current[3] == 1:
	self.car.steering.turn(105)
	time.sleep(0.01)
	elif current[4] == 1:
	self.car.steering.turn(120)
	time.sleep(0.01)

#current의 3, 4번째 원소가 1인 경우에는 오른쪽의 센서들이 검은 줄을 인식한 것입니다.

#current의 0,1번째 원소가 1인 경우와 반대 경우이므로 왼쪽으로 앞바퀴를 왼쪽으로 움직이던 것과 대칭이 되도록 설정했습니다.

#(self.car.steering.turn()의 인자로 105와 120을 넣었습니다.)

	elif current[2] == 1:
	self.car.steering.center_alignment()
	time.sleep(0.01)

#마지막으로 current의 2번째 원소가 1인 경우에는 검은 줄이 가운데에 존재한다는 뜻이므로 앞바퀴를 앞으로 정렬하여 직진하도록 설정했습니다.

#만약 current가 [1,1,1,1,1]이거나 [0,0,0,0,0]일 때의 조건을 첫 번째 조건문으로 쓰지 않고 맨 아래 조건문으로 쓰면 위의 조건문들을 다 확인하고 마지막에 이 조건문을 확인하기 때문에 트랙 끝까지 가도 멈추지 않는 현상이 있었습니다.

#처음에는 이 때문에 혼란스러웠지만 조건문의 순서 때문에 이런 일이 일어난다는 것을 깨닫고 현재의 코드와 같이 변경했습니다.
