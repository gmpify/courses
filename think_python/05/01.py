import time

now = time.time()

second = int(now % 60)

now = now // 60

minute = int(now % 60)

now = now // 60

hour = int(now % 24)

days = int(now // 60)

print(f"days since epoch: {days}")
print(f"time now: {hour}:{minute}:{second}")
