# 2-masala. 1ta label va 3ta Button yarating va 1-buttonni bosganda Ismingiz, 2-buttonni bosganda Familiyangiz va 
# 3-buttonni bosganda tug'ilgan sanangiz Labelda chiqarib beruvchi dastur yozing. 
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont

os.system("cls")

class MalumotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.oyna_sozlamalari()
        self.vidjetlarni_yaratish()

    def oyna_sozlamalari(self):
        self.setWindowTitle("Super App - Ma'lumotlar")
        self.setGeometry(1400, 200, 405, 720)
        self.setStyleSheet("background-color: #8cd9fa;")
        self.font1 = QFont("Comic Sans MS", 24)

    def vidjetlarni_yaratish(self):
        self.text1 = QLabel("Ma'lumotni tanlang", self)
        self.text1.setFont(self.font1)
        self.text1.setGeometry(25, 60, 355, 80)
        self.text1.setStyleSheet("color: red; font-weight: bold;")

        self.btn1 = QPushButton("Ism", self)
        self.btn1.setGeometry(125, 200, 155, 50)
        self.btn1.setStyleSheet(self.tugma_stili())
        self.btn1.clicked.connect(self.ko_rsat_ism)

        self.btn2 = QPushButton("Familiya", self)
        self.btn2.setGeometry(125, 280, 155, 50)
        self.btn2.setStyleSheet(self.tugma_stili())
        self.btn2.clicked.connect(self.ko_rsat_familiya)

        self.btn3 = QPushButton("Tug'ilgan sana", self)
        self.btn3.setGeometry(125, 360, 155, 50)
        self.btn3.setStyleSheet(self.tugma_stili())
        self.btn3.clicked.connect(self.ko_rsat_sana)

    def tugma_stili(self):
        return """
            font-size: 18px;
            font-weight: bold;
            background-color: #22c70c;
            border-radius: 25px;
            border: 2px solid black;
        """

    def ko_rsat_ism(self):
        self.text1.setText("Alijon")

    def ko_rsat_familiya(self):
        self.text1.setText("Valiyev")

    def ko_rsat_sana(self):
        self.text1.setText("15.08.2005")

if __name__ == "__main__":
    app = QApplication([])
    dastur = MalumotApp()
    dastur.show()
    app.exec_()
