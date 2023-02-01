"""TestFiler
        Tests the capabilities of filer
    """
import unittest
import logging

from .. import filer


class TestFiler(unittest.TestCase):  # pylint: disable=missing-class-docstring
    logger = logging.getLogger(__name__)

    def setUp(self):
        self.logger.setLevel(20)

    def test_read_file(self):
        """test_read_file
            Tests the line read capability
        """

        fil = filer.Filer(
            '/Users/ss670121/sourcebox/github.com/python-projects/sample2/filer/tests/test_file.txt',
            20)

        # Test case where file exists and has the required line
        result = fil.read_line(2)
        self.assertEqual(result, '# I am line 2\n')
        self.assertRegex(str(fil), r"File.*")

        # Test case where file exists but has less lines than the requested line
        with self.assertRaises(filer.FilerException):
            fil.read_line(10)
        # with self.assertRaises(IndexError):
        #     fil.read_file('test_file.txt', 10)

    def test_read_file_none(self):
        """test_read_file_none
            Reading a file that doesn't exists
        """
        fil = filer.Filer('non_existent_file.txt', logging.DEBUG)

        # Test case where file does not exist
        # with self.assertRaises(FileNotFoundError):
        #     fil.read_file('non_existent_file.txt', 2)
        with self.assertRaises(filer.FilerException):
            fil.read_line(2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
