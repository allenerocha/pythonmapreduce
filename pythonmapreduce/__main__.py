#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The main entry point.
Invoke as `pythonmapreduce' or python -m pythonmapreduce.
"""


def main():
    from .cli import parse
    from .pythonmapreduce import MapReduce

    input_filename, output_filename, formats = parse()
    MapReduce(input_filename, output_filename, formats)


if __name__ == "__main__":
    main()
