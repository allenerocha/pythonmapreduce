"""Main module."""
import json
import os
from concurrent.futures import ThreadPoolExecutor
from os import path, listdir
from pathlib import Path
from typing import List

from .utils import median_management
from .utils.analyze import Scatter
from .utils.seive import punctuation_split, extra_spaces


class MapReduce:
    def __init__(
        self,
        input_filename: List[str],
        formats: List[str],
        threads,
        output_filename="output",
    ):
        self.input_filenames = input_filename
        self.output_filename = output_filename
        self.formats = formats
        self.threads = threads
        self.data = list()
        self.stdin_lines = list()
        self.median_char_scatter = Scatter(None)
        self.median_word_scatter = Scatter(None)
        self.average_char_scatter = Scatter(None)
        self.average_word_scatter = Scatter(None)

    def in_parse(self, stdin_lines: List[str]):
        """
        Split the any specified files from the input_filenames and add to the dataset. This only cleans the `\n`
        and empty character from the data.

        :param stdin_lines: standard input from the sys.stdin command.
        """
        if len(self.input_filenames) == 0 and len(stdin_lines) == 0:
            print("No data to parse.")

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
        y_axis = "Total lines"
        self.median_char_scatter.plot(
            "Median characters per line vs Total lines",
            "Median characters per line",
            y_axis,
            "median-chars",
        )
        self.median_word_scatter.plot(
            "Median words per line vs Total lines",
            "Median words per line",
            y_axis,
            "median-words",
        )
        self.average_char_scatter.plot(
            "Average characters per line vs Total lines",
            "Average characters per line",
            y_axis,
            "average-chars",
        )
        self.average_word_scatter.plot(
            "Average words per line vs Total lines",
            "Average words per line",
            y_axis,
            "average-words",
        )

    def gen_dict(self, file):
        with open(file, "r", encoding="ISO-8859-1") as in_file:
            title = os.path.basename(file).split(".")[0].replace("-", " ")
            char_min_heap = list()
            char_max_heap = list()
            word_min_heap = list()
            word_max_heap = list()
            word_sum = 0
            contents = list()
            char_count = 0
            # TODO get average word-per-line
            # TODO get median word-per-line
            for line in in_file.readlines():
                if line.strip() != "":
                    char_count += len(line.strip())
                    char_max_heap, char_min_heap = median_management.push(
                        char_max_heap, char_min_heap, len(line.strip())
                    )
                    word_max_heap, word_min_heap = median_management.push(
                        word_max_heap,
                        word_min_heap,
                        len(extra_spaces(line.strip()).split(" ")),
                    )
                    word_sum += len(extra_spaces(line.strip()).split(" "))
                    contents.append(line.strip())

            char_median = median_management.median(char_max_heap, char_min_heap)
            word_median = median_management.median(word_max_heap, word_min_heap)

            self.median_char_scatter.append(title, [char_median, len(contents)])
            self.median_word_scatter.append(title, [word_median, len(contents)])
            self.average_char_scatter.append(
                title, [char_count / len(contents), len(contents)]
            )
            self.average_word_scatter.append(
                title, [word_sum / len(contents), len(contents)]
            )

            self.data.append(
                {
                    "title": title,
                    "stats": {
                        "lines": len(contents),
                        "characters": char_count,
                        "median c/l": char_median,
                        "average c/l": char_count / len(contents),
                        "median w/l": word_median,
                        "average w/l": word_sum / len(contents),
                        "delta": 100.0
                        * abs(char_median - (char_count / len(contents)))
                        / (char_median + (char_count / len(contents)) / 2),
                    },
                    "contents": contents,
                }
            )

    def filter(self):
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            results = list(executor.map(punctuation_split, self.data))
