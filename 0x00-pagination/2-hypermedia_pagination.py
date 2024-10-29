#!/usr/bin/env python3
"""a module to solve task 1"""
from typing import Tuple
import csv
import math
from typing import List
from typing import Dict
from typing import Optional
from typing import Any
from typing import Union


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[
        Optional[int], List[List[Any]]]
    ]:
        """
        returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        mydict: Dict[str, Union[
            Optional[int], List[List[Any]]]
            ] = {'page_size': page_size, 'page': page}
        mylist: List[Any] = Server.get_page(self, page, page_size)
        t: Tuple[int, int] = index_range(page, page_size)
        dataset: List[Any] = Server.dataset(self)
        mydict['data'] = mylist
        if mylist == []:
            total = math.ceil(len(dataset) / float(page_size))
            mydict['page_size'] = 0
        else:
            total = math.ceil(len(dataset) / float(page_size))
        if page >= total:
            n = None
        else:
            n = page + 1
        mydict['next_page'] = n
        if page <= 1:
            p = None
        else:
            p = page - 1
        mydict['prev_page'] = p
        mydict['total_pages'] = total
        return mydict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to
    return in a list for those particular pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)
