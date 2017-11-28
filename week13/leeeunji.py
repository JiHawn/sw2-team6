class Guess:

    def __init__(self, word):
        self.word = word
        self.guessedChars = []
        self.numTries = 0
        self.tries = 0 # total tries

        self.sentence = ["_"]*len(self.word)
        self.currentStatus = "_"*len(self.word) # ['_','_'] 이렇게 안보이기 위해


    def display(self):
        print("Current :", self.currentStatus)
        print("Fail Tries: ", self.numTries)
        print("Total Tries:", self.tries)

    def guess(self, character):
        check = 0
        self.currentStatus = ""
        self.guessedChars.append(character)

        for i in range(len(self.word)):
            if self.word[i] == character:
                check += 1
                self.sentence[i] = character
            self.currentStatus += self.sentence[i]

        if check == 0:
            self.numTries += 1
            self.tries += 1
        else:
            self.tries +=1

        if self.word == self.currentStatus:
            return True
        else:
            return False
