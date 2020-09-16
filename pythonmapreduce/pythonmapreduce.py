"""Main module."""
from typing import List, Dict


class MapReduce:
    def __init__(self, input_filename: str, output_filename: str, formats: List[str]):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.formats = formats

    def map(self, data: Dict[str, List[str]]):
        if self.input_filename is not None:
            data[self.input_filename] = [
                line.strip()
                for line in open(self.input_filename, "r", encoding="utf8").readlines()
                if line.strip() != ""
            ]
        print(data.keys())
