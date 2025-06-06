from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from demo_signup_window import SignUp_Window

font = QFont("Cordia New", 16)

class SignUp_Button(QPushButton):
    def __init__(self):
        super().__init__()

        # Setting Up SignUp Button
        self.setText("ลงทะเบียน")
        self.setFont(font)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet(
            "QPushButton{border:none; color:blue; text-decoration:underline;}"
            "QPushButton:hover{color: red;}"
        )

        # Setting Up Connect Function
        self.clicked.connect(self.open_signup_window)

    def open_signup_window(self):
        self.signup_window = SignUp_Window()
        self.signup_window.show()