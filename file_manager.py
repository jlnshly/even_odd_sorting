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
        if not os.path.exists(filepath):
            raise FileNotFoundError(f'File {filepath} not found')
        try:
            with open(filepath, 'r') as file:
                content = file.read().split()
                return [int(x) for x in content if x.lstrip('-').isdigit()]
        except Exception as e:
            logging.error(f'Error reading file to {filepath}: {e}')
            return []

    @staticmethod
    def write_to_file(filepath: str, data: list):
        """Writes data to file"""
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, 'w') as file:
                 output ='\n'.join(map(str, data))
        except Exception as e:
            logging.error(f'Error writing file to {filepath}: {e}')