import numpy as np
import random
import matplotlib.pyplot as plt

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

def generate_random_numbers(positions, num_pendulums):

  random_numbers = positions[-1]
  random_number_ranges = []

  for i in range(num_pendulums):
    min_value = min(random_numbers[i], -np.pi)
    max_value = max(random_numbers[i], np.pi)
    random_number_ranges.append((min_value, max_value))

  return random_numbers, random_number_ranges

# 시뮬레이션 매개 변수 설정
num_pendulums = 5  # 진자의 개수
initial_angles = np.random.uniform(-np.pi, np.pi, num_pendulums)  # 초기 각도
lengths = np.random.uniform(0.5, 2.0, num_pendulums)  # 길이
damping = 0.1  # 감쇠 계수
timesteps = 1000  # 시간 단계
dt = 0.01  # 시간 간격

# 진자 시뮬레이션 수행
positions = simulate_pendulums(num_pendulums, initial_angles, lengths, damping, timesteps, dt)

# 난수 생성 및 범위 계산
random_numbers, random_number_ranges = generate_random_numbers(positions, num_pendulums)

# 그래프 생성
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 진자 시뮬레이션 그래프
x_axis = np.arange(timesteps) * dt
y_axis = positions

for i in range(num_pendulums):
  ax1.plot(x_axis, y_axis[:, i], label=f"Pendulum {i + 1}")

ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Angle (radians)")
ax1.set_title(f"Multi-Pendulum Simulation (N={num_pendulums})")
ax1.legend()
ax1.grid(True)

# 난수 범위 히스토그램
for i, (random_number, range_) in enumerate(zip(random_numbers, random_number_ranges)):
  ax2.hist(random_number, bins=20, label=f"Pendulum {i + 1} Range: [{range_[0]}, {range_[1]}]")

ax2.set_xlabel("Random Number")
ax2.set_ylabel("Frequency")
ax2.set_title("Histogram of Random Numbers")
ax2.grid(True)
ax2.legend()

# 조정 및 출력
plt.tight_layout()
plt.show()
