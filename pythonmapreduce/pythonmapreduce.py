"""Main module."""
import json
import os
from concurrent.futures import ThreadPoolExecutor
from os import path, listdir
from pathlib import Path
from typing import List

from .utils import median_management
from .utils.seive import punctuation_split


class MapReduce:
    def __init__(
        self, input_filename: list, output_filename: str, formats: List[str], threads
    ):
        self.input_filenames = input_filename
        self.output_filename = output_filename
        self.formats = formats
        self.threads = threads
        self.data = list()
        self.stdin_lines = list()

    def in_parse(self, stdin_lines: List[str]):
        """
        Split the any specified files from the input_filenames and add to the dataset. This only cleans the `\n`
        and empty character from the data.

        :param stdin_lines: standard input from the sys.stdin command.
        """
        if len(self.input_filenames) > 0:
            for path_ in self.input_filenames:
                if path.isfile(path_):
                    self.gen_dict(path_)
                else:
                    for file in [
                        path.join(path_, f)
                        for f in listdir(path_)
                        if path.isfile(path.join(path_, f))
                    ]:
                        self.gen_dict(file)
        if len(stdin_lines) > 0:
            self.data.append(
                {"stdin": [line.strip() for line in stdin_lines if line.strip() != ""]}
            )

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            if not os.path.isdir(Path("data", "parsed")):
                os.makedirs(Path("data", "parsed"))

            def dump(data):
                with open(
                    Path(
                        "data",
                        "parsed",
                        f"{data['title'].replace(' ', '-')}.json",
                    ),
                    "w",
                ) as dumped:
                    json.dump(data, dumped, indent=2)

            executor.map(dump, self.data)

    def gen_dict(self, file):
        with open(file, "r", encoding="ISO-8859-1") as in_file:
            title = os.path.basename(file).split(".")[0].replace("-", " ")
            min_heap = list()
            max_heap = list()
            contents = list()
            char_count = 0
            # TODO get average word-per-line
            # TODO get median word-per-line
            for line in in_file.readlines():
                if line.strip() != "":
                    char_count += len(line.strip())
                    max_heap, min_heap = median_management.push(
                        max_heap, min_heap, len(line.strip())
                    )
                    contents.append(line.strip())

            median = median_management.median(max_heap, min_heap)

            self.data.append(
                {
                    "title": title,
                    "meta": {
                        "lines": len(contents),
                        "characters": char_count,
                        "median characters per line": median,
                        "average characters per line": char_count / len(contents),
                    },
                    "contents": contents,
                }
            )

    def filter(self):
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            results = list(executor.map(punctuation_split, self.data))
