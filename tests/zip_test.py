import unittest

import ../zip

class TestZip(unittest.TestCase):

    def test_zip(self):
        test_dir = 'C:/test'
        self.assertEqual(zip.zip_dir(test_dir), True, f"Zipped directory should be {test_dir}")


if __name__ == '__main__':
    unittest.main()