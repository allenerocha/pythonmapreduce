"""Main module."""
from typing import List


class MapReduce:
    def __init__(self, input_filename: str, output_filename: str, formats: List[str]):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.formats = formats
