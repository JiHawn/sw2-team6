import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QGridLayout,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):
        '''
        label = ['Name', 'Age', "Score", 'Amount']
        push = ['Add','Del', 'Find', 'Inc', 'Show']
        p_d = ['AddClick', 'DelClick', 'FindClick', 'IncClick', 'ShowClick']

        self.list = []
        self.list2 = []
        self.plist = []
        self.txt = QTextEdit()
        self.combo = QComboBox(self)

        key = QLabel("key", self)
        result = QLabel("Result", self)
        self.scdb = self.readScoreDB()
        print(self.scdb)

        for i in label:
            self.list.append(QLabel(i,self))
            self.list2.append(QLineEdit(self))
            self.combo.addItem(i)
            
        '''
        self.list = []
        self.list2 = []
        # Layout name age score
        name = QLabel("Name", self)
        name.move(15, 10)
        
        age = QLabel("Age", self)
        age.move(195, 10)
        
        score = QLabel("Score", self)
        score.move(375, 10)
        amount = QLabel("Amount", self)
        amount.move(155, 30)
        key = QLabel("Key", self)
        key.move(400, 30)

        result = QLabel("Result", self)
        result.move(15, 450)
        
        nameEdit = QLineEdit()
        ageEdit = QLineEdit()
        scoreEdit = QLineEdit()
        amountEdit = QLineEdit()

        
        keyEdit = QComboBox(self)
        keyEdit.addItem("Name")
        keyEdit.addItem("Age")
        keyEdit.addItem("Score")

        keyEdit.move(450, 30)
        keyEdit.activated[str].connect(self.onActivated)
        
        resultEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(name, 1, 0)
        grid.addWidget(nameEdit, 1, 1)

        grid.addWidget(age, 1, 2)
        grid.addWidget(ageEdit, 1, 3)


        grid.addWidget(score, 1, 4)
        grid.addWidget(scoreEdit, 1, 5)

        grid.addWidget(amount, 2, 0)
        grid.addWidget(amountEdit, 2, 1)

        grid.addWidget(result, 3, 0)
        grid.addWidget(resultEdit, 10, 1, 10, 10)

        self.setLayout(grid)
       
        
        
        # button add del find inc show
        btn1 = QPushButton("Add", self)
        btn1.move(100, 70)

        btn2 = QPushButton("Del", self)
        btn2.move(190, 70)
        btn3 = QPushButton("Find", self)
        btn3.move(280, 70)
        btn4 = QPushButton("Inc", self)
        btn4.move(370, 70)
        btn5 = QPushButton("Show", self)
        btn5.move(460, 70)
        
        btn1.clicked.connect(self.button1)
        btn2.clicked.connect(self.button2)
        btn3.clicked.connect(self.button3)
        btn4.clicked.connect(self.button4)
        btn5.clicked.connect(self.button5)

        self.setGeometry(600, 600, 590, 450)
        self.setWindowTitle("Event sender")
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def button1(self):
        sender = self.sender()
        '''record = {"Name":self.list2[0].text(), 'Age':self.list2[1].text(),'Score':self.list2[2].text()}
        self.scdb +=[record]
        self.resultEdit.setText("")
        self.showScoreDB()
'''
    def button2(self):
        sender = self.sender()
    def button3(self):
        sender = self.sender()
    def button4(self):
        sender = self.sender()
    def button5(self):
        sender = self.sender()

        
    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            print("New:", self.dbfilname)
            return []
        self.scdb = []
        try:
            self.scoredb =  pickle.load(fH)
        except:
            print("Empty", self.dbfilename)
        else:
            print("Open:", self.dbfilename)
        fH.close()
        
        return self.scdb

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scdb, fH)
        fH.close()

    def showScoreDB(self):
        for i in range(len(self.scdb)):
            self.resultEdit.append("%s %29s %29s %29s %29s %29s %29s"%('Name', str(self.scdb[i]['Name']),
                                                                   'Age', str(self.scdb[i]['Age']),
                                                                   "Score", str(self.scdb[i]['Score'])))
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





