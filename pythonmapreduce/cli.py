"""Console script for pythonmapreduce."""
import argparse


def parse():
    """Console script for pythonmapreduce."""
    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into " "pythonmapreduce.cli.main")
    return 0
