from datetime import datetime

class ActivityTracker:

    def __init__(self):
        self.start_time = datetime.now()
        self.activity_count = 0

    def logactivity(self):
        self.activity_count += 1