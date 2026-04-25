from datetime import datetime

class ActivityTracker:

    def __init__(self):
        self.start_time = datetime.now()
        self.activity_count = 0

    def log_activity(self, message: str):
        self.activity_count += 1
        time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{time_stamp}] {message}')

    def get_runtime(self):
        delta = datetime.now() - self.start_time
        return f"{delta.total_seconds()} seconds"
