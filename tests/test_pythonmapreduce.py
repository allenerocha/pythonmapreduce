#!/usr/bin/env python

"""Tests for `pythonmapreduce` package."""

import unittest
from pathlib import Path

from pythonmapreduce import pythonmapreduce


class TestPythonmapreduce(unittest.TestCase):
    """Tests for `pythonmapreduce` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_map_file(self):
        """Test one single file (../data/Adventures-of-Huckleberry-Finn.txt)."""
        mapreduce = pythonmapreduce.MapReduce(
            [
                Path(__file__).parent.parent
                / "data"
                / "Adventures-of-Huckleberry-Finn.txt"
            ],
            "",
            None,
        )
        mapreduce.in_parse(list())
        self.assertEqual(69.0, mapreduce.data)

    def test_map_dir(self):
        """Test reading all 18 files in ../data/*."""
        mapreduce = pythonmapreduce.MapReduce(
            [Path(__file__).parent.parent / "data"], "", None
        )
        mapreduce.map(list())
        self.assertEqual(18, len(mapreduce.data))

    def test_stdin(self):
        # TODO test reading form stdin and mapping it.
        pass


if __name__ == "__main__":
    unittest.main()
