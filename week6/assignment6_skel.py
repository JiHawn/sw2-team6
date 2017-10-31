import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
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

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
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

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





