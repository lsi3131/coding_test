import time

class ElapsedTimer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            raise ValueError("Timer not started. Call start() before stop.")
        elapsed_time = (time.time() - self.start_time) * 1000
        self.start_time = None  # 다음 측정을 위해 초기화
        return elapsed_time