import os
import logging

class FileManager:
    """
    Stores simple I/O operations on files
    Uses @staticmethod to not store state here
    """

    @staticmethod
    def read_integers(filepath: str):
        """Reads file and only return list of integers"""
        try:
            if not os.path.exists(filepath):
                raise FileNotFoundError(f'File {filepath} not found')
            with open(filepath, 'r') as file:
                content = file.read()
                words = content.split()
                numbers = [int(x) for x in words if x.lstrip('-').isdigit()]
                return numbers
        except Exception as e:
            logging.error(f'Error reading file to {filepath}: {e}')
            return []

    @staticmethod
    def write_to_file(filepath: str, data: list):
        """Writes data to file"""
        try:
            directory = os.path.dirname(filepath)
            if directory:
                os.makedirs(directory, exist_ok=True)
            with open(filepath, 'w') as file:
                output ='\n'.join(map(str, data))
                file.write(output)
            print(f'Succesfully writing into {filepath}')
        except Exception as e:
            logging.error(f'Error writing file to {filepath}: {e}')