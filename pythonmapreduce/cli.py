"""Console script for pythonmapreduce."""
import argparse


def parse():
    """Console script for pythonmapreduce."""
    parser = argparse.ArgumentParser(
        prog="pythonmapreduce",
        description="%(prog)s -- Takes standard input or a specified file and uses a map reduce algorithm to generate "
        "the word count and saves it to a given format.",
        epilog="More for information for %(prog)s can be found at https://github.com/allenerocha/pythonmapreduce",
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        nargs="*",
        help="Used to specify input file(s) or directories to read (optional)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="output",
        help="Output filename (optional) [Default: output.json]",
    )
    parser.add_argument(
        "-f",
        "--formats",
        type=str,
        default="json",
        nargs="*",
        help="Format(s) for the out file (optional, will generate a file for each given format) [Default: JSON "
        "format. View https://github.com/allenerocha/pythonmapreduce for more available formats.]",
    )
    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=1,
        help="Number of  threads to run this application with (optional).",
    )
    args = parser.parse_args()
    if args.input is None:
        return list(), str(args.output), list(args.formats), int(args.threads)
    return list(args.input), str(args.output), list(args.formats), int(args.threads)
