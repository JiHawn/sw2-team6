import  sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit,QWidget,QLabel, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
class Calculator(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUI()
#----------------------------------------------------------
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        grid.addWidget(self.display, 0, 0, 1, 5)
        names = [
        '7', '8', '9', '*','/',
        '4', '5', '6', '+','-',
        '1', '2', '3', '(',')',
        '0', '.', '=', 'C',   ]
        positions = [(i+1, j) for i in range(4)for j in range(5)]
        for position, name in zip(positions, names):
            button = QPushButton(name)
            button.clicked.connect(self.buttonClicked)
            grid.addWidget(button,*position)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('My Calculator')

    def buttonClicked(self):
        sender = self.sender();
        # self.display.setText(sender.text())
        key = sender.text()
        if key == "=":
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == "C":
            self.display.setText('0')
        else:
            if(self.display.text()=="0"):
                self.display.setText('')
            self.display.setText(self.display.text() + key)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc= Calculator()
    calc.show()
    sys.exit((app.exec_()))
