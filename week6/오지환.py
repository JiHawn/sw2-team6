import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()

        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.initUI()
        self.showScoreDB(self.scoredb, self.key.currentText())
        
        
    def initUI(self):

        self.labels = {'name' : QLabel('Name: '), 'age' : QLabel('Age: '), 'score' : QLabel('Score: '),
                      'amount' : QLabel('Amount: '), 'key' : QLabel("Key: "), 'result' : QLabel('Result')}
        self.edits = {'name' : QLineEdit(), 'age' : QLineEdit(), 'score' : QLineEdit(), 'amount' : QLineEdit(),
                     'result' : QTextEdit()}
        self.buttons = {'add' : QPushButton('Add'), 'del' : QPushButton('Del'), 'find' : QPushButton('Find'),
                       'inc' : QPushButton('Inc'), 'show' : QPushButton('show')}
        self.key = QComboBox()
        self.key.addItem('Name')
        self.key.addItem('Age')
        self.key.addItem('Score')

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.labels['name'])
        hbox1.addWidget(self.edits['name'])
        hbox1.addWidget(self.labels['age'])
        hbox1.addWidget(self.edits['age'])
        hbox1.addWidget(self.labels['score'])
        hbox1.addWidget(self.edits['score'])

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.labels['amount'])
        hbox2.addWidget(self.edits['amount'])
        hbox2.addWidget(self.key)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.buttons['add'])
        hbox3.addWidget(self.buttons['del'])
        hbox3.addWidget(self.buttons['find'])
        hbox3.addWidget(self.buttons['inc'])
        hbox3.addWidget(self.buttons['show'])

        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.labels['result'])

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addWidget(self.edits['result'])

        self.setLayout(vbox)

        self.buttons['add'].clicked.connect(self.buttonClicked)
        self.buttons['del'].clicked.connect(self.buttonClicked)
        self.buttons['find'].clicked.connect(self.buttonClicked)
        self.buttons['inc'].clicked.connect(self.buttonClicked)
        self.buttons['show'].clicked.connect(self.buttonClicked)


        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.doScoreDB(sender.text())

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            print('Empty DB: ', self.dbfilename)
        else:
            print('Open DB: ', self.dbfilename)
        fH.close()
        return self.scoredb

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def doScoreDB(self, order):
        if order == 'Add':
            record = {'Name': self.edits['name'].text(), 'Age': int(self.edits['age'].text()), 'Score': int(self.edits['age'].text())}
            self.scoredb += [record]
            self.showScoreDB(self.scoredb, self.key.currentText())

        elif order == 'Del':
            check_del = False

            not_deleted = []
            for p in self.scoredb:
                if p['Name'] != self.edits['name'].text():
                    not_deleted.append(p)
                    check_del = True
            self.scoredb = not_deleted
            if not (check_del):
                QMessageBox.question(self, 'Error', 'No matching name exist', QMessageBox.Yes)
            self.showScoreDB(self.scoredb, self.key.currentText())

        elif order == 'show':
            sortKey = self.key.currentText()
            self.showScoreDB(self.scoredb, sortKey)

        elif order == 'Find':
            check_find = False
            for p in self.scoredb:
                if p['Name'] == self.edits['name'].text():
                    text = ''
                    for attr in sorted(p):
                        text += attr + "=" + str(p[attr]) + '\t'
                    text += '\n'
                    self.edits['result'].setText(text)
                    check_find = True
            if not (check_find):
                QMessageBox.question(self, 'Error', 'No matching name exist', QMessageBox.Yes)

        elif order == 'Inc':
            for p in self.scoredb:
                if p['Name'] == self.edits['name'].text():
                    p['Score'] += int(self.edits['amount'].text())
            self.showScoreDB(self.scoredb, self.key.currentText())

    def showScoreDB(self, scdb, keyname):
        text_whole = ''
        for p in sorted(scdb, key=lambda person: person[keyname]):
            text_person = ''
            for attr in sorted(p):
                text_person += attr + " = " + str(p[attr]) + '\t'
            text_whole += text_person + '\n'
        self.edits['result'].setText(text_whole)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





