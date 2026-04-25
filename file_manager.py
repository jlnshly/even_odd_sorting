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
