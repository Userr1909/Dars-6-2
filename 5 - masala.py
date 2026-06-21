# 5-masala. Parol tekshiruvchi kichik ilova
# Oynaga bir LineEdit (parol kiritish uchun), bir Button va bir Label joylashtiring. Button bosilganda agar LineEditga "12345" yozilgan bo'lsa:
# Label -> "Parol to'g'ri" matnini ko'rsatadi.
# Aks holda:
# Label -> "Noto'g'ri parol" matnini ko'rsatadi.
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont

os.system("cls")

class ParolApp(QWidget):
    def __init__(self):
        super().__init__()
        self.oyna_sozlamalari()
        self.vidjetlarni_yaratish()

    def oyna_sozlamalari(self):
        self.setWindowTitle("Parol Tekshirgich")
        self.setGeometry(1400, 200, 405, 720)
        self.setStyleSheet("background-color: #8cd9fa;")
        self.font1 = QFont("Comic Sans MS", 22)

    def vidjetlarni_yaratish(self):
        self.line_parol = QLineEdit(self)
        self.line_parol.setGeometry(25, 60, 355, 50)
        self.line_parol.setPlaceholderText("Parolni kiriting...")
        self.line_parol.setEchoMode(QLineEdit.Password)
        self.line_parol.setFont(QFont("Arial", 16))
        self.line_parol.setStyleSheet("background-color: white; border: 2px solid black;")

        self.text1 = QLabel("Tizimga kirish", self)
        self.text1.setFont(self.font1)
        self.text1.setGeometry(25, 140, 355, 60)
        self.text1.setStyleSheet("color: black; font-weight: bold;")

        self.btn1 = QPushButton("Tekshirish", self)
        self.btn1.setGeometry(125, 240, 155, 50)
        self.btn1.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            background-color: #22c70c;
            border-radius: 25px;
            border: 2px solid black;
        """)
        self.btn1.clicked.connect(self.tekshir)

    def tekshir(self):
        kiritilgan_parol = self.line_parol.text()
        
        if kiritilgan_parol == "12345":
            self.text1.setText("Parol to'g'ri")
            self.text1.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.text1.setText("Noto'g'ri parol")
            self.text1.setStyleSheet("color: red; font-weight: bold;")

if __name__ == "__main__":
    app = QApplication([])
    dastur = ParolApp()
    dastur.show()
    app.exec_()
