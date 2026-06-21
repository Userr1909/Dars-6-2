# Berilgan vazifalarni PyQt5 da bajaring.
# Vazifalarni bajarishda yangi classlar hosil qilish talab qilinmaydi.

# 1-masala. Tugmacha bosilganda Labelga 1 va 100 orasidagi random sonni chiqaruvchi dastur yozing.
import os
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont

os.system("cls")

class RandomSonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.oyna_sozlamalari()
        self.vidjetlarni_yaratish()

    def oyna_sozlamalari(self):
        self.setWindowTitle("Super App - Random")
        self.setGeometry(1400, 200, 405, 720)
        self.setStyleSheet("background-color: #8cd9fa;")
        self.font1 = QFont("Comic Sans MS", 30)

    def vidjetlarni_yaratish(self):
        self.text1 = QLabel("0", self)  
        self.text1.setFont(self.font1)
        self.text1.setGeometry(25, 50, 355, 80)
        self.text1.setStyleSheet("color: red; font-weight: bold;")
        self.text1.setProperty("alignment", 0x0004 | 0x0080)

        self.btn1 = QPushButton("Random Son", self)
        self.btn1.setGeometry(125, 300, 155, 50)
        self.btn1.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            background-color: #22c70c;
            border-radius: 25px;
            border: 2px solid black;
        """)
        self.btn1.clicked.connect(self.tasodifiy_son_chiqar)

    def tasodifiy_son_chiqar(self):
        son = random.randint(1, 100)
        self.text1.setText(str(son))
if __name__ == "__main__":
    app = QApplication([])
    dastur = RandomSonApp()
    dastur.show()
    app.exec_()