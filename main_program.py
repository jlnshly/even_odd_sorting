import os
from integer_handling import IntegerHandling
from functionalities import ActivityTracker
from file_manager import FileManager

print(f'Finding here: {os.getcwd()}')

class MainProgram(ActivityTracker):
    def __init__(self):
        super().__init__()
        self.files = {
            'source' : 'numbers.txt',
            'even': 'even.txt',
            'odd': 'odd.txt'
        }

    def execute(self):
        self.log_activity('Starting...')
        try:
            data = FileManager.read_integers(self.files['source'])
            self.log_activity('Reading file {}'.format(self.files['source']))
            engine = IntegerHandling(data)
            evens = engine.filter_using_parity('even')
            odds = engine.filter_using_parity('odd')
            FileManager.write_to_file(self.files['even'], evens)
            FileManager.write_to_file(self.files['odd'], odds)
            self.log_activity(f'Writing File (Evens: ({len(evens)}), Odds: ({len(odds)}))')
            self.log_activity(f'Total runtime: {self.get_runtime()}')

        except Exception as e:
            self.log_activity(f'Critical Error: {e}')

if __name__ == '__main__':
    app = MainProgram()
    app.execute()

