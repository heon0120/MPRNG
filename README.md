# MPRNG
Multiple Pendulum Random Number Generation

## 프로그램 구성:


fig.py: 다중 진자의 그래프를 Matplotlib을 사용하여 보여줍니다.

gen.py: fig.py 코드를 응용하여 난수를 생성합니다.

## 선행 조건

아래 사항들이 설치가 되어있어야합니다.

    python



## 사용 방법:

1. 이 저장소를 GitHub에 복제합니다.

2. requirements.txt에 있는 라이브러리를 설치합니다:


       pip install -r requirements.txt


3. fig.py를 실행하여 다중 진자 시뮬레이션 그래프와 난수 범위 히스토그램을 확인할수 있습니다.:

       python fig.py
4. gen.py를 실행하여 마지막 진자의 마지막 위치를 난수로 출력합니다.:

       python gen.py


## 시뮬레이션 매개변수 설정
> [!Warning]
> gen.py의 매개변수는 랜덤한 값을 가집니다!
> 매개변수들은 임의의 변수로 수정이 가능합니다.

### 시뮬레이션 매개변수 설정(fig.py)


``` python
# Define gravitational acceleration constant
g = 9.81  # m/s^2

num_pendulums = 5  # 진자의 개수
initial_angles = np.random.uniform(-np.pi, np.pi, num_pendulums)  # 초기 각도
lengths = np.random.uniform(0.5, 2.0, num_pendulums)  # 길이
damping = 0.1  # 감쇠 계수
timesteps = 1000  # 시간 단계
dt = 0.01  # 시간 간격
```



> g: 중력 가속도 (m/s^2)

> num_pendulums: 시뮬레이션에 사용할 진자의 개수

> initial_angles: 각 진자의 초기 각도 (균일 분포, -π ~ π)

> lengths: 각 진자의 길이 (균일 분포, 0.5 ~ 2.0)

> damping: 진동 감쇠를 조절하는 감쇠 계수 (값이 클수록 진동 감쇠 속도가 빨라짐)

> timesteps: 시뮬레이션을 수행할 시간 단계의 개수

> dt: 각 시간 단계의 길이 (초)




### 시물레이션 매개변수 설정(gen.py)
> [!Warning]
> gen.py의 매개변수는 fig.py와 크게 다를것이 없습니다.


``` python
# Define gravitational acceleration constant
g = 9.81  # m/s^2

num_pendulums = 5  # 진자의 개수
initial_angles = np.random.uniform(-np.pi, np.pi, num_pendulums)  # 초기 각도
lengths = np.random.uniform(0.5, 2.0, num_pendulums)  # 길이
damping = 0.1  # 감쇠 계수
timesteps = 1000  # 시간 단계
dt = 0.01  # 시간 간격
```



> g: 중력 가속도 (m/s^2)

> num_pendulums: 시뮬레이션에 사용할 진자의 개수

> initial_angles: 각 진자의 초기 각도 (균일 분포, -π ~ π)

> lengths: 각 진자의 길이 (균일 분포, 0.5 ~ 2.0)

> damping: 진동 감쇠를 조절하는 감쇠 계수 (값이 클수록 진동 감쇠 속도가 빨라짐)

> timesteps: 시뮬레이션을 수행할 시간 단계의 개수

> dt: 각 시간 단계의 길이 (초)

## 라이브러리:

numpy

random

matplotlib


## 기여
소스 수정사항이 있다면 Pull requests 로 열어주세요.(시간없는 중딩이라 자주 확인 못할수 있습니다.)

## 라이센스
이 프로젝트는 MIT라이선스가 적용됩니다.
