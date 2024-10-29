#!/usr/bin/env python3
"""a module to solve task 1"""
from typing import Tuple
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        if isinstance(page, int) and isinstance(page_size, int):
            assert page >= 0 and page_size >= 0, (
                "AssertionError raised with negative values"
            )
            assert page != 0 and page_size != 0, "AssertionError raised with 0"
        else:
            raise AssertionError(
                "AssertionError raised when page and/or"
                " page_size are not ints"
            )
        t = index_range(page, page_size)
        data = Server.dataset(self)
        if len(data) <= t[1]:
            return []
        return data[t[0]:t[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to
    return in a list for those particular pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)
