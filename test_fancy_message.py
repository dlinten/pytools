import unittest
from fancy_message import Message


class FancyMessageTestCase(unittest.TestCase):

    @staticmethod
    def test_header():
        Message.header('This is a Message.header() test')

    @staticmethod
    def test_info():
        Message.info('This is a Message.info() test')

    @staticmethod
    def test_warn():
        Message.warn('This is a Message.warn() test')

    @staticmethod
    def test_error():
        Message.error('This is a Message.error() test')

    @staticmethod
    def test_output():
        Message.output('This is a Message.output() test')

if __name__ == '__main__':
    unittest.main()
