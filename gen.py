import numpy as np
import random

# 중력가속도 설정
# 기본값: g = 9.81
# 240413 추가- 중력 랜덤 파라미터
g = random.randrange(9,16)

def simulate_pendulums(num_pendulums, initial_angles, lengths, damping, timesteps, dt):

  positions = np.zeros((timesteps, num_pendulums))
  velocities = np.zeros((timesteps, num_pendulums))
  positions[0] = initial_angles

  for t in range(1, timesteps):
    accelerations = -g / lengths * np.sin(positions[t - 1])
    velocities[t] = velocities[t - 1] + accelerations * dt - damping * velocities[t - 1] * dt
    positions[t] = positions[t - 1] + velocities[t] * dt

  return positions

# 시뮬레이션 매개 변수 설정

# 시뮬레이션 파라미터 값 설정방법:
'''
num_pendulums = 5  # 진자의 개수
initial_angles = [원하는 초기각도]  # 초기 각도
lengths = [원하는 다중진자의 길이]  # 길이
damping = [원하는 감쇠 계수]  # 감쇠 계수
timesteps = [원하는 시간단계] # 시간 단계
dt = [원하는 시간 간격]  # 시간 간격
'''

# 240413 추가- 진자 개수와 시간단계 랜덤한 파라미터로 설정
num_pendulums = random.randrange(5,100)
initial_angles = np.random.uniform(-np.pi, np.pi, num_pendulums)
lengths = np.random.uniform(0.5, 2.0, num_pendulums)
damping = 0.1
timesteps = random.randrange(1000,7000)
dt = 0.01

# 진자 시뮬레이션 수행
positions = simulate_pendulums(num_pendulums, initial_angles, lengths, damping, timesteps, dt)

# 마지막 진자의 마지막 위치를 난수로 사용
random_number = positions[-1, -1]

print(random_number)
