"""

This binary search implementation only returns a True if the element is found, otherwise False

Added a unittest as well

"""

import unittest
import logging

LOGLEVEL = logging.INFO

class TestSearch(unittest.TestCase):

    def test_search_found(self):

        array = [1, 3, 4, 16, 31, 34, 55, 56, 67, 78, 88, 902]
        logging.debug(array)

        self.assertEqual(binarySearch(tuple(array), 56), True)

    def test_search_notfound(self):

        array = [1, 3, 4, 16, 31, 34, 55, 56, 67, 78, 88, 902]
        logging.debug(array)

        self.assertEqual(binarySearch(tuple(array), 54), False)



def binarySearch(arr: tuple, i: int):

    half = len(arr) // 2

    if len(arr) < 2 and i != arr[half]:
        logging.debug(f"dead end: {i} is definitely not in {arr}")
        return False

    if i == arr[half]:
        logging.debug(f"found {i} in {arr}")
        return True
    elif i < arr[half]: # if the number to search is bigger than the `middle` element, search in the lower half
        logging.debug(f"searching in {arr[0:half]}")
        return binarySearch(arr[0:half], i)
    elif i >= arr[half]:
        logging.debug(f"searching in {arr[half:]}")
        return binarySearch(arr[half:], i)


if __name__ == '__main__':

    logging.basicConfig(level=LOGLEVEL)
    unittest.main()
