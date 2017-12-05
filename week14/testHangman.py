import unittest
from hangman import Hangman

class TestHangman(unittest.TestCase):

    def setUp(self):
        self.h1 = Hangman()

    def tearDown(self):
        pass

    def testCurrentShape(self):
        self.assertEqual(self.h1.currentShape(), 
'''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''')
        self.h1.decreaseLife()
        self.assertEqual(self.h1.currentShape(),
'''\
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''')

if __name__ == '__main__':
    unittest.main()
