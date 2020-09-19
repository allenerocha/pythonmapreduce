#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The main entry point.
Invoke as `pythonmapreduce' or python -m pythonmapreduce.
"""


def main():
    from .cli import parse
    from .pythonmapreduce import MapReduce

    input_filename, output_filename, formats, threads = parse()
    mapreduce = MapReduce(
        input_filename=input_filename,
        output_filename=output_filename,
        formats=formats,
        threads=threads,
    )
    mapreduce.in_parse([])


if __name__ == "__main__":
    main()
