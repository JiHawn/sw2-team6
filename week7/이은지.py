from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

class Button(QToolButton):

    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size




class Calculator(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        self.txt = ""
        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]
        for i in range(10):
            self.digitButton[i] = Button(str(i))
            self.digitButton[i].clicked.connect(self.buttonClicked)
        # . and = Buttons
        self.decButton = Button('.')
        self.eqButton = Button('=')
        self.decButton.clicked.connect(self.buttonClicked)
        self.eqButton.clicked.connect(self.buttonClicked)
        # Operator Buttons
        self.mulButton = Button('*')
        self.divButton = Button('/')
        self.addButton = Button('+')
        self.subButton = Button('-')
        self.mulButton.clicked.connect(self.buttonClicked)
        self.divButton.clicked.connect(self.buttonClicked)
        self.addButton.clicked.connect(self.buttonClicked)
        self.subButton.clicked.connect(self.buttonClicked)

        # Parentheses Buttons
        self.lparButton = Button('(')
        self.rparButton = Button(')')
        self.lparButton.clicked.connect(self.buttonClicked)
        self.rparButton.clicked.connect(self.buttonClicked)
        # Clear Button
        self.clearButton = Button('C')
        self.clearButton.clicked.connect(self.buttonClicked)
        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()
        numLayout.addWidget(self.digitButton[0],3,0)
        j = 3
        for i in range(10):
            numLayout.addWidget(self.digitButton[i], j, (i-1)%3)
            if (i)% 3 == 0:
                j -=1
            else:
                j+0

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
        
        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)
        
        self.setWindowTitle("My Calculator")
    def buttonClicked(self):
        sender = self.sender()
        self.doButton(sender.text())

    def doButton(self, order):

        if order != '=':
            if order == 'C':
                self.txt = ""
                self.display.setText(self.txt)

            else:
                self.txt += order
                self.display.setText(self.txt)
        else:
            self.txt = str(eval(self.txt))
            self.display.setText(self.txt)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
