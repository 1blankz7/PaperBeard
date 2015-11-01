#!/usr/bin/env python
"""

"""
import argparse
from io import StringIO
import time
from paper_beard.engine import Just
import paper_beard.export
import os
import paper_beard
import random


__author__ = 'Malte Eckhoff'

description = """Parses PDFs from a folder and puts out a csv containing meta information (like ranking) for the
contained PDFs."""


class App(object):

    @staticmethod
    def run(arguments):
        output_file = open(arguments.outputCSVFile, "w")
        result = []
        for root, directories, filenames in os.walk(arguments.inputFolder):
            for filename in filenames:
                # Get the full path to the file
                path_to_file = os.path.join(root, filename)
                result.append(paper_beard.check(path_to_file))
                # Wait a moment to avoid getting tagged as a bot...
                time.sleep(0.5 + 3 * random.random())
        result = list(map(lambda x: x.value, filter(lambda x: type(x) is Just, result)))
        buffer = StringIO()
        buffer = paper_beard.export.csv_export(result, buffer)
        output_file.write(buffer.getvalue())

        output_file.close()
        print("Getting Google Scholar results for PDF completed...")


if __name__ == '__main__':
    # Fixme: as an alternative we could add __main__.py to paper_beard
    # Parse arguments
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('inputFolder', help='The folder from which the PDFs will be looked up on Google Scholar.')
    parser.add_argument('outputCSVFile',
                        help='The csv file where the extracted information about the PDF files will be written.')
    args = parser.parse_args()
    App.run(args)
