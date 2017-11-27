class Guess:
    def __init__(self, word):
        self.numTries = 0
        self.guessedChars = []
        self.secretWord = word
        self.currentStatus = ''
        for i in range(len(self.secretWord)):
            self.currentStatus += '_'

    def display(self):
        print('Current: ' + self.currentStatus)
        print('Tries: ' + str(self.numTries))

    def guess(self, character):
        character = character.lower()
        self.guessedChars.append(character)
        finished = False
        if character in self.secretWord:
            for i in range(len(self.secretWord)):
                if self.secretWord[i] == character:
                    self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i+1:]
            if self.secretWord == self.currentStatus:
                finished = True
        else:
            self.numTries += 1
        return finished
