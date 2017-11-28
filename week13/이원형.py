class Guess:

    def __init__(self, word):

        self.secretWord = word
        self.guessedChars = set()
        self.numTries = 0
        self.currentStatus = '_' * len(word)


    def display(self):
        print('Current : ' + self.currentStatus)
        print('Tries : ' + str(self.numTries))

    def guess(self, character):
        self.guessedChars = self.guessedChars.union({character})
        if character not in self.secretWord:
            self.numTries += 1
            return  False
        else:
            currentStatus = ''
            for i in self.secretWord:
                if i in self.guessedChars:
                    currentStatus += i
                else:
                    currentStatus += '_'
            self.currentStatus = currentStatus
        checker = None
        if self.currentStatus == self.secretWord:
            checker = True
        else :
            checker = False
        return checker
