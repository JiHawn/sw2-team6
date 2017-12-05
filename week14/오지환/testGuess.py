import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('a')
    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('z')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')
        self.g2.guess('a')
        self.assertEqual(self.g2.displayCurrent(), 'a ')

    def testDisplayGuessed(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('z')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u z ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n t u z ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f n t u z ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f l n t u z ')
        self.g2.guess('a')
        self.assertEqual(self.g2.displayGuessed(), ' a e n ')
    
    def testFinished(self):
        self.g2.guess('b')
        self.assertFalse(self.g2.finished())
        self.g2.guess('a')
        self.assertTrue(self.g2.finished())

    def testGuess(self):
        self.assertFalse(self.g1.guess('z'))

if __name__ == '__main__':
    unittest.main()
