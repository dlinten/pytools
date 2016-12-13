import unittest
from async_runner import Execute


class AsyncRunnerTestCase(unittest.TestCase):
    def test_execute_async(self):
        listing = ''
        for line in Execute.execute_async(cmd='ls -la'):
            listing += line
        self.assertTrue(listing)

    def test_execute_with_info_async(self):
        listing = ''
        for line in Execute.execute_with_info_async(cmd='ls -la'):
             listing += line
        self.assertTrue(listing)


if __name__ == '__main__':
    unittest.main()
