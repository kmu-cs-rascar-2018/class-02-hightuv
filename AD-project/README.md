창업연계공학 AD-project 보고서
===
# 조원 
김진석 20181600  
박민서 20181610

## 프로젝트 제안서
[제안서](제안서.md)
## 발표 자료
AD_Project_Presentation.pptx

## 환경 구성 및 스피커 제작
음원을 재생을 하기 위해 파이썬 라이브러리중 wav, mp3 등의 음성 파일을 재생할 수 있는
라이브러리를 찾기위해 검색을 하였다. 여러 옵션이 나왔는데 pygame과 python-vlc가 
그것 중 하나였다. pygame은 여러 옵션을 주어야 재생이 가능 했던것과 비교하여 python-vlc는 
파일을 불러오고 재생만 시키면 되었기에 python-vlc를 사용했다.  
>python-vlc installation
```bash
sudo apt install vlc libvlc5 libvlc-bin libvlccore9 libvlccore-dev libvlc-dev
pip3 install python-vlc
```

스피커는 2개의 버전을 만들고 마지막 버전을 사용했다. 첫번째 버전은 간단한 회로부품을 이용하여 제작한 것으로 그닥 좋은 음질이 나오지 않아 바로 다음 버전의 스피커를 제자했다.
마지막 버전의 스피커는 원래 있던 스피커를 회로와 전선, 스피커만 취한 것이다. ac전원을 받는 물건이지만 dc전원을 넣어도 작동하여 그대로 구동체에 연결했다.

프로토타입
![프로토타입](./images/prototype_speaker.jpg)

최종 버전
![최종버전](./images/lastest_version_speaker.jpg)

## 구현
RGB센서 사용이 빈번함으로 측정하는 위치도 많이 고려했다. 1cm 부터 바닥에 거의 닿게하는 수준까지 바닥과의 거리를 달리하여 측정을 했다.
위치에 따라 값이 달라지는 지 확인을 하고 값이 제일 큰 바닥면에 제일가깝게하는 것으로 했다.
RGB의 값을 받아 들여 음원을 재생해야 하므로 RGB센서를 붙이고 대략적인 색의 범위를 정했다. 3개의 값을 받아들여 3개의 범위로 복합적인 범위를 설정했다.
```python
if color_list[0] > 1000 and color_list[1] > 1000 and 400 < color_list[2] < 750:
    print("Yellow")
```

음악 재생은 라이브러리를 초기화하고 플레이어를 만들고 파일을 불러온뒤 재생하는 것이다.
>준비 작업
```python
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
```
>재생
```python
self.player.stop()
self.player.set_media(self.sounds[4])
self.player.play()
```
주행 코드와 정지후 장애물이 나오면 다시 주행하는 것은 이전 과제의 코드와 다른것이 없다.
장애물을 만나면 멈추었다가 사라지면 주행하는 것밖에 다를 것이 없다.
```python
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
```