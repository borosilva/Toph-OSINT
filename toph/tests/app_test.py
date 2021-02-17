import unittest
from toph.app import run

class TestAppClass(unittest.TestCase):

    def test_run(self):
        self.assertEqual(run(), 'Hola Mundo.')

