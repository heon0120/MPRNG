import numpy as np
import random

# Define gravitational acceleration constant
g = 9.81  # m/s^2

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
num_pendulums = 5  # 진자의 개수
initial_angles = np.random.uniform(-np.pi, np.pi, num_pendulums)  # 초기 각도
lengths = np.random.uniform(0.5, 2.0, num_pendulums)  # 길이
damping = 0.1  # 감쇠 계수
timesteps = 1000  # 시간 단계
dt = 0.01  # 시간 간격

# 진자 시뮬레이션 수행
positions = simulate_pendulums(num_pendulums, initial_angles, lengths, damping, timesteps, dt)

# 마지막 진자의 마지막 위치를 난수로 사용
random_number = positions[-1, -1]

print("난수:", random_number)
