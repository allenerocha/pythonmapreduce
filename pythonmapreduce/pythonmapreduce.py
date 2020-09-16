"""Main module."""
from os import path, listdir
from typing import List


class MapReduce:
    def __init__(self, input_filename: list, output_filename: str, formats: List[str]):
        self.input_filenames = input_filename
        self.output_filename = output_filename
        self.formats = formats
        self.data = dict()

    def map(self, stdin_lines: List[str]):
        """
        Split the any specified files from the input_filenames and add to the dataset. This only cleans the `\n`
        and empty character from the data.

        :param stdin_lines: standard input from the sys.stdin command.
        """
        if len(self.input_filenames) > 0:
            for path_ in self.input_filenames:
                if path.isfile(path_):
                    self.data[path_] = [
                        line.strip()
                        for line in open(path_, "r", encoding="ISO-8859-1").readlines()
                        if line.strip() != ""
                    ]
                else:
                    for file in [
                        path.join(path_, f)
                        for f in listdir(path_)
                        if path.isfile(path.join(path_, f))
                    ]:
                        self.data[file] = [
                            line.strip()
                            for line in open(
                                file, "r", encoding="ISO-8859-1"
                            ).readlines()
                            if line.strip() != ""
                        ]

        if len(stdin_lines) > 0:
            self.data["stdin"] = [
                line.strip() for line in stdin_lines if line.strip() != ""
            ]
