#!/usr/bin/env python3

# References
# http://docs.python.org/3.3/library/unittest.html

import unittest
import logpuzzle

class TestCopySpecial(unittest.TestCase):

    def setUp(self):
        pass


    def test_read_urls(self):

        results = logpuzzle.read_urls('a_filename')

        expected_result = 1
        self.assertEqual(expected_result, len(results),
                         'expected {} but got {}'.format(
                             expected_result,
                             len(results)))

        test_index = 0
        expected_result_index = 1

        test_datas = [
            [0, '10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"']
        ]

        for test_data in test_datas:
            result = results[test_data[test_index]]
            expected_result = test_data[expected_result_index]
            self.assertEqual(expected_result, result,
                             'read_urls()[{}] expected {} but got {}'.format(test_index,
                                                                                 expected_result,
                                                                                 result))


    def test_download_images(self):
        pass

if __name__ == "__main__": unittest.main()
