"""
Main module of PaperBeard.
"""

import os
from paper_beard import pdf_tools
from paper_beard import pdf_title
import paper_beard.engine


def check(path_to_file):
    # Check if this is actually a file
    if not os.path.isfile(path_to_file):
        return

    # Check if this is a PDF file
    extension = os.path.splitext(path_to_file)[1]
    if extension.lower() != '.pdf':
        return

    # Get the title of the paper from the metadata
    try:
        title = pdf_tools.get_title(path_to_file)
    except Exception as e:
        print("There was an error while getting the title of the PDF : %s: %s The file will be skipped."
              % (path_to_file, str(e)))
        return

    if title is None or pdf_title.empty_str(title):
        print(
            "The metadata of the PDF-file %s doesn't contain information about the title."
            "We will try the content of the PDF instead." % path_to_file)
        title = pdf_title.title(path_to_file)

    # Get the name of the author from the metadata
    author = pdf_tools.get_author(path_to_file)

    result = paper_beard.engine.google_scholar(title, author=author)
    print("Getting Google Scholar results for PDF completed...")
    return result