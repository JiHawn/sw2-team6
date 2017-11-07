import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
<<<<<<< HEAD
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
=======
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QGridLayout,
>>>>>>> 7185f65e4e8cd720ddf20659b94d5209b4992cc0
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
<<<<<<< HEAD
     

 

    def initUI(self):
        nameLabel = QLabel("Name:",self)
        self.nameLine = QLineEdit()
        ageLabel = QLabel("Age:",self)
        self.ageLine = QLineEdit()
        scoreLabel = QLabel("Score:",self)
        self.scoreLine = QLineEdit()

        Box1 = QHBoxLayout()
        Box1.addWidget(nameLabel)
        Box1.addWidget(self.nameLine)
        Box1.addWidget(ageLabel)
        Box1.addWidget(self.ageLine)
        Box1.addWidget(scoreLabel)
        Box1.addWidget(self.scoreLine)

        spaceLabel = QLabel("               ",self)
        amountLabel = QLabel("Amount: ",self)
        self.amountLineBox = QLineEdit()
        keyLabel = QLabel("key:")
        self.keyComboBox = QComboBox()
        self.keyComboBox.addItem("Name")
        self.keyComboBox.addItem("Score")
        self.keyComboBox.addItem("Age")

        Box2 = QHBoxLayout()
        Box2.addWidget(spaceLabel)
        Box2.addWidget(amountLabel)
        Box2.addWidget(self.amountLineBox)
        Box2.addWidget(keyLabel)
        Box2.addWidget(self.keyComboBox)

        spaceLabel2 = QLabel('                  ',self)
        addButton = QPushButton("Add",self)
        delButton = QPushButton("Del",self)
        findButton = QPushButton("Find",self)
        incButton = QPushButton("Inc",self)
        showButton = QPushButton("Show",self)

        addButton.clicked.connect(self.AddClicked)
        delButton.clicked.connect(self.DelClicked)
        findButton.clicked.connect(self.FindClicked)
        incButton.clicked.connect(self.IncClicked)
        showButton.clicked.connect(self.ShowClicked)

        Box3 = QHBoxLayout()
        Box3.addWidget(spaceLabel2)
        Box3.addWidget(addButton)
        Box3.addWidget(delButton)
        Box3.addWidget(findButton)
        Box3.addWidget(incButton)
        Box3.addWidget(showButton)

        resultLabel = QLabel("Result: ")

        Box4 = QHBoxLayout()
        Box4.addWidget(resultLabel)

        self.textBox = QTextEdit(self)

        Box5 = QHBoxLayout()
        Box5.addWidget(self.textBox)


        qvBox = QVBoxLayout()
        qvBox.addLayout(Box1)
        qvBox.addLayout(Box2)
        qvBox.addLayout(Box3)
        qvBox.addLayout(Box4)
        qvBox.addLayout(Box5)
        self.setLayout(qvBox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('DataBaseManager')
        

        self.show()
    def ShowClicked(self):
        self.showScoreDB(self.keyComboBox.currentText())

    def AddClicked(self):
        record = {'Name': self.nameLine.text(),'Age': int(self.ageLine.text()),'Score':int(self.scoreLine.text())}
        self.scoredb += [record]
        self.showScoreDB()

    def DelClicked(self):
        reverse_scdb = sorted(self.scoredb,key=lambda x: x["Name"],reverse=True)
        for p in reverse_scdb:
            if p['Name'] == self.nameLine.text():
                self.scoredb.remove(p)
        self.showScoreDB()
    def FindClicked(self):
        temp = ""
        for p in sorted(self.scoredb , key=lambda person: person["Name"]):        
            for attr in sorted(p):
                if p["Name"] == self.nameLine.text():
                    temp += attr + "=" + str(p[attr]) + " "

            temp += "\n"
        self.textBox.setText(temp)      
    def IncClicked(self):
        for p in sorted(self.scoredb , key=lambda person: person["Name"]):        
            for attr in sorted(p):
                if p["Name"] == self.nameLine.text():
                    p["Score"] += int(self.amountBox.text())
                    break;
        self.showScoreDB(); 



    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Escape:
            self.close()

=======
        
        
    def initUI(self):
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
    def button2(self):
        sender = self.sender()
    def button3(self):
        sender = self.sender()
    def button4(self):
        sender = self.sender()
    def button5(self):
        sender = self.sender()

        
>>>>>>> 7185f65e4e8cd720ddf20659b94d5209b4992cc0
    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
<<<<<<< HEAD
            self.scoredb = []
            return
        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            for i in self.scoredb:
                i['Age'] = int(i['Age'])
                i['Score'] = int(i['Score'])
        fH.close()


    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self,keyname="Score"):
        tmp = ""
        for p in sorted(self.scoredb , key=lambda person: person[keyname]):
            for attr in sorted(p):
                tmp += attr + "=" + str(p[attr]) + " "

            tmp += "\n"
        self.textBox.setText(tmp)

=======
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
        
        
>>>>>>> 7185f65e4e8cd720ddf20659b94d5209b4992cc0
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





