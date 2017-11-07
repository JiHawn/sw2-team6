from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from math import *
import time


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        
        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        for i in range(10):
            self.digitButton[i] = Button(str(i), self.buttonClicked)

        # . and = Buttons
        self.decButton = Button('.', self.buttonClicked)
        self.eqButton = Button('=', self.buttonClicked)

        # Operator Buttons
        self.mulButton = Button('*', self.buttonClicked)
        self.divButton = Button('/', self.buttonClicked)
        self.addButton = Button('+', self.buttonClicked)
        self.subButton = Button('-', self.buttonClicked)

        # Parentheses Buttons
        self.lparButton = Button('(', self.buttonClicked)
        self.rparButton = Button(')', self.buttonClicked)

        # Clear Button
        self.clearButton = Button('C', self.buttonClicked)
        self.delButton = Button("Del", self.buttonClicked)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        # functions
        self.factoButton = Button('factorial', self.buttonClicked)
        self.binButton = Button('binary', self.buttonClicked)
        self.bindecButton = Button('bin->dec',self.buttonClicked)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        numLayout.addWidget(self.digitButton[0], 3, 0)

        for i in range(10):
            numLayout.addWidget(self.digitButton[i], (9-i)/3, (i-1)%3 )

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)
        
        opLayout.addWidget(self.clearButton, 3, 0)
        opLayout.addWidget(self.delButton, 3, 1)

        opLayout.addWidget(self.factoButton, 5,1)
        opLayout.addWidget(self.binButton, 6,1)
        opLayout.addWidget(self.bindecButton, 7,1)
        
        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)
        
        self.setWindowTitle("My Calculator")

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        length = len(self.display.text())

        if key == '=':
            if (self.display.text()[length-1] == "+") or (self.display.text()[length-1] == "-") or (self.display.text()[length-1] == "*") or (self.display.text()[length-1] == "/") or (self.display.text()[length-1] == ")") or (self.display.text()[length-1] == "("):
                self.display.setText('')
                self.display.setText('ERROR')
                time.sleep(1)
                self.display.setText('')
            else:
                result = str(eval(self.display.text()))
                self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        elif key == "Del":
            self.display.setText(self.display.text()[0:length-1])
        elif key == "factorial" :
            self.display.setText(str(factorial(int(self.display.text()))))
        elif key == "binary" :
            self.display.setText(str(bin(int(self.display.text()))))
        elif key == "bin ->dec" :
            self.display.setText(str(int(self.display.text())))
        else:
            self.display.setText(self.display.text() + key)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
