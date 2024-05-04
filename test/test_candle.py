from unittest import TestCase

from src.main import Candle

class CandleTestCase(TestCase):

    def test_debug(self):
        candle = Candle()
        candle.debug("debug message", "hello", kwarg1="world")