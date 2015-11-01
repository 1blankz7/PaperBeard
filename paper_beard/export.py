"""
Export module for PaperBeard.

Every export function should have the following signature:

```
xyz_export(data: list[Result], buffer: StringIO) -> StringIO
```
"""
import csv
from collections import OrderedDict
from io import StringIO


exportable_fields = ["title", "author", "year", "citations", "link", "excerpt"]


def csv_export(data, buffer) -> StringIO:
    """Formats the data into a csv stream and returns the value.

    Uses the exportable_fields list for querying the results and generating the header.

    :type buffer: StringIO
    :type data: list[Result]
    :param data: a list of result objects fetch from a search engine
    :param buffer: the stream in which the formatted data should be written
    :return a stream of data formatted as valid csv
    """
    writer = csv.DictWriter(
        buffer,
        delimiter=';',
        quotechar='|',
        quoting=csv.QUOTE_MINIMAL,
        fieldnames=OrderedDict(map(lambda x: tuple([x, None]), exportable_fields)),
        extrasaction='ignore'
    )
    writer.writeheader()
    writer.writerows(data)
    return buffer
