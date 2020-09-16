"""Main module."""
from typing import List, Dict


class MapReduce:
    def __init__(self, input_filename: list, output_filename: str, formats: List[str]):
        self.input_filenames = input_filename
        self.output_filename = output_filename
        self.formats = formats
        self.data = dict()

    def map(self, stdin_lines: List[str]):
        """Split the any specified files from the input_filenames and add to the dataset."""
        if len(self.input_filenames) > 0:
            for file in self.input_filenames:
                self.data[file] = [
                    line.strip()
                    for line in open(file, "r", encoding="utf8").readlines()
                    if line.strip() != ""
                ]

        if len(stdin_lines) > 0:
            self.data["stdin"] = [
                line.strip() for line in stdin_lines if line.strip() != ""
            ]
