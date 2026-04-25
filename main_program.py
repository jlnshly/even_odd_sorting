from integer_handling import IntegerHandling
from functionalities import ActivityTracker
from file_manager import FileManager

class MainProgram(ActivityTracker):
    def __init__(self):
        super().__init__()
        self.files = {
            "source": "numbers.txt",
            "even": "even.txt",
            "odd": "odd.txt"
        }

    def execute(self):
        